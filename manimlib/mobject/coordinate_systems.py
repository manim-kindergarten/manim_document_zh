import numpy as np
import numbers

from manimlib.constants import *
from manimlib.mobject.functions import ParametricFunction
from manimlib.mobject.geometry import Arrow
from manimlib.mobject.geometry import Line
from manimlib.mobject.number_line import NumberLine
from manimlib.mobject.svg.tex_mobject import TexMobject
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.utils.config_ops import digest_config
from manimlib.utils.config_ops import merge_dicts_recursively
from manimlib.utils.simple_functions import binary_search
from manimlib.utils.space_ops import angle_of_vector

# TODO: There should be much more code reuse between Axes, NumberPlane and GraphScene


class CoordinateSystem():
    """坐标系统(Axes, NumberPlane)的抽象基类
    
    - ``dimension`` : 坐标系统维度
    - ``x_min, x_max`` : x轴范围(默认全屏)
    - ``y_min, y_max`` : y轴范围(默认全屏)
    """
    CONFIG = {
        "dimension": 2,
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "y_min": -FRAME_Y_RADIUS,
        "y_max": FRAME_Y_RADIUS,
    }

    def coords_to_point(self, *coords):
        raise Exception("Not implemented")

    def point_to_coords(self, point):
        raise Exception("Not implemented")

    def c2p(self, *coords):
        """Abbreviation for coords_to_point"""
        return self.coords_to_point(*coords)

    def p2c(self, point):
        """Abbreviation for point_to_coords"""
        return self.point_to_coords(point)

    def get_axes(self):
        raise Exception("Not implemented")

    def get_axis(self, index):
        return self.get_axes()[index]

    def get_x_axis(self):
        return self.get_axis(0)

    def get_y_axis(self):
        return self.get_axis(1)

    def get_z_axis(self):
        return self.get_axis(2)

    def get_x_axis_label(self, label_tex, edge=RIGHT, direction=DL, **kwargs):
        """获取x轴上的标志"""
        return self.get_axis_label(
            label_tex, self.get_x_axis(),
            edge, direction, **kwargs
        )

    def get_y_axis_label(self, label_tex, edge=UP, direction=DR, **kwargs):
        """获取y轴上的标志"""
        return self.get_axis_label(
            label_tex, self.get_y_axis(),
            edge, direction, **kwargs
        )

    def get_axis_label(self, label_tex, axis, edge, direction, buff=MED_SMALL_BUFF):
        label = TexMobject(label_tex)
        label.next_to(
            axis.get_edge_center(edge), direction,
            buff=buff
        )
        label.shift_onto_screen(buff=MED_SMALL_BUFF)
        return label

    def get_axis_labels(self, x_label_tex="x", y_label_tex="y"):
        """获取x轴和y轴上的标志（一个VGroup）"""
        self.axis_labels = VGroup(
            self.get_x_axis_label(x_label_tex),
            self.get_y_axis_label(y_label_tex),
        )
        return self.axis_labels

    def get_graph(self, function, **kwargs):
        """获取函数图像（使用 ``ParametricFunction`` ）"""
        x_min = kwargs.pop("x_min", self.x_min)
        x_max = kwargs.pop("x_max", self.x_max)
        graph = ParametricFunction(
            lambda t: self.coords_to_point(t, function(t)),
            t_min=x_min,
            t_max=x_max,
            **kwargs
        )
        graph.underlying_function = function
        return graph

    def get_parametric_curve(self, function, **kwargs):
        """获取参数方程图像（使用 ``ParametricFunction`` ）"""
        dim = self.dimension
        graph = ParametricFunction(
            lambda t: self.coords_to_point(
                *function(t)[:dim]
            ),
            **kwargs
        )
        graph.underlying_function = function
        return graph

    def input_to_graph_point(self, x, graph):
        """返回图像 ``graph`` 上横坐标为 ``x`` 的点"""
        if hasattr(graph, "underlying_function"):
            return self.coords_to_point(x, graph.underlying_function(x))
        else:
            alpha = binary_search(
                function=lambda a: self.point_to_coords(
                    graph.point_from_proportion(a)
                )[0],
                target=x,
                lower_bound=self.x_min,
                upper_bound=self.x_max,
            )
            if alpha is not None:
                return graph.point_from_proportion(alpha)
            else:
                return None


class Axes(VGroup, CoordinateSystem):
    """直角坐标系"""
    CONFIG = {
        "number_line_config": {
            "color": LIGHT_GREY,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
        },
        "x_axis_config": {},
        "y_axis_config": {
            "label_direction": LEFT,
        },
        "center_point": ORIGIN,
    }

    def __init__(self, **kwargs):
        """由两个 ``NumberLine`` 构成 ( ``Axes.axes=VGroup(Axes.x_axis, Axes.y_axis`` ))
        
        - ``number_line_config`` : x/y轴共有的属性
        - ``x_axis_config`` : x轴特有的属性
        - ``y_axis_config`` : y轴特有的属性
        - ``center_point`` : 原点的位置
        """
        VGroup.__init__(self, **kwargs)
        self.x_axis = self.create_axis(
            self.x_min, self.x_max, self.x_axis_config
        )
        self.y_axis = self.create_axis(
            self.y_min, self.y_max, self.y_axis_config
        )
        self.y_axis.rotate(90 * DEGREES, about_point=ORIGIN)
        # Add as a separate group incase various other
        # mobjects are added to self, as for example in
        # NumberPlane below
        self.axes = VGroup(self.x_axis, self.y_axis)
        self.add(*self.axes)
        self.shift(self.center_point)

    def create_axis(self, min_val, max_val, axis_config):
        new_config = merge_dicts_recursively(
            self.number_line_config,
            {"x_min": min_val, "x_max": max_val},
            axis_config,
        )
        return NumberLine(**new_config)

    def coords_to_point(self, *coords):
        """在该坐标系里的坐标转化为在画面上的点"""
        origin = self.x_axis.number_to_point(0)
        result = np.array(origin)
        for axis, coord in zip(self.get_axes(), coords):
            result += (axis.number_to_point(coord) - origin)
        return result

    def c2p(self, *coords):
        """``coords_to_point`` 的缩写"""
        return self.coords_to_point(*coords)

    def point_to_coords(self, point):
        """在画面上的点转化为在在该坐标系里的坐标"""
        return tuple([
            axis.point_to_number(point)
            for axis in self.get_axes()
        ])

    def p2c(self, point):
        """``point_to_coords`` 的缩写"""
        return self.point_to_coords(point)

    def get_axes(self):
        return self.axes

    def get_coordinate_labels(self, x_vals=None, y_vals=None, **kwargs):
        """获取坐标轴上的数字

        - ``x_vals`` : x轴上需要的数字（默认为空，即全需要）
        - ``y_vals`` : y轴上需要的数字（默认为空，即全需要）
        """
        if x_vals is None:
            x_vals = []
        if y_vals is None:
            y_vals = []
        x_mobs = self.get_x_axis().get_number_mobjects(*x_vals, **kwargs)
        y_mobs = self.get_y_axis().get_number_mobjects(*y_vals, **kwargs)

        self.coordinate_labels = VGroup(x_mobs, y_mobs)
        return self.coordinate_labels

    def add_coordinates(self, x_vals=None, y_vals=None, **kwargs):
        """添加坐标轴上的数字（将 ``get_coordinate_labels`` 返回的添加到场景中）"""
        self.add(self.get_coordinate_labels(x_vals, y_vals, **kwargs))
        return self


class ThreeDAxes(Axes):
    """空间直角坐标系"""
    CONFIG = {
        "dimension": 3,
        "x_min": -5.5,
        "x_max": 5.5,
        "y_min": -5.5,
        "y_max": 5.5,
        "z_axis_config": {},
        "z_min": -3.5,
        "z_max": 3.5,
        "z_normal": DOWN,
        "num_axis_pieces": 20,
        "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
    }

    def __init__(self, **kwargs):
        """在 ``Axes`` 基础上加了一个轴
        
        - ``z_axis_config`` : z轴特有的属性
        - ``num_axis_piece`` : 每个轴需要拆成的部分，默认20（简单解决3D中遮盖问题）
        - ``light_source`` : 虚拟光源的位置
        - 其余同 ``Axes``
        """
        Axes.__init__(self, **kwargs)
        z_axis = self.z_axis = self.create_axis(
            self.z_min, self.z_max, self.z_axis_config
        )
        z_axis.rotate(-np.pi / 2, UP, about_point=ORIGIN)
        z_axis.rotate(
            angle_of_vector(self.z_normal), OUT,
            about_point=ORIGIN
        )
        self.axes.add(z_axis)
        self.add(z_axis)

        self.add_3d_pieces()
        self.set_axis_shading()

    def add_3d_pieces(self):
        for axis in self.axes:
            axis.pieces = VGroup(
                *axis.get_pieces(self.num_axis_pieces)
            )
            axis.add(axis.pieces)
            axis.set_stroke(width=0, family=False)
            axis.set_shade_in_3d(True)

    def set_axis_shading(self):
        def make_func(axis):
            vect = self.light_source
            return lambda: (
                axis.get_edge_center(-vect),
                axis.get_edge_center(vect),
            )
        for axis in self:
            for submob in axis.family_members_with_points():
                submob.get_gradient_start_and_end_points = make_func(axis)
                submob.get_unit_normal = lambda a: np.ones(3)
                submob.set_sheen(0.2)


class NumberPlane(Axes):
    """坐标平面"""
    CONFIG = {
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        },
        "y_axis_config": {
            "label_direction": DR,
        },
        "background_line_style": {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 1,
        },
        # Defaults to a faded version of line_config
        "faded_line_style": None,
        "x_line_frequency": 1,
        "y_line_frequency": 1,
        "faded_line_ratio": 1,
        "make_smooth_after_applying_functions": True,
    }

    def __init__(self, **kwargs):
        """与 ``Axes`` 类似
        
        - ``axis_config`` : 坐标轴的共有属性（也可写为 ``number_line_config`` ）
        - ``x_axis_config, y_axis_config`` : x/y轴的特有属性
        - ``background_line_style`` : 背景直线的样式
        - ``fade_line_style`` : 背景中较暗直线的样式，默认为None
        - ``x_line_frequency, y_line_frequency`` : 背景直线的频率
        - ``faded_line_ratio`` : 背景中较暗直线的所占比例
        - 其余同 ``Axes``
        """
        digest_config(self, kwargs)
        kwargs["number_line_config"] = self.axis_config
        Axes.__init__(self, **kwargs)
        self.init_background_lines()

    def init_background_lines(self):
        if self.faded_line_style is None:
            style = dict(self.background_line_style)
            # For anything numerical, like stroke_width
            # and stroke_opacity, chop it in half
            for key in style:
                if isinstance(style[key], numbers.Number):
                    style[key] *= 0.5
            self.faded_line_style = style

        self.background_lines, self.faded_lines = self.get_lines()
        self.background_lines.set_style(
            **self.background_line_style,
        )
        self.faded_lines.set_style(
            **self.faded_line_style,
        )
        self.add_to_back(
            self.faded_lines,
            self.background_lines,
        )

    def get_lines(self):
        x_axis = self.get_x_axis()
        y_axis = self.get_y_axis()
        x_freq = self.x_line_frequency
        y_freq = self.y_line_frequency

        x_lines1, x_lines2 = self.get_lines_parallel_to_axis(
            x_axis, y_axis, x_freq,
            self.faded_line_ratio,
        )
        y_lines1, y_lines2 = self.get_lines_parallel_to_axis(
            y_axis, x_axis, y_freq,
            self.faded_line_ratio,
        )
        lines1 = VGroup(*x_lines1, *y_lines1)
        lines2 = VGroup(*x_lines2, *y_lines2)
        return lines1, lines2

    def get_lines_parallel_to_axis(self, axis1, axis2, freq, ratio):
        line = Line(axis1.get_start(), axis1.get_end())
        dense_freq = (1 + ratio)
        step = (1 / dense_freq) * freq

        lines1 = VGroup()
        lines2 = VGroup()
        ranges = (
            np.arange(0, axis2.x_max, step),
            np.arange(0, axis2.x_min, -step),
        )
        for inputs in ranges:
            for k, x in enumerate(inputs):
                new_line = line.copy()
                new_line.move_to(axis2.number_to_point(x))
                if k % (1 + ratio) == 0:
                    lines1.add(new_line)
                else:
                    lines2.add(new_line)
        return lines1, lines2

    def get_center_point(self):
        return self.coords_to_point(0, 0)

    def get_x_unit_size(self):
        return self.get_x_axis().get_unit_size()

    def get_y_unit_size(self):
        return self.get_x_axis().get_unit_size()

    def get_axes(self):
        return self.axes

    def get_vector(self, coords, **kwargs):
        """获取一个从原点到 ``coords`` 的向量( ``Arrow`` )"""
        kwargs["buff"] = 0
        return Arrow(
            self.coords_to_point(0, 0),
            self.coords_to_point(*coords),
            **kwargs
        )

    def prepare_for_nonlinear_transform(self, num_inserted_curves=50):
        """将所有线拆成 ``num_inserted_curves`` 段，以执行非线性变换"""
        for mob in self.family_members_with_points():
            num_curves = mob.get_num_curves()
            if num_inserted_curves > num_curves:
                mob.insert_n_curves(
                    num_inserted_curves - num_curves
                )
        return self


class ComplexPlane(NumberPlane):
    """复平面"""
    CONFIG = {
        "color": BLUE,
        "line_frequency": 1,
    }

    def number_to_point(self, number):
        """复平面中一个复数转化为画面中的点"""
        number = complex(number)
        return self.coords_to_point(number.real, number.imag)

    def n2p(self, number):
        """``number_to_point`` 的简写"""
        return self.number_to_point(number)

    def point_to_number(self, point):
        """画面中的点转化为复平面中一个复数"""
        x, y = self.point_to_coords(point)
        return complex(x, y)

    def p2n(self, point):
        """``point_to_number`` 的简写"""
        return self.point_to_number(point)

    def get_default_coordinate_values(self):
        x_numbers = self.get_x_axis().default_numbers_to_display()
        y_numbers = self.get_y_axis().default_numbers_to_display()
        y_numbers = [
            complex(0, y) for y in y_numbers if y != 0
        ]
        return [*x_numbers, *y_numbers]

    def get_coordinate_labels(self, *numbers, **kwargs):
        """获取坐标轴上数字物体，传入多个实数或纯虚数 ``numbers``"""
        if len(numbers) == 0:
            numbers = self.get_default_coordinate_values()

        self.coordinate_labels = VGroup()
        for number in numbers:
            z = complex(number)
            if abs(z.imag) > abs(z.real):
                axis = self.get_y_axis()
                value = z.imag
                kwargs = merge_dicts_recursively(
                    kwargs,
                    {"number_config": {"unit": "i"}},
                )
            else:
                axis = self.get_x_axis()
                value = z.real
            number_mob = axis.get_number_mobject(value, **kwargs)
            self.coordinate_labels.add(number_mob)
        return self.coordinate_labels

    def add_coordinates(self, *numbers):
        """将坐标轴上数字添加到场景中（传入多个实数或纯虚数 ``numbers`` ）"""
        self.add(self.get_coordinate_labels(*numbers))
        return self
