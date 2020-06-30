import numpy as np

from manimlib.mobject.mobject import Mobject


class ValueTracker(Mobject):
    """记录一个数值（不在画面中显示）"""

    def __init__(self, value=0, **kwargs):
        """传入的 ``value`` 为初始数值"""
        Mobject.__init__(self, **kwargs)
        self.points = np.zeros((1, 3))
        self.set_value(value)

    def get_value(self):
        """获取当前存的值"""
        return self.points[0, 0]

    def set_value(self, value):
        """将值设为 ``value``"""
        self.points[0, 0] = value
        return self

    def increment_value(self, d_value):
        """将存储的值增加 ``d_value``"""
        self.set_value(self.get_value() + d_value)


class ExponentialValueTracker(ValueTracker):
    """以指数形式变化的存值器"""

    def get_value(self):
        return np.exp(ValueTracker.get_value(self))

    def set_value(self, value):
        return ValueTracker.set_value(self, np.log(value))


class ComplexValueTracker(ValueTracker):
    """记录一个复数数值"""
    def get_value(self):
        return complex(*self.points[0, :2])

    def set_value(self, z):
        z = complex(z)
        self.points[0, :2] = (z.real, z.imag)
        return self
