3D graphics三维图形类
======================

.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是想把Markdown、pdf等资料整合编辑成方便的文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。



三维图形类
-------------

**\\manimlib\mobject\three_dimensions.py**


1 球 Sphere
~~~~~~~~~~~~~

继承自ParametricSurface,实现通过绘制三维多边形曲面实现的，具体看源码

.. code:: python

   CONFIG = {
           "resolution": (12, 24),
           "radius": 1,
           "u_min": 0.001,
           "u_max": PI - 0.001,
           "v_min": 0,
           "v_max": TAU,
       }



2 立方 Cube
~~~~~~~~~~~~~

.. code:: python

   CONFIG = {
           "fill_opacity": 0.75,
           "fill_color": BLUE,
           "stroke_width": 0,
           "side_length": 2,
       }



3 棱柱Prism
~~~~~~~~~~~~~

继承自cube

.. code:: python

   CONFIG = {
           "dimensions": [3, 2, 1]
       }



4 参数曲面 ParametricSurface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

参数方程表达的曲面

**ParametricSurface(func, \*\*kwargs)**

.. code:: python

    CONFIG = {
           "u_min": 0,
           "u_max": 1,
           "v_min": 0,
           "v_max": 1,
           "resolution": 32,
           "surface_piece_config": {},
           "fill_color": BLUE_D,
           "fill_opacity": 1.0,
           "checkerboard_colors": [BLUE_D, BLUE_E],
           "stroke_color": LIGHT_GREY,
           "stroke_width": 0.5,
           "should_make_jagged": False,
           "pre_function_handle_to_anchor_scale_factor": 0.00001,
       }

func:自定义的方程，此方程传入两个参数，返回三维向量，每一个分量均是传入两个自变量的表达式

如：

.. code:: python

   def func(x, y):
       return np.array([x**2,y+2,x**2 - y**2])

绘制三维曲面的例子：

.. code:: python

   class SurfacesAnimation(ThreeDScene):
       def construct(self):
           axes = ThreeDAxes()
           cylinder = ParametricSurface(
               lambda u, v: np.array([
                   np.cos(TAU * v),
                   np.sin(TAU * v),
                   2 * (1 - u)
               ]),
               resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

           paraboloid = ParametricSurface(
               lambda u, v: np.array([
                   np.cos(v)*u,
                   np.sin(v)*u,
                   u**2
               ]),v_max=TAU,
               checkerboard_colors=[PURPLE_D, PURPLE_E],
               resolution=(10, 32)).scale(2)

           para_hyp = ParametricSurface(
               lambda u, v: np.array([
                   u,
                   v,
                   u**2-v**2
               ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
               resolution=(15, 32)).scale(1)

           cone = ParametricSurface(
               lambda u, v: np.array([
                   u*np.cos(v),
                   u*np.sin(v),
                   u
               ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
               resolution=(15, 32)).scale(1)

           hip_one_side = ParametricSurface(
               lambda u, v: np.array([
                   np.cosh(u)*np.cos(v),
                   np.cosh(u)*np.sin(v),
                   np.sinh(u)
               ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
               resolution=(15, 32))

           ellipsoid=ParametricSurface(
               lambda u, v: np.array([
                   1*np.cos(u)*np.cos(v),
                   2*np.cos(u)*np.sin(v),
                   0.5*np.sin(u)
               ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
               resolution=(15, 32)).scale(2)

           sphere = ParametricSurface(
               lambda u, v: np.array([
                   1.5*np.cos(u)*np.cos(v),
                   1.5*np.cos(u)*np.sin(v),
                   1.5*np.sin(u)
               ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
               resolution=(15, 32)).scale(2)


           self.set_camera_orientation(phi=75 * DEGREES)
           self.begin_ambient_camera_rotation(rate=0.2)


           self.add(axes)
           self.play(Write(sphere))
           self.wait()
           self.play(ReplacementTransform(sphere,ellipsoid))
           self.wait()
           self.play(ReplacementTransform(ellipsoid,cone))
           self.wait()
           self.play(ReplacementTransform(cone,hip_one_side))
           self.wait()
           self.play(ReplacementTransform(hip_one_side,para_hyp))
           self.wait()
           self.play(ReplacementTransform(para_hyp,paraboloid))
           self.wait()
           self.play(ReplacementTransform(paraboloid,cylinder))
           self.wait()
           self.play(FadeOut(cylinder))



5 参数曲线 ParametricFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**ParametricSurface(func, \*\*kwargs)**

func:自定义的方程，此方程传入一个参数，返回三维向量，每一个分量均是传入自变量的表达式

.. code:: python

   CONFIG = {
           "t_min": 0,
           "t_max": 1,
           "step_size": 0.01,  # Use "auto" (lowercase) for automatic step size
           "dt": 1e-8,
           # TODO, be smarter about figuring these out?
           "discontinuities": [],
       }

例：

.. code:: python

   class ParametricCurve2(ThreeDScene):
       def construct(self):
           curve1=ParametricFunction(
                   lambda u : np.array([
                   1.2*np.cos(u),
                   1.2*np.sin(u),
                   u/2
               ]),color=RED,t_min=-TAU,t_max=TAU,
               )
           curve2=ParametricFunction(
                   lambda u : np.array([
                   1.2*np.cos(u),
                   1.2*np.sin(u),
                   u
               ]),color=RED,t_min=-TAU,t_max=TAU,
               )

           curve1.set_shade_in_3d(True)
           curve2.set_shade_in_3d(True)

           axes = ThreeDAxes()

           self.add(axes)

           self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
           self.begin_ambient_camera_rotation(rate=0.1) 
           self.play(ShowCreation(curve1))
           self.wait()
           self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
           self.wait()

