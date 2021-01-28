import operator as op

from manimlib.constants import *
from manimlib.mobject.geometry import Line
from manimlib.mobject.numbers import DecimalNumber
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.utils.bezier import interpolate
from manimlib.utils.config_ops import digest_config
from manimlib.utils.config_ops import merge_dicts_recursively
from manimlib.utils.simple_functions import fdiv
from manimlib.utils.space_ops import normalize


class NumberLine(Line):
    """数轴"""
    CONFIG = {
        "color": LIGHT_GREY,
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "unit_size": 1,
        "include_ticks": True,
        "tick_size": 0.1,
        "tick_frequency": 1,
        # Defaults to value near x_min s.t. 0 is a tick
        # TODO, rename this
        "leftmost_tick": None,
        # Change name
        "numbers_with_elongated_ticks": [0],
        "include_numbers": False,
        "numbers_to_show": None,
        "longer_tick_multiple": 2,
        "number_at_center": 0,
        "number_scale_val": 0.75,
        "label_direction": DOWN,
        "line_to_number_buff": MED_SMALL_BUFF,
        "include_tip": False,
        "tip_width": 0.25,
        "tip_height": 0.25,
        "decimal_number_config": {
            "num_decimal_places": 0,
            "color": BLACK
        },
        "exclude_zero_from_default_numbers": False,
    }

    def __init__(self, **kwargs):
        """全部以关键字参数的形式传入
        
        - ``x_min, x_max`` : 数轴的最大值最小值
        - ``unit_size`` : 单位长度大小
        - 刻度相关

          - ``include_ticks`` : 是否包含刻度线（bool值，默认True）
          - ``tick_size`` : 刻度大小（默认0.1）
          - ``tick_frequency`` : 刻度的频率（默认每一个单位一个刻度）
          - ``numbers_with_elongated_ticks`` : 需要大刻度的数字（一个列表，默认为[0]）

        - 数字相关

          - ``include_numbers`` : 是否包含数字（bool值，默认False）
          - ``numbers_to_show`` : 需要显示的数字
          - ``number_at_center`` : 中心的数字
          - ``label_direction`` : 数字在刻度的哪个方位（默认DOWN）
          - ``line_to_number_buff`` : 数字到线的距离
          - ``decimal_number_config`` : 字典，表示要传入给 ``DecimalNumber`` 的样式
          - ``exclude_zero_from_default_numbers`` : 是否不显示0，默认False
        
        - 箭头相关

          - ``include_tip`` : 是否包含箭头（bool值，默认False）
          - ``tip_width, tip_height`` : 箭头的宽度、高度
        """
        digest_config(self, kwargs)
        start = self.unit_size * self.x_min * RIGHT
        end = self.unit_size * self.x_max * RIGHT
        Line.__init__(self, start, end, **kwargs)
        self.shift(-self.number_to_point(self.number_at_center))

        self.init_leftmost_tick()
        if self.include_tip:
            self.add_tip()
        if self.include_ticks:
            self.add_tick_marks()
        if self.include_numbers:
            self.add_numbers()

    def init_leftmost_tick(self):
        if self.leftmost_tick is None:
            self.leftmost_tick = op.mul(
                self.tick_frequency,
                np.ceil(self.x_min / self.tick_frequency)
            )

    def add_tick_marks(self):
        tick_size = self.tick_size
        self.tick_marks = VGroup(*[
            self.get_tick(x, tick_size)
            for x in self.get_tick_numbers()
        ])
        big_tick_size = tick_size * self.longer_tick_multiple
        self.big_tick_marks = VGroup(*[
            self.get_tick(x, big_tick_size)
            for x in self.numbers_with_elongated_ticks
        ])
        self.add(
            self.tick_marks,
            self.big_tick_marks,
        )

    def get_tick(self, x, size=None):
        if size is None:
            size = self.tick_size
        result = Line(size * DOWN, size * UP)
        result.rotate(self.get_angle())
        result.move_to(self.number_to_point(x))
        result.match_style(self)
        return result

    def get_tick_marks(self):
        return VGroup(
            *self.tick_marks,
            *self.big_tick_marks,
        )

    def get_tick_numbers(self):
        u = -1 if self.include_tip else 1
        return np.arange(
            self.leftmost_tick,
            self.x_max + u * self.tick_frequency / 2,
            self.tick_frequency
        )

    def number_to_point(self, number):
        """将在数轴上的数字转化为在屏幕上的点坐标"""
        alpha = float(number - self.x_min) / (self.x_max - self.x_min)
        return interpolate(
            self.get_start(), self.get_end(), alpha
        )

    def point_to_number(self, point):
        """将在屏幕上的点坐标转化为在数轴上的数字"""
        start_point, end_point = self.get_start_and_end()
        full_vect = end_point - start_point
        unit_vect = normalize(full_vect)

        def distance_from_start(p):
            return np.dot(p - start_point, unit_vect)

        proportion = fdiv(
            distance_from_start(point),
            distance_from_start(end_point)
        )
        return interpolate(self.x_min, self.x_max, proportion)

    def n2p(self, number):
        """``number_to_point`` 的简写"""
        return self.number_to_point(number)

    def p2n(self, point):
        """``point_to_number`` 的简写"""
        return self.point_to_number(point)

    def get_unit_size(self):
        return (self.x_max - self.x_min) / self.get_length()

    def default_numbers_to_display(self):
        if self.numbers_to_show is not None:
            return self.numbers_to_show
        numbers = np.arange(
            np.floor(self.leftmost_tick),
            np.ceil(self.x_max),
        )
        if self.exclude_zero_from_default_numbers:
            numbers = numbers[numbers != 0]
        return numbers

    def get_number_mobject(self, number,
                           number_config=None,
                           scale_val=None,
                           direction=None,
                           buff=None):
        """根据传入的 ``number`` 获取需要显示的数字物体"""
        number_config = merge_dicts_recursively(
            self.decimal_number_config,
            number_config or {},
        )
        if scale_val is None:
            scale_val = self.number_scale_val
        if direction is None:
            direction = self.label_direction
        buff = buff or self.line_to_number_buff

        num_mob = DecimalNumber(number, **number_config)
        num_mob.scale(scale_val)
        num_mob.next_to(
            self.number_to_point(number),
            direction=direction,
            buff=buff
        )
        return num_mob

    def get_number_mobjects(self, *numbers, **kwargs):
        """根据传入的 ``number`` 数组获取需要显示的数字物体"""
        if len(numbers) == 0:
            numbers = self.default_numbers_to_display()
        return VGroup(*[
            self.get_number_mobject(number, **kwargs)
            for number in numbers
        ])

    def get_labels(self):
        return self.get_number_mobjects()

    def add_numbers(self, *numbers, **kwargs):
        self.numbers = self.get_number_mobjects(
            *numbers, **kwargs
        )
        self.add(self.numbers)
        return self


class UnitInterval(NumberLine):
    CONFIG = {
        "x_min": 0,
        "x_max": 1,
        "unit_size": 6,
        "tick_frequency": 0.1,
        "numbers_with_elongated_ticks": [0, 1],
        "number_at_center": 0.5,
        "decimal_number_config": {
            "num_decimal_places": 1,
        }
    }
    def __init__(self, **kwargs):
        """0到1的区间（单位长度默认为6）"""
        super().__init__(**kwargs)
