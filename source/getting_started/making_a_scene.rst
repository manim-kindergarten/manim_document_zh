编写场景-Making a Scene
===============================

.. admonition:: 声明

        这一页翻译自EulerTour的教程,我只是翻译+学习笔记

场景是当manim运行时需要渲染的东西，每个场景包含一些需要执行动画的 :class:`~mobject.mobject.Mobject` 的声明。
在代码中，一个场景是继承自 :class:`~scene.scene.Scene` 的子类，并且实现了 ``construct`` 方法。
这样，manim就可以运行这个方法来渲染出这个场景

.. code-block:: python
   :linenos:

    from manimlib.imports import *

    class ExampleScene(Scene):
        def construct(self):
            # Add and animate mobjects here

上述是一个 ``Scene`` 类的定义，结合 example_scenes.py 的 ``SquareToCircle`` 就可以理解


场景类的CONFIG配置 
--------------------

所有的动画均是scene类的子类产生的，因此scene的功能比较少，主要是对一些基础的属性进行配置

**\\manimlib\\scene\\scene.py**

变量的默认值见下：

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
        # FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
        "frame_height": FRAME_HEIGHT,
        "frame_width": FRAME_WIDTH,
        # 相机中心位置
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
   		"z_buff_func": lambda m: np.round(m.get_center()[2], 2),
        "cairo_line_width_multiple": 0.01,
    }

所有的动画都是继承自Scene,所以动画的某些特定的属性可以通过CONFIG修改：

例：插入背景图片

.. code:: python

   class BackGround(Scene):
       CONFIG = {
           "camera_config": {
               "background_image": "path/to/background.png",
           },
       }
       def construct(self):
           self.add(TextMobject("Text").set_color(RED))
           self.wait()

.. figure:: ../assets/image/1565833717545.png
   :alt: 

