import inspect
import numpy as np

from manimlib.constants import DEGREES
from manimlib.constants import RIGHT
from manimlib.mobject.mobject import Mobject


def assert_is_mobject_method(method):
    """判断 ``method`` 是否是Mobject的方法"""
    assert(inspect.ismethod(method))
    mobject = method.__self__
    assert(isinstance(mobject, Mobject))


def always(method, *args, **kwargs):
    """一直调用 ``method``，传入 ``*args, **kwargs``"""
    assert_is_mobject_method(method)
    mobject = method.__self__
    func = method.__func__
    mobject.add_updater(lambda m: func(m, *args, **kwargs))
    return mobject


def f_always(method, *arg_generators, **kwargs):
    """与 ``always`` 类似，但是传入的多个 ``arg_generators`` 是可调用对象，用于生成参数"""
    assert_is_mobject_method(method)
    mobject = method.__self__
    func = method.__func__

    def updater(mob):
        args = [
            arg_generator()
            for arg_generator in arg_generators
        ]
        func(mob, *args, **kwargs)

    mobject.add_updater(updater)
    return mobject


def always_redraw(func):
    """始终重复调用 ``func`` 生成新物体"""
    mob = func()
    mob.add_updater(lambda m: mob.become(func()))
    return mob


def always_shift(mobject, direction=RIGHT, rate=0.1):
    """将 ``mobject`` 始终向 ``direction`` 方向移动，速度为 ``rate``"""
    mobject.add_updater(
        lambda m, dt: m.shift(dt * rate * direction)
    )
    return mobject


def always_rotate(mobject, rate=20 * DEGREES, **kwargs):
    """将 ``mobject`` 始终旋转"""
    mobject.add_updater(
        lambda m, dt: m.rotate(dt * rate, **kwargs)
    )
    return mobject


def turn_animation_into_updater(animation, cycle=False, **kwargs):
    """将 ``animation`` 转化为对执行动画对象的updater
    
    - ``cycle`` 为True时循环执行，否则只执行一次
    """
    mobject = animation.mobject
    animation.update_config(**kwargs)
    animation.suspend_mobject_updating = False
    animation.begin()
    animation.total_time = 0

    def update(m, dt):
        run_time = animation.get_run_time()
        time_ratio = animation.total_time / run_time
        if cycle:
            alpha = time_ratio % 1
        else:
            alpha = np.clip(time_ratio, 0, 1)
            if alpha >= 1:
                animation.finish()
                m.remove_updater(update)
                return
        animation.interpolate(alpha)
        animation.update_mobjects(dt)
        animation.total_time += dt

    mobject.add_updater(update)
    return mobject


def cycle_animation(animation, **kwargs):
    """循环执行 ``animation``"""
    return turn_animation_into_updater(
        animation, cycle=True, **kwargs
    )
