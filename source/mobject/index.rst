物体部分mobject
=================

.. admonition:: 声明

   这一部分全为鹤翔万里原创编写

:class:`~mobject.mobject.Mobject` 是屏幕中出现的所有物体的超类。

:class:`~mobject.mobject.Mobject` 类似为抽象基类，它的直接子类只有：

- :class:`~mobject.types.vectorized_mobject.VMobject` 使用贝塞尔曲线作为轮廓
- :class:`~mobject.types.point_cloud_mobject.PMobject` 点集构成物体
- :class:`~mobject.types.image_mobject.AbstractImageMobject` 关于图片的抽象基类
- :class:`~mobject.value_tracker.ValueTracker` 只记录数值，不在屏幕上显示


.. toctree::
   :maxdepth: 2
   :caption: 目录

   mobject
   types/index
   svg/index
