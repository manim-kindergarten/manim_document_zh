from manimlib.constants import *
from manimlib.mobject.svg.tex_mobject import SingleStringTexMobject
from manimlib.mobject.types.vectorized_mobject import VMobject


class DecimalNumber(VMobject):
    """十进制数字（比直接使用TexMobject方便，支持复数）"""
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
    }

    def __init__(self, number=0, **kwargs):
        """传入 ``number`` 表示初始的数值
        
        - ``num_decimal_places`` : 小数位数
        - ``include_sign`` : 正数是否包含"+"标志（默认为False）
        - ``digit_to_digit_buff`` : 两个字符之间的距离（默认为0.05）
        - ``show_ellipsis`` : 是否显示省略号（默认为False）
        - ``unit`` : 末尾的单位
        - ``include_background_rectangle`` : 是否包含背景矩形（默认为False）
        - ``edge_to_fix`` : 在变化时，以哪边对齐（默认LEFT）
        """
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            SingleStringTexMobject(char, **kwargs)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(SingleStringTexMobject("\\dots"))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = SingleStringTexMobject(self.unit, color=self.color)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i+1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

    def get_formatter(self, **kwargs):
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        """设置新值（新建一个 ``DecimalNumber``）"""
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalNumber(number, **full_config)
        # Make sure last digit has constant height
        new_decimal.scale(
            self[-1].get_height() / new_decimal[-1].get_height()
        )
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        """获取当前数值（``DecimalNumber.number``）"""
        return self.number

    def increment_value(self, delta_t=1):
        """给值增加 ``delta_t``"""
        self.set_value(self.get_value() + delta_t)


class Integer(DecimalNumber):
    """整数（利用 ``DecimalNumber``）"""
    CONFIG = {
        "num_decimal_places": 0,
    }
    def __init__(self, number=0, **kwargs):
        """参数和 ``DecimalNumber`` 相同"""
        super().__init__(number, **kwargs)

    def get_value(self):
        """对值四舍五入后返回"""
        return int(np.round(super().get_value()))
