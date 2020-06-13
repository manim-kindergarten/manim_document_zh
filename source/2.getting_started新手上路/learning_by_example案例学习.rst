案例学习-Learning by Example
=============================


.. admonition:: 声明

      此例子，来自 `这一集 <https://www.bilibili.com/video/BV1W4411Z7Zt?p=5>`_ 

写视频之前必须学会制作图片，因为视频就是根据帧率连续播放图片的过程。

在example_scenes.py中自定义一个类：

.. code::

   class FirstScene(Scene): 
      def construct(self): 
         text = TextMobject("text")
         self.add(text)

命令行执行

.. code::

    python -m manim example_scenes.py FirstScene -ps

新版本中，如果你不选定里面的类（比如FirstScene）：

.. code::

   python -m manim example_scenes.py -ps

就会让你选择渲染那个场景（只含有一个场景的除外）：

.. code::

   1: FirstScene
   2: OpeningManimExample
   3: SquareToCircle
   4: UpdatersExample
   5: WarpSquare
   6: WriteStuff

   Choose number corresponding to desired scene/arguments.
   (Use comma separated list for multiple entries)
   Choice(s):     



.. figure:: ../assets/image/FirstScene.png
    :width: 100%
    :align: center

    FirstScene

画一个点

.. code::

   class Positions(Scene):
      def construct(self):
         object = Dot()
         # 用object.to_edge(UP)传参为常量中的向量UP可以向量指定位置np.array((0., 1., 0.))
         # 用object.to_corner(UR)传参为常量中的向量UR可以移动到向量指定位置np.array((右1., 上1., 0.))
         self.add(object)
         self.wait()


定位方式可以有绝对和相对定位。

绝对定位

``.to_edge()`` 和 ``.to_corner()`` 方法
``.to_edge(DIRECTION,buff=NUMBER)`` 可以设置边距buff

相对定位

``.move_to()``
``.next_to()``
``.shift()``

详细教程可以看 `〔manim教程〕第一讲 物体的位置与坐标变换  <https://www.bilibili.com/video/BV1p54y197cC>`_


方变圆-SquareToCircle
-----------------------

.. admonition:: 声明

   这部分是EulerTour写的教程,我只是翻译+学习笔记

样例 ``example_scenes.py`` 包含了一些学习manim的示例场景

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
       <source src="../_static/Animation/SquareToCircle.mp4" type="video/mp4">
   </video>


.. note::

  选项 ``-p`` 使用系统默认播放器播放渲染出的视频文件，没有指定质量，则默认使用 ``-w`` 选项最高画质（1440p60）

  其他常用选项:

    * ``-l`` 低分辨率480p15渲染更快
    * ``-m`` 中等分辨率720p30
    * ``-s`` 只导出最后一帧

  运行 ``python -m manim -h`` 或 ``manim -h`` 查看所有可用选项


让我们一行一行解析 ``SquareToCircle`` 的代码

.. code-block:: python
   :lineno-start: 3

   class SquareToCircle(Scene):

你通过构建 :class:`~scene.scene.Scene` 的子类来创建视频

manim中的所有 :class:`~scene.scene.Scene` 只包含类定义本身，意思是类之间互不干涉，也不会执行类之外的内容

比如 ``$ python -m manim example_scenes.py OpeningManimExample -pl`` 和 ``SquareToCircle`` 的代码不相干

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

调用 :meth:`~mobject.mobject.Mobject.flip` 以水平为轴翻转了 :class:`~mobject.geometry.Square`，相当于x轴上的反射

调用 :meth:`~mobject.mobject.Mobject.rotate` 逆时针旋转了 :class:`~mobject.geometry.Square` 3/8圆.

调用 :meth:`~mobject.mobject.Mobject.set_fill` 设置了 :class:`~mobject.geometry.Circle` 填充颜色为粉色(PINK), 不透明度(opacity)为0.5.

.. code-block:: python
   :lineno-start: 11

   self.play(ShowCreation(square))
   self.play(Transform(square, circle))
   self.play(FadeOut(square))

实例化 :class:`~animation.animation.Animation` 构建动画

每个 :class:`~animation.animation.Animation` 传入一个或多个 :class:`~mobject.mobject.Mobject` 对象参数
传递给 :meth:`~scene.scene.Scene.play` 呈现出动画，构建视频。

:class:`~mobject.mobject.Mobject` 实例会自动添加到 :class:`~scene.scene.Scene` 中，当使用动画时
你可以把 :class:`~mobject.mobject.Mobject` 手动添加到 :class:`~scene.scene.Scene` 中通过使用 :meth:`~scene.scene.Scene.add` 方法


:class:`~animation.creation.ShowCreation` 在屏幕上绘制出一个 :class:`~mobject.mobject.Mobject` 

:class:`~animation.transform.Transform` 把一个 :class:`~mobject.mobject.Mobject` 变成另一个图像

:class:`~animation.creation.FadeOut` 使一个 :class:`~mobject.mobject.Mobject` 淡出

.. note::

  第一个Mobject对象会被 :class:`~animation.transform.Transform` 方法修改，第二个对象不会被添加到Scene类中。
  仅仅更改了外形但是没有更改根本/基础的属性

  例子中，``transform()`` 变换后 ``square`` 还是 :class:`~mobject.geometry.Square` 的实例，仅仅是渲染出来圆形外表，还要调用 :class:`~mobject.geometry.Square` 的属性和方法。`03:40动画很清晰 <https://www.bilibili.com/video/BV1W4411Z7Zt?p=11>`_ 。
   

补充一个类似的案例：from `manim-tutorial <https://github.com/malhotra5/Manim-Tutorial>`_ 。

.. literalinclude:: ../assets/code/manim-tutorial/basics.py
   :linenos:


.. raw:: html

    <video width="700" height="394" controls>
        <source src="../_static/manim-tutorial/basics_Shapes.mp4" type="video/mp4">
    </video>


帮助-manim help
-----------------------


``python -m  manim --help``

.. parsed-literal::

   usage: manim.py [-h] [-p] [-w] [-s] [-l] [-m] [--high_quality] [-g] [-i] [-f]
                  [-t] [-q] [-a] [-o FILE_NAME] [-n START_AT_ANIMATION_NUMBER从动画编号开始]
                  [-r 分辨率RESOLUTION] [-c COLOR] [--sound] [--leave_progress_bars]
                  [--media_dir MEDIA_DIR]
                  [--video_dir VIDEO_DIR | --video_output_dir VIDEO_OUTPUT_DIR]
                  [--tex_dir TEX_DIR] [--livestream] [--to-twitch]
                  [--with-key TWITCH_KEY]
                  [file] [scene_names [scene_names ...]]
   positional arguments:
   file                  path to file holding the python code for the scene包含场景的python代码的文件的路径，如example_scenes.py 
   scene_names           Name of the Scene class you want to see您要查看的Scene类的名称，如SquareToCircle

   optional arguments:
   -h, --help            show this help message and exit
   -p, --preview         Automatically open the saved file once its done完成后自动打开预览保存的文件

   -w, --write_to_movie  Render the scene as a movie file将场景渲染为电影文件
   -s, --save_last_frame 显示最后一帧Save the last frame
   -l, --low_quality     Render at a low quality (for faster rendering)快，低质量渲染
   -m, --medium_quality  Render at a medium quality 中质量
   --high_quality        Render at a high quality 高质量
   -g, --save_pngs       Save each frame as a png 每帧保存png
   -i, --save_as_gif     Save the video as gif 视频保存为gif
   -f, --show_file_in_finder    Show the output file in finder 在finder中显示输出文件
   -t, --transparent     Render to a movie file with an alpha channel使用Alpha通道渲染到电影文件
   -q, --quiet
   -a, --write_all       Write all the scenes from a file写一个文件中所有场景
   -o FILE_NAME, --file_name FILE_NAME
                         Specify the name of the output file, ifit should be different from the scene class name指定输出文件的名称（如果它与场景类名称不同）
   -n START_AT_ANIMATION_NUMBER, --start_at_animation_number START_AT_ANIMATION_NUMBER
                         Start rendering not from the first animation, but from another, specified by its index. 
                         If you passin two comma separated values, e.g. "3,6", it will end the rendering at the second value。
                         不从第一个动画开始渲染，而是从其索引指定的另一个动画开始渲染。如果您传入两个逗号分隔的index值，
                         例如“ 3,6”，它将在第二个index值处结束渲染。
   -r RESOLUTION, --resolution RESOLUTION
                         Resolution, passed as "height,width"分辨率，“高度，宽度”传递
   -c COLOR, --color COLOR
                         Background color背景色
   --sound               Play a success/failure sound显示成功/失败的声音
   --leave_progress_bars
                         Leave progress bars displayed in terminal保持进度条显示在终端中，
   --media_dir MEDIA_DIR
                         directory to write media写入多媒体路径
   --video_dir VIDEO_DIR
                         directory to write file tree for video写入视频文件树的目录
   --video_output_dir VIDEO_OUTPUT_DIR
                         directory to write video 编写视频的目录
   --tex_dir TEX_DIR     directory to write tex 设置text路径
   --livestream          Run in streaming mode流模式
   --to-twitch           Stream to twitch
   --with-key TWITCH_KEY
                         Stream key for twitch


默认 ``--preview`` 分辨率1440p60，在manimlib/contants.py有需要可以自行修改， ``-l`` 低分辨率480p15,小项目查阅的时候，快很多。

.. code-block::

  python -m manim example_scenes.py SquareToCircle -ps

``-s`` 可以在images文件夹下看到保存的最后一张图片，比如在一个比较大的项目中，想看自己的某一张图画出来效果，可以使用 ``-s`` 导出最后一帧

.. code-block:: bash

   python -m manim example_scenes.py SquareToCircle -al

``-a`` 把文件中所有scene写成视频。

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -o <file_name>

输出 <file_name>.mp4

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -pl -c WHITE

.. code-block:: bash

  manim example_scenes.py SquareToCircle -pl -c '#FFFFFF' 

.. code-block:: bash

  manim example_scenes.py SquareToCircle -pl -c '#FFFFFF' 
  
白色背景


.. code-block:: bash
   
   self.play(ShowCreation(square))         #0
   self.play(Transform(square, circle))    #1
   self.play(FadeOut(square))              #2


SquareToCircle有3个animations渲染任务，可以：

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -pl -n 2 

这就能直接从第3个（0开始）animations渲染到最后。

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -r 1080

获得 1920x1080 分辨率的视频。


**存为gif**


   你可以使用 ``python -m manim animation.py name_scene -im`` 渲染中等质量的gif文件
   ``python -m manim animation.py name_scene -gm`` 获取每帧的图片


ps: 选项 ``-i`` 目前被取消了，依旧会生成mp4文件，可以按照常见问题中更改，或者
使用 `MK版本的manim <https://github.com/manim-kindergarten/manim>`_

也可以使用ffmpeg手动转换

.. code-block:: bash

   ffmpeg -i SquareToCircle.mp4 -b:v 2048k SquareToCircle.gif

通过例子学习是最快的,看已有的项目模仿也很快，但是系统学习+定制还是要看manimlib源码
