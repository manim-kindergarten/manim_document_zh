属性容器container
==================

目前 :class:`~container.Container` 只是 :class:`~scene.scene.Scene` 和
:class:`~mobject.mobject.Mobject` 的抽象基类（父类），在 ``__init__``
中实现了对CONFIG字典转化为属性的处理。

还规定了需要子类实现 ``add`` 方法和 ``remove`` 方法

Container
*********

.. autoclass:: manimlib.container.container.Container

.. automethod:: manimlib.container.container.Container.__init__

执行 ``digest_config(self, kwargs)`` 把 ``CONFIG`` 字典和 ``kwargs`` 字典
转化为类属性

.. automethod:: manimlib.container.container.Container.add

需要子类实现

.. automethod:: manimlib.container.container.Container.remove

需要子类实现
