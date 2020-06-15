ImageMobject
============

:class:`~mobject.types.point_cloud_mobject.AbstractImageMobject` 是
:class:`~mobject.mobject.Mobject` 的子类，可看作抽象类，用于存放 ``pixel_array``。

它有两个子类：:class:`~mobject.types.point_cloud_mobject.ImageMobject`
用于在场景中插入图片；:class:`~mobject.types.point_cloud_mobject.ImageMobjectFromCamera`
用相机不断获取图片，主要用在 :class:`~camera.multi_camera.MultiCamera`
中作为子相机

.. autoclass:: manimlib.mobject.types.image_mobject.AbstractImageMobject
    :members:

TODO：
完成文档字符串
ImageMobject需要示例
传入的filename_or_array的范围
VMobject中有两个需要示例