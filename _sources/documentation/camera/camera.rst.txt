Camera
=============

.. admonition:: 注意

    本部分涉及到很多关于 OpenGL 的编写，例如 vertex array object, vertex buffer object, texture 等内容。由于编者对这部分也不是很熟悉，也希望有专业的同学来一起完善这部分内容。

CameraFrame
*************
.. autoclass:: manimlib.camera.camera.CameraFrame
    :members:

在 ``manimgl`` 版本，你可以通过改变 ``CameraFrame`` 的属性来控制相机所拍摄到的画面，也就是说，旋转、缩放画面大小都可以用这种方式来完成。

.. manim-example:: MoveCameraExample
    :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/MoveCameraExample.mp4

    class MoveCameraExample(Scene):
        def setup(self):
            self.plane = NumberPlane()
            self.plane.add_coordinate_labels()
            self.add(self.plane)

        def t_func(self, t):
            a, b = 3, 3
            return np.array([
                a * np.cos(t) / t,
                b * np.sin(t) / t,
                0
            ])

        def construct(self):
            frame = self.camera.frame
            curve = ParametricCurve(self.t_func, t_range=[0.1, 100, 0.05], color=YELLOW)
            self.add(curve)
            self.play(
                curve.animate.set_stroke(width=0.3),
                frame.animate.set_width(2).rotate(PI / 2),
                run_time=3
            )
            self.wait(0.5)

Camera
*************
.. autoclass:: manimlib.camera.camera.Camera
    :members:

ThreeDCamera
*************
.. autoclass:: manimlib.camera.camera.ThreeDCamera
