Making a Scene
===================

.. admonition:: 声明

        这一页是EulerTour写的教程,我只是翻译+学习笔记，github早就有很多教程，但是为了方便查询使用，我才整合这么一份文档。

A scene is what renders when manim is executed.一个python文件中scene类渲染出一个视频。 Each scene contains mobjects, which can then be animated as
previously explained. In code, a scene is a class that extends继承 ``Scene`` 类and implements执行 the ``construct`` 
function函数, like so. Manim will execute this function to render the scene.

.. code-block:: python
   :linenos:

   from manimlib.imports import *

   class ExampleScene(Scene):
       def construct(self):
           # Add and animate mobjects here

上述是一个 ``Scene`` 类的定义，对比 example_scenes.py 的 ``SquareToCircle`` 就能看懂。


.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是把他们的Markdown想整合编辑成文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。

基础动画类 Scene 
--------------------

所有的动画均是scene类的子类产生的，因此scene的功能比较少，主要是对一些基础的属性进行配置

**\\manimlib\\scene\\scene.py**

变量的值得初始定义见下：

.. code:: python

   # \manimlib\scene\scene.py
   CONFIG = {
           "camera_class": Camera,
           "camera_config": {},
           "file_writer_config": {},
           "skip_animations": False,
           "always_update_mobjects": False,
           "random_seed": 0,
           "start_at_animation_number": None,
           "end_at_animation_number": None,
           "leave_progress_bars": False,
       }

其中\ **camera_config**\ 是对视频的处理，由\ **camera类**\ 完成:

**\\manimlib\\camera\\camera.py**

.. code:: python

   # \manimlib\camera\camera.py
   CONFIG = {
   # 背景颜色
           "background_image": None,
   # 视频的高宽与帧率
           "pixel_height": DEFAULT_PIXEL_HEIGHT,
           "pixel_width": DEFAULT_PIXEL_WIDTH,
           "frame_rate": DEFAULT_FRAME_RATE,
   # Note: frame height and width will be resized to match
   # the pixel aspect ratio
   # FRAME_HEIGHT = 8.0
   # FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / 						DEFAULT_PIXEL_HEIGHT
           "frame_height": FRAME_HEIGHT,
           "frame_width": FRAME_WIDTH,
   # 默认方向
           "frame_center": ORIGIN,
   # 背景颜色
           "background_color": BLACK,
           "background_opacity": 1,
   # Points in vectorized mobjects with norm greater
   # than this value will be rescaled.
           "max_allowable_norm": FRAME_WIDTH,
           "image_mode": "RGBA",
           "n_channels": 4,
           "pixel_array_dtype": 'uint8',
   # z_buff_func is only used if the flag above is set to True.
   # round z coordinate to nearest hundredth when comparring
   		"z_buff_func": lambda m: np.round(m.get_center()[2], 2),
           "cairo_line_width_multiple": 0.01,
       }

所有的动画都是继承自Scene,所以动画的某些特定的属性可以通过CONFIG修改：

例子：

插入背景图片

.. code:: python

   class TextLike1DArrays(Scene):
   	CONFIG={
   		"camera_config": {
   			"background_image": r"1.png",
   		},
   	}
   	def construct(self):
   		self.add(TextMobject("Text").set_color(RED))
   		self.wait()

.. figure:: ../assets/image/1565833717545.png
   :alt: 


详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>`  。