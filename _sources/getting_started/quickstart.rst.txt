快速入门
===========

在按照 :doc:`installation` 页面中的指导安装好 manim 的环境后，你可以尝试从头开始自己制作一个场景。

首先，根据如下结构创建一个新的 ``.py`` 文件（如 ``start.py`` ）：

.. code-block:: text
    :emphasize-lines: 8

    manim/
    ├── manimlib/
    │   ├── animation/
    │   ├── ...
    │   ├── default_config.yml
    │   └── window.py
    ├── (custom_config.yml)
    └── start.py

然后粘贴如下代码（稍后我会详细解释其每行的作用）：

.. code-block:: python
    :linenos:

    from manimlib import *

    class SquareToCircle(Scene):
        def construct(self):
            circle = Circle()
            circle.set_fill(BLUE, opacity=0.5)
            circle.set_stroke(BLUE_E, width=4)

            self.add(circle)

运行这个命令：

.. code-block:: sh

    manimgl start.py SquareToCircle

屏幕上会弹出一个窗口，这时你可以：

- 滚动鼠标中键来上下移动画面
- 按住键盘上 :kbd:`z` 键的同时滚动鼠标中键来缩放画面
- 按住键盘上 :kbd:`s` 键的同时移动鼠标来平移画面
- 按住键盘上 :kbd:`d` 键的同时移动鼠标来改变三维视角

最后，你可以通过按 :kbd:`q` 来关闭窗口并退出程序.

再运行这个命令：

.. code-block:: sh

    manimgl start.py SquareToCircle -os

这时将没有窗口弹出，当程序运行结束后，会自动打开这张渲染得到的图片
（默认位于同级目录的子目录 ``images/`` 中）：

.. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/quickstart/SquareToCircle.png
    :align: center

制作图片
-------------

接下来我们来详细看看每一行都有什么作用：

**Line 1**: 

.. code-block:: python
    
    from manimlib import *
    
这将一步引入在使用 manim 时所有可能会用到的类。

**Line 3**:

.. code-block:: python
    
    class SquareToCircle(Scene):

创建一个 :class:`~manimlib.scene.scene.Scene` 的子类 ``SquareToCircle``，
这将是你编写并要渲染的场景。

**Line 4**:

.. code-block:: python
    
    def construct(self):

编写 :meth:`~manimlib.scene.scene.Scene.construct` 方法，
这里面的内容将决定如何创建画面中的物体，以及需要执行哪些操作。

**Line 5**:

.. code-block:: python
    
    circle = Circle()

创建一个圆（:class:`~manimlib.mobject.geometry.Circle` 类的实例），叫做 ``circle``。

**Line 6~7**:

.. code-block:: python
    
    circle.set_fill(BLUE, opacity=0.5)
    circle.set_stroke(BLUE_E, width=4)

通过调用 circle 的方法设置 circle 的样式。

- ``.set_fill()`` 方法将这个圆的填充颜色设为蓝色（``BLUE``，在 :doc:`../documentation/constants` 中定义），填充透明度设为0.5。
- ``.set_stroke()`` 方法将这个圆的线条颜色设为深蓝色（``BLUE_E``，在 :doc:`../documentation/constants` 中定义），线条宽度设为4

**Line 9**:

.. code-block:: python
    
    self.add(circle)

通过 :class:`~manimlib.scene.scene.Scene` 的 :meth:`~manimlib.scene.scene.Scene.add` 方法，将这个圆添加到画面上。

添加动画
--------------

下面我们改变一些代码，添加一些动画来制作视频而不是仅仅只有图片。

.. code-block:: python
    :linenos:

    from manimlib import *

    class SquareToCircle(Scene):
        def construct(self):
            circle = Circle()
            circle.set_fill(BLUE, opacity=0.5)
            circle.set_stroke(BLUE_E, width=4)
            square = Square()
    
            self.play(ShowCreation(square))
            self.wait()
            self.play(ReplacementTransform(square, circle))
            self.wait()

这次运行：

.. code-block:: sh

    manimgl start.py SquareToCircle

弹出的窗口中会播放一个绘制正方形并变换为圆的动画。
若想要保存这段动画，运行：

.. code-block:: sh
    
    manimgl start.py SquareToCircle -ow

这次将不会弹出窗口，但会在运行结束后自动打开这个视频文件
（默认存放在与 ``start.py`` 同级的 ``videos/`` 文件夹中）：

.. raw:: html

    <video class="manim-video" controls loop autoplay src="https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/quickstart/SquareToCircle.mp4"></video>

我们再来看看这次的代码。前7行和前面的一样，第8行类似第5行，
创建了一个 :class:`~manimlib.mobject.geometry.Square` 类的实例，命名为 ``square``。

**Line 10**:

.. code-block:: python
    
    self.play(ShowCreation(square))

通过 :class:`~manimlib.scene.scene.Scene` 的 :meth:`~manimlib.scene.scene.Scene.play` 方法播放了一个动画。
:class:`~manimlib.animation.creation.ShowCreation` 为一个动画，其表示呈现出创建给出物体的过程。
``self.play(ShowCreation(square))`` 即播放创建 ``square`` 的动画。

**Line 11**:

.. code-block:: python
    
    self.wait()

通过 :class:`~manimlib.scene.scene.Scene` 的 :meth:`~manimlib.scene.scene.Scene.wait` 方法来停顿（默认1s），
你可以向其中传入参数来表示停顿的时间（如 ``self.wait(3)`` 表示停顿3s）

**Line 12**:

.. code-block:: python
    
    self.play(ReplacementTransform(square, circle))

播放将 ``square`` 变化为 ``circle`` 的动画。``ReplacementTransform(A, B)`` 
表示把A转换为B的图案并替代B

**Line 13**: 同Line 11，停顿1s


启用交互
------------------

支持交互是新版本的新特性，可以在代码的末尾加上如下一行来启用交互：

.. code-block:: python

    self.embed()

这时再执行 ``manimgl start.py SquareToCircle``。

在前面的动画执行后，将会在命令行打开 iPython 终端。这时你将不能触碰动画窗口，而只能在终端中输入要运行的代码，
如果要和动画窗口进行互动，则要在终端中输入 ``touch()`` 或 ``self.interact()``。

在 iPython 中你可以继续编写代码，
回车后将会立即运行你输入的语句。例如：向其中分别输入以下行
（``self.play`` 在此时可以简写为 ``play`` ）：

.. code-block:: python

    # 在水平方向上拉伸到四倍
    play(circle.stretch, 4, {"dim": 0})
    # 旋转90°
    play(Rotate(circle, TAU / 4))
    # 在向右移动2单位同时缩小为原来的1/4
    play(circle.shift, 2 * RIGHT, circle.scale, 0.25)
    # 为了非线性变换，给circle增加10段曲线（不会播放动画）
    circle.insert_n_curves(10)
    # 给circle上的所有点施加f(z)=z^2的复变换
    play(circle.apply_complex_function, lambda z: z**2)
    # 关闭窗口并退出程序
    exit()

你将得到类似下面的动画：

.. raw:: html

    <video class="manim-video" controls loop autoplay src="https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/quickstart/SquareToCircleEmbed.mp4"></video>

如果你想要直接进入交互模式的话，你不必特意编写一个只含 ``self.embed()`` 的空场景，
你可以直接运行下面的命令（这会在弹出窗口的同时进入iPython终端）：

.. code-block:: sh

    manimgl

成功入门
--------------

在看完上述内容后，你已经了解如何使用 manim 了，下面你可以看一些例子，在 :doc:`example_scenes` 页面中。
但在这之前，你最好先了解一下 manim 的 :doc:`configuration`。

