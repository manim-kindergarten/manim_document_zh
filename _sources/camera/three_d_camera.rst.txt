ThreeDCamera
============

``ThreeDCamera`` 是一个3D相机类，只通过给3D物体施加 ``rotation_matrix`` 来
将3D物体转为2D，因此，manim的3D效果不是很好，很多问题不宜解决（例如穿模）。
在 :class:`~manimlib.scene.three_d_scene.ThreeDScene` 和 
:class:`~manimlib.scene.three_d_scene.SpecialThreeDScene` 中被默认使用。

ThreeDCamera
************

.. autoclass:: manimlib.camera.three_d_camera.ThreeDCamera
    :members:
