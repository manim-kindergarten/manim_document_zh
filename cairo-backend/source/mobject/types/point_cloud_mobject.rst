PMobject
========

:class:`~manimlib.mobject.types.point_cloud_mobject.PMobject` 是
:class:`~manimlib.mobject.mobject.Mobject` 的子类，使用点集来表示物体，目前不太常用

PMobject
********
.. autoclass:: manimlib.mobject.types.point_cloud_mobject.PMobject
    :members:

Mobject1D
*********
.. autoclass:: manimlib.mobject.types.point_cloud_mobject.Mobject1D
    :members:

Mobject2D
*********
.. autoclass:: manimlib.mobject.types.point_cloud_mobject.Mobject2D
    :members:

PGroup
******
.. autoclass:: manimlib.mobject.types.point_cloud_mobject.PGroup
    :members:

PointCloudDot
*************
.. autoclass:: manimlib.mobject.types.point_cloud_mobject.PointCloudDot
    :members:

.. TODO: 添加示例

Point
*****
.. autoclass:: manimlib.mobject.types.point_cloud_mobject.Point
    :members:

.. TODO: 添加示例

但是不推荐使用 :class:`~manimlib.mobject.types.point_cloud_mobject.PointCloudDot`
或 :class:`~manimlib.mobject.types.point_cloud_mobject.Point` 来表示点，
这样会因为属于 :class:`~manimlib.mobject.types.point_cloud_mobject.PMobject`
而非 :class:`~manimlib.mobject.types.vectorized_mobject.VMobject` 而产生很多问题。

一般来表示点，通常使用 :class:`~manimlib.mobject.geometry.Dot` 来完成
