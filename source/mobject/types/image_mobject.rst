ImageMobject
============

:class:`~manimlib.mobject.types.point_cloud_mobject.AbstractImageMobject` 是
:class:`~manimlib.mobject.mobject.Mobject` 的子类，可看作抽象类，用于存放 ``pixel_array``。

它有两个子类：:class:`~manimlib.mobject.types.point_cloud_mobject.ImageMobject`
用于在场景中插入图片；:class:`~manimlib.mobject.types.point_cloud_mobject.ImageMobjectFromCamera`
用相机不断获取图片，主要用在 :class:`~manimlib.camera.multi_camera.MultiCamera`
中作为子相机

MK做了一个关于常用 :class:`~manimlib.mobject.types.image_mobject.ImageMobject` 的的视频：
`〔manim教程〕第四讲 SVG、图片与文字  <https://www.bilibili.com/video/BV1CC4y1H7kp>`__

AbstractImageMobject
********************
.. autoclass:: manimlib.mobject.types.image_mobject.AbstractImageMobject
    :members:

ImageMobject
************
.. autoclass:: manimlib.mobject.types.image_mobject.ImageMobject
    :members:

.. TODO: 添加示例

**关于传入的图片**：

- 使用相对于运行位置的相对路径，或使用绝对路径，或把图片放在 ``assets/raster_images`` 文件夹中
- 可以是 ``jpg/png/gif`` ，但 ``gif`` 格式不会添加动图，只会显示第一帧
- 可以直接传入 ``pixel_array`` 数组，内容是rgba模式表示的每个像素颜色。可以利用这个达到像素级处理


ImageMobjectFromCamera
**********************
.. autoclass:: manimlib.mobject.types.image_mobject.ImageMobjectFromCamera
    :members:

.. TODO: 添加示例
