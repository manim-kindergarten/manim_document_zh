数学物件 mobject
================

.. admonition:: 声明

   这一部分全为鹤翔万里与數心原创编写，新版由 widcardw 修订，目前示例部分还没有完成

:class:`~manimlib.mobject.mobject.Mobject` 是屏幕中出现的所有物体的超类。

:class:`~manimlib.mobject.mobject.Mobject` 类似为抽象基类，它的直接子类只有：

- :class:`~manimlib.mobject.types.vectorized_mobject.VMobject` 使用贝塞尔曲线作为轮廓
- :class:`~manimlib.mobject.types.point_cloud_mobject.PMobject` 点集构成物体
- :class:`~manimlib.mobject.types.image_mobject.ImageMobject` 图片类
- :class:`~manimlib.mobject.value_tracker.ValueTracker` 只记录数值，不在屏幕上显示


.. toctree::
   :maxdepth: 2
   :caption: 目录

   types/index
   svg/index
   changing
   coordinate_systems
   frame
   functions
   geometry
   interactive
   matrix
   mobject
   mobject_update_utils
   number_line
   numbers
   probability
   shape_matchers
   three_dimensions
   value_tracker
   vector_field