camera相机参数
=====================

.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是想把Markdown、pdf等资料整合编辑成方便的文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。

camera相机参数
-------------------

相机是针对3D动画类(\ **ThreeDScene**)的方法

**\\manimlib\\scene\\threedscene.py**

将视频的视窗看做相机，就可以通过调整相机的远近，角度来观察三维物体，这就是相机类的作用


1 set\ *camera*\ orientation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**threeDScene.set\ camera\ orientation(phi=degrees1,theta=degrees2,gamma=degrees3,distance=number)**

设置相机的角度



2 move_camera
~~~~~~~~~~~~~~~~

**threeDScene.move\ camera(phi=None,theta=None, distance=None,
gamma=None, frame\ center=None,added_anims=[],\*\*kwargs)**

例子：

.. code:: python

   class MoveCamera2(ThreeDScene):
       def construct(self):
           axes = ThreeDAxes()
           circle=Circle()
           self.set_camera_orientation(phi=80 * DEGREES)           
           self.play(ShowCreation(circle),ShowCreation(axes))
           #Start move camera
           self.begin_ambient_camera_rotation(rate=0.1)            
           self.wait(5)
           #Stop move camera
           self.stop_ambient_camera_rotation()                     
           #Return the position of the camera
           self.move_camera(phi=80*DEGREES,theta=-PI/2)            
           self.wait()



3 set\ *to*\ default\ *angled*\ camera_orientation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

还原为默认角度



4 add\ *fixed*\ in\ *frame*\ mobjects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

加入固定在屏幕的图像，此图像不随相机变化而变化

**add\ fixed\ in\ frame\ mobjects(*mobjects)**

例：

.. code:: python

   class Text3D3(ThreeDScene):
       def construct(self):
           axes = ThreeDAxes()
           self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
           text3d=TextMobject("This is a 3D text")

           self.add_fixed_in_frame_mobjects(text3d) #<----- Add this
           text3d.to_corner(UL)

           self.add(axes)
           self.begin_ambient_camera_rotation()
           self.play(Write(text3d))

           sphere = ParametricSurface(
               lambda u, v: np.array([
                   1.5*np.cos(u)*np.cos(v),
                   1.5*np.cos(u)*np.sin(v),
                   1.5*np.sin(u)
               ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
               resolution=(15, 32)).scale(2)

           self.play(LaggedStart(ShowCreation,sphere))
           self.wait(2)

