import warnings
import numpy as np

from manimlib.constants import *
from manimlib.mobject.mobject import Mobject
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.mobject.types.vectorized_mobject import DashedVMobject
from manimlib.utils.config_ops import digest_config
from manimlib.utils.iterables import adjacent_n_tuples
from manimlib.utils.iterables import adjacent_pairs
from manimlib.utils.simple_functions import fdiv
from manimlib.utils.space_ops import angle_of_vector
from manimlib.utils.space_ops import angle_between_vectors
from manimlib.utils.space_ops import compass_directions
from manimlib.utils.space_ops import line_intersection
from manimlib.utils.space_ops import get_norm
from manimlib.utils.space_ops import normalize
from manimlib.utils.space_ops import rotate_vector


DEFAULT_DOT_RADIUS = 0.08
DEFAULT_SMALL_DOT_RADIUS = 0.04
DEFAULT_DASH_LENGTH = 0.05
DEFAULT_ARROW_TIP_LENGTH = 0.35


class TipableVMobject(VMobject):
    """可以带箭头的物体（实现了和箭头tip有关的方法）
    
    - ``tip_length`` : 默认的箭头长度（默认为0.35）
    - ``tip_style`` : 默认的箭头样式（默认有填充无线条）
    """
    CONFIG = {
        "tip_length": DEFAULT_ARROW_TIP_LENGTH,
        # TODO
        "normal_vector": OUT,
        "tip_style": {
            "fill_opacity": 1,
            "stroke_width": 0,
        }
    }
    
    # Adding, Creating, Modifying tips

    def add_tip(self, tip_length=None, at_start=False):
        """添加箭头

        - ``tip_length`` : 强制箭头长度（不填则为默认长度）
        - ``at_start`` : True时在开头添加箭头，反之在结尾（默认为False在末尾）
        """
        tip = self.create_tip(tip_length, at_start)
        self.reset_endpoints_based_on_tip(tip, at_start)
        self.asign_tip_attr(tip, at_start)
        self.add(tip)
        return self

    def create_tip(self, tip_length=None, at_start=False):
        """返回箭头，参数同 ``add_tip``"""
        tip = self.get_unpositioned_tip(tip_length)
        self.position_tip(tip, at_start)
        return tip

    def get_unpositioned_tip(self, tip_length=None):
        """返回没有定位的箭头，参数只有 ``tip_length``"""
        if tip_length is None:
            tip_length = self.get_default_tip_length()
        color = self.get_color()
        style = {
            "fill_color": color,
            "stroke_color": color
        }
        style.update(self.tip_style)
        tip = ArrowTip(length=tip_length, **style)
        return tip

    def position_tip(self, tip, at_start=False):
        # Last two control points, defining both
        # the end, and the tangency direction
        if at_start:
            anchor = self.get_start()
            handle = self.get_first_handle()
        else:
            handle = self.get_last_handle()
            anchor = self.get_end()
        tip.rotate(
            angle_of_vector(handle - anchor) -
            PI - tip.get_angle()
        )
        tip.shift(anchor - tip.get_tip_point())
        return tip

    def reset_endpoints_based_on_tip(self, tip, at_start):
        if self.get_length() == 0:
            # Zero length, put_start_and_end_on wouldn't
            # work
            return self

        if at_start:
            self.put_start_and_end_on(
                tip.get_base(), self.get_end()
            )
        else:
            self.put_start_and_end_on(
                self.get_start(), tip.get_base(),
            )
        return self

    def asign_tip_attr(self, tip, at_start):
        if at_start:
            self.start_tip = tip
        else:
            self.tip = tip
        return self

    # Checking for tips

    def has_tip(self):
        return hasattr(self, "tip") and self.tip in self

    def has_start_tip(self):
        return hasattr(self, "start_tip") and self.start_tip in self


    # Getters

    def pop_tips(self):
        """删除并返回 ``tips``"""
        start, end = self.get_start_and_end()
        result = VGroup()
        if self.has_tip():
            result.add(self.tip)
            self.remove(self.tip)
        if self.has_start_tip():
            result.add(self.start_tip)
            self.remove(self.start_tip)
        self.put_start_and_end_on(start, end)
        return result

    def get_tips(self):
        """返回一个包含首尾tips的VGroup，没有则为空"""
        result = VGroup()
        if hasattr(self, "tip"):
            result.add(self.tip)
        if hasattr(self, "start_tip"):
            result.add(self.start_tip)
        return result

    def get_tip(self):
        """返回第一个tip，如果没有则抛出异常"""
        tips = self.get_tips()
        if len(tips) == 0:
            raise Exception("tip not found")
        else:
            return tips[0]

    def get_default_tip_length(self):
        return self.tip_length

    def get_first_handle(self):
        return self.points[1]

    def get_last_handle(self):
        return self.points[-2]

    def get_end(self):
        if self.has_tip():
            return self.tip.get_start()
        else:
            return VMobject.get_end(self)

    def get_start(self):
        if self.has_start_tip():
            return self.start_tip.get_start()
        else:
            return VMobject.get_start(self)

    def get_length(self):
        start, end = self.get_start_and_end()
        return get_norm(start - end)


class Arc(TipableVMobject):
    """圆弧"""
    CONFIG = {
        "radius": 1.0,
        "num_components": 9,
        "anchors_span_full_range": True,
        "arc_center": ORIGIN,
    }

    def __init__(self, start_angle=0, angle=TAU / 4, **kwargs):
        """传入 ``start_angle`` 表示起始的角度， ``angle`` 表示圆心角
        
        - ``radius`` : 圆弧半径
        - ``num_components`` : 数越大越精细
        - ``arc_center`` : 圆弧的中心
        """
        self.start_angle = start_angle
        self.angle = angle
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        self.set_pre_positioned_points()
        self.scale(self.radius, about_point=ORIGIN)
        self.shift(self.arc_center)

    def set_pre_positioned_points(self):
        anchors = np.array([
            np.cos(a) * RIGHT + np.sin(a) * UP
            for a in np.linspace(
                self.start_angle,
                self.start_angle + self.angle,
                self.num_components,
            )
        ])
        # Figure out which control points will give the
        # Appropriate tangent lines to the circle
        d_theta = self.angle / (self.num_components - 1.0)
        tangent_vectors = np.zeros(anchors.shape)
        # Rotate all 90 degress, via (x, y) -> (-y, x)
        tangent_vectors[:, 1] = anchors[:, 0]
        tangent_vectors[:, 0] = -anchors[:, 1]
        # Use tangent vectors to deduce anchors
        handles1 = anchors[:-1] + (d_theta / 3) * tangent_vectors[:-1]
        handles2 = anchors[1:] - (d_theta / 3) * tangent_vectors[1:]
        self.set_anchors_and_handles(
            anchors[:-1],
            handles1, handles2,
            anchors[1:],
        )

    def get_arc_center(self):
        """获取圆弧圆心"""
        # First two anchors and handles
        a1, h1, h2, a2 = self.points[:4]
        # Tangent vectors
        t1 = h1 - a1
        t2 = h2 - a2
        # Normals
        n1 = rotate_vector(t1, TAU / 4)
        n2 = rotate_vector(t2, TAU / 4)
        try:
            return line_intersection(
                line1=(a1, a1 + n1),
                line2=(a2, a2 + n2),
            )
        except Exception:
            warnings.warn("Can't find Arc center, using ORIGIN instead")
            return np.array(ORIGIN)

    def move_arc_center_to(self, point):
        """将圆弧圆心移动到 ``point`` 的位置"""
        self.shift(point - self.get_arc_center())
        return self

    def stop_angle(self):
        return angle_of_vector(
            self.points[-1] - self.get_arc_center()
        ) % TAU


class ArcBetweenPoints(Arc):
    """在两点之间的圆弧"""
    def __init__(self, start, end, angle=TAU / 4, **kwargs):
        """传入 ``start, end`` 表示起点终点，``angle`` 表示圆心角
        
        其余关键字参数同 ``Arc``
        """
        Arc.__init__(
            self,
            angle=angle,
            **kwargs,
        )
        if angle == 0:
            self.set_points_as_corners([LEFT, RIGHT])
        self.put_start_and_end_on(start, end)


class CurvedArrow(ArcBetweenPoints):
    """弯曲的单向箭头"""
    def __init__(self, start_point, end_point, **kwargs):
        """从 ``start_point`` 到 ``end_point`` 的弯曲箭头，圆心角为90°
        
        其余关键字参数同 ``Arc``
        """
        ArcBetweenPoints.__init__(self, start_point, end_point, **kwargs)
        self.add_tip()


class CurvedDoubleArrow(CurvedArrow):
    """弯曲的双向箭头"""
    def __init__(self, start_point, end_point, **kwargs):
        """从 ``start_point`` 到 ``end_point`` 的弯曲双向箭头，圆心角为90°
        
        其余关键字参数同 ``Arc``
        """
        CurvedArrow.__init__(
            self, start_point, end_point, **kwargs
        )
        self.add_tip(at_start=True)


class Circle(Arc):
    """圆"""
    CONFIG = {
        "color": RED,
        "close_new_points": True,
        "anchors_span_full_range": False
    }

    def __init__(self, **kwargs):
        """参数同 ``Arc`` ，半径使用 ``radius`` (来自 ``Arc`` )"""
        Arc.__init__(self, 0, TAU, **kwargs)

    def surround(self, mobject, dim_to_match=0, stretch=False, buffer_factor=1.2):
        """让圆环绕住物体（dim_to_match和stretch无效，始终为圆）"""
        # Ignores dim_to_match and stretch; result will always be a circle
        # TODO: Perhaps create an ellipse class to handle singele-dimension stretching

        # Something goes wrong here when surrounding lines?
        # TODO: Figure out and fix
        self.replace(mobject, dim_to_match, stretch)

        self.set_width(
            np.sqrt(mobject.get_width()**2 + mobject.get_height()**2)
        )
        self.scale(buffer_factor)

    def point_at_angle(self, angle):
        """返回圆上距离起点（默认在x轴）角度为 ``angle`` 的点"""
        if angle >= TAU:
            angle %= TAU
        start_angle = angle_of_vector(
            self.points[0] - self.get_center()
        )
        return self.point_from_proportion(
            (angle - start_angle) / TAU
        )


class Dot(Circle):
    """点（半径默认为0.08）"""
    CONFIG = {
        "radius": DEFAULT_DOT_RADIUS,
        "stroke_width": 0,
        "fill_opacity": 1.0,
        "color": WHITE
    }

    def __init__(self, point=ORIGIN, **kwargs):
        """传入参数 ``point`` 表示点的位置，其余同 ``Arc``"""
        Circle.__init__(self, arc_center=point, **kwargs)


class SmallDot(Dot):
    """小点（半径默认为0.04）"""
    CONFIG = {
        "radius": DEFAULT_SMALL_DOT_RADIUS,
    }


class Ellipse(Circle):
    """椭圆"""
    CONFIG = {
        "width": 2,
        "height": 1
    }

    def __init__(self, **kwargs):
        """宽度为 ``width``，高度为 ``height``"""
        Circle.__init__(self, **kwargs)
        self.set_width(self.width, stretch=True)
        self.set_height(self.height, stretch=True)


class AnnularSector(Arc):
    """扇环
    
    - ``inner_radius`` : 内圆半径
    - ``outer_radius`` : 外圆半径
    - 其余同 ``Arc``
    """
    CONFIG = {
        "inner_radius": 1,
        "outer_radius": 2,
        "angle": TAU / 4,
        "start_angle": 0,
        "fill_opacity": 1,
        "stroke_width": 0,
        "color": WHITE,
    }

    def generate_points(self):
        inner_arc, outer_arc = [
            Arc(
                start_angle=self.start_angle,
                angle=self.angle,
                radius=radius,
                arc_center=self.arc_center,
            )
            for radius in (self.inner_radius, self.outer_radius)
        ]
        outer_arc.reverse_points()
        self.append_points(inner_arc.points)
        self.add_line_to(outer_arc.points[0])
        self.append_points(outer_arc.points)
        self.add_line_to(inner_arc.points[0])


class Sector(AnnularSector):
    """扇形
    
    即内圆半径为0的扇环
    """
    CONFIG = {
        "outer_radius": 1,
        "inner_radius": 0
    }


class Annulus(Circle):
    """圆环
    
    - ``inner_radius`` : 内圆半径
    - ``outer_radius`` : 外圆半径
    - 其余同 ``Circle`` （ ``Arc`` ）
    """
    CONFIG = {
        "inner_radius": 1,
        "outer_radius": 2,
        "fill_opacity": 1,
        "stroke_width": 0,
        "color": WHITE,
        "mark_paths_closed": False,
    }

    def generate_points(self):
        self.radius = self.outer_radius
        outer_circle = Circle(radius=self.outer_radius)
        inner_circle = Circle(radius=self.inner_radius)
        inner_circle.reverse_points()
        self.append_points(outer_circle.points)
        self.append_points(inner_circle.points)
        self.shift(self.arc_center)


class Line(TipableVMobject):
    """直线"""
    CONFIG = {
        "buff": 0,
        "path_arc": None,  # angle of arc specified here
    }

    def __init__(self, start=LEFT, end=RIGHT, **kwargs):
        """传入 ``start, end`` 为线段起点终点
        
        - ``buff`` : 为两端距离 ``start,end`` 的距离（默认为0）
        - ``path_arc`` : 如果有此关键字参数，则使用 ``ArcBetweemPoints``，``path_arc`` 表示角度
        """
        digest_config(self, kwargs)
        self.set_start_and_end_attrs(start, end)
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        if self.path_arc:
            arc = ArcBetweenPoints(
                self.start, self.end,
                angle=self.path_arc
            )
            self.set_points(arc.points)
        else:
            self.set_points_as_corners([self.start, self.end])
        self.account_for_buff()

    def set_path_arc(self, new_value):
        """设置 ``path_arc``"""
        self.path_arc = new_value
        self.generate_points()

    def account_for_buff(self):
        if self.buff == 0:
            return
        #
        if self.path_arc == 0:
            length = self.get_length()
        else:
            length = self.get_arc_length()
        #
        if length < 2 * self.buff:
            return
        buff_proportion = self.buff / length
        self.pointwise_become_partial(
            self, buff_proportion, 1 - buff_proportion
        )
        return self

    def set_start_and_end_attrs(self, start, end):
        # If either start or end are Mobjects, this
        # gives their centers
        rough_start = self.pointify(start)
        rough_end = self.pointify(end)
        vect = normalize(rough_end - rough_start)
        # Now that we know the direction between them,
        # we can the appropriate boundary point from
        # start and end, if they're mobjects
        self.start = self.pointify(start, vect)
        self.end = self.pointify(end, -vect)

    def pointify(self, mob_or_point, direction=None):
        if isinstance(mob_or_point, Mobject):
            mob = mob_or_point
            if direction is None:
                return mob.get_center()
            else:
                return mob.get_boundary_point(direction)
        return np.array(mob_or_point)

    def put_start_and_end_on(self, start, end):
        """把直线的首尾放在 ``start, end`` 上"""
        curr_start, curr_end = self.get_start_and_end()
        if np.all(curr_start == curr_end):
            # TODO, any problems with resetting
            # these attrs?
            self.start = start
            self.end = end
            self.generate_points()
        return super().put_start_and_end_on(start, end)

    def get_vector(self):
        """获取直线的方向向量"""
        return self.get_end() - self.get_start()

    def get_unit_vector(self):
        """获取直线方向上的单位向量"""
        return normalize(self.get_vector())

    def get_angle(self):
        """获取直线倾斜角"""
        return angle_of_vector(self.get_vector())

    def get_slope(self):
        """获取直线斜率"""
        return np.tan(self.get_angle())

    def set_angle(self, angle):
        """设置直线倾斜角为 ``angle``"""
        self.rotate(
            angle - self.get_angle(),
            about_point=self.get_start(),
        )

    def set_length(self, length):
        """缩放到 ``length`` 长度"""
        self.scale(length / self.get_length())

    def set_opacity(self, opacity, family=True):
        # Overwrite default, which would set
        # the fill opacity
        self.set_stroke(opacity=opacity)
        if family:
            for sm in self.submobjects:
                sm.set_opacity(opacity, family)
        return self


class DashedLine(Line):
    """虚线"""
    CONFIG = {
        "dash_length": DEFAULT_DASH_LENGTH,
        "dash_spacing": None,
        "positive_space_ratio": 0.5,
    }

    def __init__(self, *args, **kwargs):
        """使用 ``DashedVMobject``
        
        - ``dash_length`` : 每段虚线的长度，默认为0.05
        """
        Line.__init__(self, *args, **kwargs)
        ps_ratio = self.positive_space_ratio
        num_dashes = self.calculate_num_dashes(ps_ratio)
        dashes = DashedVMobject(
            self,
            num_dashes=num_dashes,
            positive_space_ratio=ps_ratio
        )
        self.clear_points()
        self.add(*dashes)

    def calculate_num_dashes(self, positive_space_ratio):
        try:
            full_length = self.dash_length / positive_space_ratio
            return int(np.ceil(
                self.get_length() / full_length
            ))
        except ZeroDivisionError:
            return 1

    def calculate_positive_space_ratio(self):
        return fdiv(
            self.dash_length,
            self.dash_length + self.dash_spacing,
        )

    def get_start(self):
        if len(self.submobjects) > 0:
            return self.submobjects[0].get_start()
        else:
            return Line.get_start(self)

    def get_end(self):
        if len(self.submobjects) > 0:
            return self.submobjects[-1].get_end()
        else:
            return Line.get_end(self)

    def get_first_handle(self):
        return self.submobjects[0].points[1]

    def get_last_handle(self):
        return self.submobjects[-1].points[-2]


class TangentLine(Line):
    """切线"""
    CONFIG = {
        "length": 1,
        "d_alpha": 1e-6
    }

    def __init__(self, vmob, alpha, **kwargs):
        """传入 ``vmob`` 表示需要做切线的物体，``alpha`` 表示切点在 ``vmob`` 上的比例
        
        - ``length`` : 切线长度
        - ``d_alpha`` : 精细程度，越小越精细（默认1e-6）
        """
        digest_config(self, kwargs)
        da = self.d_alpha
        a1 = np.clip(alpha - da, 0, 1)
        a2 = np.clip(alpha + da, 0, 1)
        super().__init__(
            vmob.point_from_proportion(a1),
            vmob.point_from_proportion(a2),
            **kwargs
        )
        self.scale(self.length / self.get_length())


class Elbow(VMobject):
    """折线（一般用作直角符号）"""
    CONFIG = {
        "width": 0.2,
        "angle": 0,
    }

    def __init__(self, **kwargs):
        """``width`` 表示宽度，``angle`` 表示角度"""
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners([UP, UP + RIGHT, RIGHT])
        self.set_width(self.width, about_point=ORIGIN)
        self.rotate(self.angle, about_point=ORIGIN)


class Arrow(Line):
    """箭头"""
    CONFIG = {
        "stroke_width": 6,
        "buff": MED_SMALL_BUFF,
        "max_tip_length_to_length_ratio": 0.25,
        "max_stroke_width_to_length_ratio": 5,
        "preserve_tip_size_when_scaling": True,
    }

    def __init__(self, *args, **kwargs):
        """和 ``Line`` 相同，箭头大小自动
        
        - ``buff`` : 默认为0.25
        - ``max_tip_length_to_length_ratio`` : 箭头长度和直线长度最大比例（默认0.25）
        - ``max_stroke_width_to_length_ratio`` : 线条粗细和直线长度最大比例（默认5）
        """
        Line.__init__(self, *args, **kwargs)
        # TODO, should this be affected when
        # Arrow.set_stroke is called?
        self.initial_stroke_width = self.stroke_width
        self.add_tip()
        self.set_stroke_width_from_length()

    def scale(self, factor, **kwargs):
        """缩放箭头，自动调节箭头大小和线条宽度"""
        if self.get_length() == 0:
            return self

        has_tip = self.has_tip()
        has_start_tip = self.has_start_tip()
        if has_tip or has_start_tip:
            old_tips = self.pop_tips()

        VMobject.scale(self, factor, **kwargs)
        self.set_stroke_width_from_length()

        # So horribly confusing, must redo
        if has_tip:
            self.add_tip()
            old_tips[0].points[:, :] = self.tip.points
            self.remove(self.tip)
            self.tip = old_tips[0]
            self.add(self.tip)
        if has_start_tip:
            self.add_tip(at_start=True)
            old_tips[1].points[:, :] = self.start_tip.points
            self.remove(self.start_tip)
            self.start_tip = old_tips[1]
            self.add(self.start_tip)
        return self

    def get_normal_vector(self):
        p0, p1, p2 = self.tip.get_start_anchors()[:3]
        return normalize(np.cross(p2 - p1, p1 - p0))

    def reset_normal_vector(self):
        self.normal_vector = self.get_normal_vector()
        return self

    def get_default_tip_length(self):
        max_ratio = self.max_tip_length_to_length_ratio
        return min(
            self.tip_length,
            max_ratio * self.get_length(),
        )

    def set_stroke_width_from_length(self):
        max_ratio = self.max_stroke_width_to_length_ratio
        self.set_stroke(
            width=min(
                self.initial_stroke_width,
                max_ratio * self.get_length(),
            ),
            family=False,
        )
        return self

    # TODO, should this be the default for everything?
    def copy(self):
        return self.deepcopy()


class Vector(Arrow):
    """向量"""
    CONFIG = {
        "buff": 0,
    }

    def __init__(self, direction=RIGHT, **kwargs):
        """即起点为ORIGIN的箭头，终点为 ``direction``
        
        - ``buff`` 默认设为了0
        """
        if len(direction) == 2:
            direction = np.append(np.array(direction), 0)
        Arrow.__init__(self, ORIGIN, direction, **kwargs)


class DoubleArrow(Arrow):
    """双向直箭头"""
    def __init__(self, *args, **kwargs):
        """参数和 ``Arrow`` 一致"""
        Arrow.__init__(self, *args, **kwargs)
        self.add_tip(at_start=True)


class CubicBezier(VMobject):
    """三阶贝塞尔曲线"""
    def __init__(self, points, **kwargs):
        """传入 ``points`` 表示构成贝塞尔曲线的点集"""
        VMobject.__init__(self, **kwargs)
        self.set_points(points)


class Polygon(VMobject):
    """多边形"""
    CONFIG = {
        "color": BLUE,
    }

    def __init__(self, *vertices, **kwargs):
        """传入多个 ``vertices`` (点坐标)表示顶点"""
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(
            [*vertices, vertices[0]]
        )

    def get_vertices(self):
        """获取所有顶点"""
        return self.get_start_anchors()

    def round_corners(self, radius=0.5):
        """形成圆角（圆角半径为 ``radius``）"""
        vertices = self.get_vertices()
        arcs = []
        for v1, v2, v3 in adjacent_n_tuples(vertices, 3):
            vect1 = v2 - v1
            vect2 = v3 - v2
            unit_vect1 = normalize(vect1)
            unit_vect2 = normalize(vect2)
            angle = angle_between_vectors(vect1, vect2)
            # Negative radius gives concave curves
            angle *= np.sign(radius)
            # Distance between vertex and start of the arc
            cut_off_length = radius * np.tan(angle / 2)
            # Determines counterclockwise vs. clockwise
            sign = np.sign(np.cross(vect1, vect2)[2])
            arc = ArcBetweenPoints(
                v2 - unit_vect1 * cut_off_length,
                v2 + unit_vect2 * cut_off_length,
                angle=sign * angle
            )
            arcs.append(arc)

        self.clear_points()
        # To ensure that we loop through starting with last
        arcs = [arcs[-1], *arcs[:-1]]
        for arc1, arc2 in adjacent_pairs(arcs):
            self.append_points(arc1.points)
            line = Line(arc1.get_end(), arc2.get_start())
            # Make sure anchors are evenly distributed
            len_ratio = line.get_length() / arc1.get_arc_length()
            line.insert_n_curves(
                int(arc1.get_num_curves() * len_ratio)
            )
            self.append_points(line.get_points())
        return self


class RegularPolygon(Polygon):
    """正多边形"""
    CONFIG = {
        "start_angle": None,
    }

    def __init__(self, n=6, **kwargs):
        """传入数字 ``n`` 表示边数"""
        digest_config(self, kwargs, locals())
        if self.start_angle is None:
            if n % 2 == 0:
                self.start_angle = 0
            else:
                self.start_angle = 90 * DEGREES
        start_vect = rotate_vector(RIGHT, self.start_angle)
        vertices = compass_directions(n, start_vect)
        Polygon.__init__(self, *vertices, **kwargs)


class Triangle(RegularPolygon):
    """正三角形"""
    def __init__(self, **kwargs):
        """使用 ``RegularPolygon``"""
        RegularPolygon.__init__(self, n=3, **kwargs)


class ArrowTip(Triangle):
    """箭头标志"""
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 0,
        "length": DEFAULT_ARROW_TIP_LENGTH,
        "start_angle": PI,
    }

    def __init__(self, **kwargs):
        """即一个小正三角形"""
        Triangle.__init__(self, **kwargs)
        self.set_width(self.length)
        self.set_height(self.length, stretch=True)

    def get_base(self):
        return self.point_from_proportion(0.5)

    def get_tip_point(self):
        return self.points[0]

    def get_vector(self):
        return self.get_tip_point() - self.get_base()

    def get_angle(self):
        return angle_of_vector(self.get_vector())

    def get_length(self):
        return get_norm(self.get_vector())


class Rectangle(Polygon):
    """矩形"""
    CONFIG = {
        "color": WHITE,
        "height": 2.0,
        "width": 4.0,
        "mark_paths_closed": True,
        "close_new_points": True,
    }

    def __init__(self, **kwargs):
        """使用 ``Polygon``

        - ``height`` : 矩形高度
        - ``width`` : 矩形宽度
        """
        Polygon.__init__(self, UL, UR, DR, DL, **kwargs)
        self.set_width(self.width, stretch=True)
        self.set_height(self.height, stretch=True)


class Square(Rectangle):
    """正方形"""
    CONFIG = {
        "side_length": 2.0,
    }

    def __init__(self, **kwargs):
        """``side_length`` 是正方形边长"""
        digest_config(self, kwargs)
        Rectangle.__init__(
            self,
            height=self.side_length,
            width=self.side_length,
            **kwargs
        )


class RoundedRectangle(Rectangle):
    """圆角矩形"""
    CONFIG = {
        "corner_radius": 0.5,
    }

    def __init__(self, **kwargs):
        """调用了 ``round_corners`` 的 ``Rectangle``
        
        - ``corner_radius`` 为圆角半径
        """
        Rectangle.__init__(self, **kwargs)
        self.round_corners(self.corner_radius)
