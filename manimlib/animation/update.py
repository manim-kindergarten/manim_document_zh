import operator as op

from manimlib.animation.animation import Animation


class UpdateFromFunc(Animation):
    """
    时刻使用update_function来更新mobject
    """
    CONFIG = {
        "suspend_mobject_updating": False,
    }

    def __init__(self, mobject, update_function, **kwargs):
        self.update_function = update_function
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.update_function(self.mobject)


class UpdateFromAlphaFunc(UpdateFromFunc):
    """传入的函数含有参数alpha，表示动画完成度(0~1之间)"""
    def interpolate_mobject(self, alpha):
        self.update_function(self.mobject, alpha)


class MaintainPositionRelativeTo(Animation):
    """维持mobject与tracked_mobject之间的相对位置关系"""
    def __init__(self, mobject, tracked_mobject, **kwargs):
        self.tracked_mobject = tracked_mobject
        self.diff = op.sub(
            mobject.get_center(),
            tracked_mobject.get_center(),
        )
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        target = self.tracked_mobject.get_center()
        location = self.mobject.get_center()
        self.mobject.shift(target - location + self.diff)
