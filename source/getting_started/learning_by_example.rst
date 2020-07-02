案例学习
=============

.. admonition:: 声明

    第一个示例翻译自EulerTour的教程，其余为鹤翔万里编写

样例 ``example_scenes.py`` 包含了一些学习manim的示例场景，可以运行测试，也可以入门学习

方变圆SquareToCircle
----------------------

在manim文件夹中尝试执行运行命令 ``$ python -m manim example_scenes.py SquareToCircle -p`` (通过clone存储库安装)，或
``$ manim example_scenes.py SquareToCircle -p`` (通过pypi安装)

.. code-block:: python
   :linenos:

   from manimlib.imports import *

   class SquareToCircle(Scene):
       def construct(self):
           circle = Circle()
           square = Square()
           square.flip(RIGHT)
           square.rotate(-3 * TAU / 8)
           circle.set_fill(PINK, opacity=0.5)

           self.play(ShowCreation(square))
           self.play(Transform(square, circle))
           self.play(FadeOut(square))
   

.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/example/SquareToCircle.mp4" type="video/mp4">
   </video>


.. note::

  选项 ``-p`` 使用系统默认播放器播放渲染出的视频文件，没有指定质量，则默认使用 ``-w`` 选项最高画质（1440p60），其他常用选项:
    - ``-l`` 低分辨率480p15渲染更快
    - ``-m`` 中等分辨率720p30
    - ``-s`` 只导出最后一帧

  运行 ``python -m manim -h`` 或 ``manim -h`` 查看所有可用选项


让我们一行一行解析 ``SquareToCircle`` 的代码

.. code-block:: python
   :lineno-start:

   from manimlib.imports import *

将manim中的所有类都引入进来，可以直接使用

.. code-block:: python
   :lineno-start: 3

   class SquareToCircle(Scene):

通过编写一个 :class:`~scene.scene.Scene` 的子类来创建一个场景，用于渲染出视频

.. code-block:: python
   :lineno-start: 4

   def construct(self):

在 :meth:`~scene.scene.Scene.construct` 方法中说明当 :class:`~scene.scene.Scene` 渲染时要进行什么操作

.. code-block:: python
   :lineno-start: 5

   circle = Circle()
   square = Square()

``Circle()`` 和 ``Square()`` 创建了 :class:`~mobject.geometry.Circle` 和 :class:`~mobject.geometry.Square` 的实例，即一个圆一个方

它们都是 :class:`~mobject.mobject.Mobject` 的子类，注意如果一个 :class:`~mobject.mobject.Mobject` 实例
没有添加到 :class:`~scene.scene.Scene` 中, 渲染之后就不会看到任何东西

.. code-block:: python
   :lineno-start: 7

   square.flip(RIGHT)
   square.rotate(-3 * TAU / 8)
   circle.set_fill(PINK, opacity=0.5)

``flip()`` ``rotate()`` ``set_fill()`` 在执行动画之前应用了一些mobjects的变换

- 调用 :meth:`~mobject.mobject.Mobject.flip` 以水平为轴翻转了 :class:`~mobject.geometry.Square`，相当于x轴上的反射
- 调用 :meth:`~mobject.mobject.Mobject.rotate` 逆时针旋转了 :class:`~mobject.geometry.Square` 3/8圆.
- 调用 :meth:`~mobject.mobject.Mobject.set_fill` 设置了 :class:`~mobject.geometry.Circle` 填充颜色为粉色(PINK), 不透明度(opacity)为0.5.

详细教程可以看 `〔manim教程〕第一讲 物体的位置与坐标变换  <https://www.bilibili.com/video/BV1p54y197cC>`_

.. code-block:: python
   :lineno-start: 11

   self.play(ShowCreation(square))
   self.play(Transform(square, circle))
   self.play(FadeOut(square))

实例化 :class:`~animation.animation.Animation` 构建动画

每个 :class:`~animation.animation.Animation` 传入一个或多个 :class:`~mobject.mobject.Mobject` 对象参数
传递给 :meth:`~scene.scene.Scene.play` 呈现出动画，构建视频。

:class:`~mobject.mobject.Mobject` 实例会自动添加到 :class:`~scene.scene.Scene` 中，当使用动画时
你可以把 :class:`~mobject.mobject.Mobject` 通过使用 :meth:`~scene.scene.Scene.add` 方法手动添加到 :class:`~scene.scene.Scene` 中


- :class:`~animation.creation.ShowCreation` 在屏幕上绘制出一个 :class:`~mobject.mobject.Mobject` 
- :class:`~animation.transform.Transform` 把一个 :class:`~mobject.mobject.Mobject` 变成另一个图像
- :class:`~animation.creation.FadeOut` 使一个 :class:`~mobject.mobject.Mobject` 淡出

.. note::

  第一个Mobject对象会被 :class:`~animation.transform.Transform` 方法修改，第二个对象不会被添加到Scene类中。
  仅仅更改了外形但是没有更改根本/基础的属性

  例子中，``transform()`` 变换后 ``square`` 还是 :class:`~mobject.geometry.Square` 的实例，仅仅是渲染出来圆形外表，还要调用 :class:`~mobject.geometry.Square` 的属性和方法。

扭曲正方形WarpSquare
----------------------

.. code-block:: python
   :linenos:

   from manimlib.imports import *

   class WarpSquare(Scene):
       def construct(self):
           square = Square()
           self.play(ApplyPointwiseFunction(
               lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
               square
           ))
           self.wait()

.. raw::

   <video width="560" height="315" controls>
       <source src="../_static/example/WarpSquare.mp4" type="video/mp4">
   </video>

前四行和前面的一样，不重复了。第五行同样创建了一个默认的正方形

.. code-block:: python
   :line-start: 6

   self.play(ApplyPointwiseFunction(
       lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
       square
   ))

从第六行开始，执行了一个动画 :class:`~animation.transform.ApplyPointwiseFunction` ，
传入了一个函数 ``lambda point: complex_to_R3(np.exp(R3_to_complex(point)))``

这个函数的输入值是一个点坐标，先经过 ``R3_to_complex`` 函数将点坐标转换为该点在复平面上代表的复数值，
后求了e指数，将其结果传入 ``complex_to_R3`` 函数，将结果的复数转换为在复平面上的点坐标。

将这个函数和物体square传入 :class:`~animation.transform.ApplyPointwiseFunction` 后，
会对square的点集施加这个函数的作用（将每个点设为将该点传入函数后的返回值），实现了复变换。

.. code-block:: python
   :line-start: 10

   self.wait()

添加了一个停顿，默认1秒，相当于 ``self.wait(1)`` 。类似的，可以使用 ``self.wait(3)`` 来停顿3秒。

书写文字WriteStuff
-------------------

.. code-block:: python
   :linenos:

   from manimlib.imports import *

   class WriteStuff(Scene):
       def construct(self):
           example_text = TextMobject(
               "This is a some text",
               tex_to_color_map={"text": YELLOW}
           )
           example_tex = TexMobject(
               "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
           )
           group = VGroup(example_text, example_tex)
           group.arrange(DOWN)
           group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
   
           self.play(Write(example_text))
           self.play(Write(example_tex))
           self.wait()

.. raw::

   <video width="560" height="315" controls>
       <source src="../_static/example/WriteStuff.mp4" type="video/mp4">
   </video>

.. code-block:: python
   :line-start: 5

   example_text = TextMobject(
       "This is a some text",
       tex_to_color_map={"text": YELLOW}
   )

第五行到第八行创建了一个文字（:class:`~mobject.svg.tex_mobject.TextMobject`），内容是"This is a some text"（打错字了）。
第七行传入了一个字典 ``tex_to_color_map`` 将"text"指定为黄色。这时 :class:`~mobject.svg.tex_mobject.TextMobject`
会自动识别拆分开字符串，将并将"text"部分设置为黄色。

.. code-block:: python
   :line-start: 9

   example_tex = TexMobject(
       "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
   )

第九行到第十一行创建了一个公式（:class:`~mobject.svg.tex_mobject.TexMobject`），它使用LaTeX来渲染，所以使用LaTeX的公式语法，
并且在python中，需要将 ``\`` 转义写为 ``\\`` ，或者在字符串前加上 ``r`` ，例如这三行也可以写为：

.. code-block:: python
   :line-start: 9

   example_tex = TexMobject(
       r"\sum_{k=1}^\infty {1 \over k^2} = {\pi^2 \over 6}",
   )

.. code-block:: python
   :line-start: 12

   group = VGroup(example_text, example_tex)
   group.arrange(DOWN)
   group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

| 第十二行到第十四行先创建了一个物体集合（:class:`~mobject.types.vectorized_mobject.VGroup`），包含前面创建的文字和公式
| 第十三行调用了 ``arrange`` 方法，将 ``group`` 中的物体依次向下（DOWN）排列
| 第十四行将整个 ``group`` 缩放到宽度为画面宽度，并且距离两边为 ``LARGE_BUFF``

.. code-block:: python
   :line-start: 16

   self.play(Write(example_text))
   self.play(Write(example_tex))
   self.wait()

| 第十六行开始是场景中的动画部分，前两行将创建的文字和公式使用 :class:`~animation.creation.Write` 动画"写"在画面中
| 并且最后添加了一秒的停顿

更新程序UpdatersExample
------------------------

.. code-block:: python
   :linenos:

   from manimlib.imports import *

   class UpdatersExample(Scene):
       def construct(self):
           decimal = DecimalNumber(
               0,
               show_ellipsis=True,
               num_decimal_places=3,
               include_sign=True,
           )
           square = Square().to_edge(UP)
   
           decimal.add_updater(lambda d: d.next_to(square, RIGHT))
           decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
           self.add(square, decimal)
           self.play(
               square.to_edge, DOWN,
               rate_func=there_and_back,
               run_time=5,
           )
           self.wait()

.. raw::

   <video width="560" height="315" controls>
       <source src="../_static/example/UpdatersExample.mp4" type="video/mp4">
   </video>

.. code-block:: python
   :line-start: 5

   decimal = DecimalNumber(
       0,
       show_ellipsis=True,
       num_decimal_places=3,
       include_sign=True,
   )

| 第五行起创建了一个可变的十进制数字 :class:`~mobject.numbers.DecimalNumber` ，初始值为0
| 从第七行起设置了其属性，即显示省略号 ``show_ellipsis=True`` ，小数保留3位 ``num_decimal_places=3`` ，正数包含正号 ``include_sign=True``

.. code-block:: python
   :line-start: 13

   decimal.add_updater(lambda d: d.next_to(square, RIGHT))
   decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))

从第十三行起为这个数字添加了两个更新程序（``updater``）
1. 将这个数字始终放在正方形右侧（即始终调用 ``next_to`` 这个方法来维护数字的位置）
2. 将这个数字的值始终设置为正方形在画面中的纵坐标

设置了updater之后，每一帧在运行时都会调用传入的函数来更新当前物体，所以传入的函数的参数为一个物体，没有返回值，在函数内部调用这个物体的方法来维护属性

.. code-block:: python
   :line-start: 15

   self.add(square, decimal)
   self.play(
       square.to_edge, DOWN,
       rate_func=there_and_back,
       run_time=5,
   )
   self.wait()

第十五行直接将数字和正方形添加在画面中，即视频一开始两物体就已经存在于画面中了

| 第十六行开始为一个动画， ``square.to_edge, DOWN`` 表示将 ``square`` 执行了 ``.to_edge(DOWN)`` 之后设置为目标，并且变换到那个位置处
| ``rate_func=there_and_back`` 指明了当前动画使用的速率函数为 ``there_and_back`` ，即到位置后再回来
| ``run_time=5`` 指明了当前动画需要5秒

整体示例OpeningManimExample
-----------------------------

在看过了前面的例子之后，文件中的第一个视频就容易理解了

.. code-block:: python
   :linenos:

   from manimlib.imports import *

   class OpeningManimExample(Scene):
       def construct(self):
           title = TextMobject("This is some \\LaTeX") # 文字
           basel = TexMobject(                         # 公式
               "\\sum_{n=1}^\\infty "
               "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
           )
           VGroup(title, basel).arrange(DOWN)          # 集合到一起后排列位置
           self.play(
               Write(title),             # "写"出title文字
               FadeInFrom(basel, UP),    # 将basel公式从上方淡入
           )
           self.wait()  # 停顿一秒
   
           transform_title = TextMobject("That was a transform")
           transform_title.to_corner(UP + LEFT) # 放到最左上角
           self.play(
               Transform(title, transform_title), # 将title变换为transform_title
               LaggedStart(*map(FadeOutAndShiftDown, basel)), # 将basel公式中的每个字符依次从下方淡出
           )
           self.wait()  # 停顿一秒
   
           grid = NumberPlane()  # 构建一个坐标平面
           grid_title = TextMobject("This is a grid")
           grid_title.scale(1.5)
           grid_title.move_to(transform_title)
   
           self.add(grid, grid_title)  # 确保grid_title在grid上方
           self.play(
               FadeOut(title),               # 淡出title
               FadeInFromDown(grid_title),   # 从下方淡入grid_title
               ShowCreation(grid, run_time=3, lag_ratio=0.1), # 创建grid的动画，时长为3，延迟为10%
           )
           self.wait()
   
           grid_transform_title = TextMobject(
               "That was a non-linear function \\\\"
               "applied to the grid"
           )
           grid_transform_title.move_to(grid_title, UL)
           grid.prepare_for_nonlinear_transform() # 让grid准备进行非线性变换
           self.play(
               grid.apply_function,       # 对grid施加一个函数，实现非线性变换
               lambda p: p + np.array([   # 输入值为一个点，返回值也为一个点
                   np.sin(p[1]),
                   np.sin(p[0]),
                   0,
               ]),
               run_time=3,
           )
           self.wait()
           self.play(
               Transform(grid_title, grid_transform_title)
           )
           self.wait()

.. raw::

   <video width="560" height="315" controls>
       <source src="../_static/example/OpeningManimExample.mp4" type="video/mp4">
   </video>