常量部分constants
=====================

.. admonition:: 声明

   这一页翻译+笔记自EulerTour写的教程,整合elteoremadebeethoven写的 
   `manim_3feb_docs <https://github.com/Elteoremadebeethoven/manim_3feb_docs.github.io/tree/master/source>`_ 

   还有鹤翔万里在manim_sandbox中编写的wiki中的内容

编辑manimlib/constants.py相关定义即可。
``manimlib`` 文件夹中的 ``constants.py`` 定义了在运行manim时需要的常量。
一些常量在这里没有说明，因为他们只在manim内部使用

配置目录
---------

MEDIA_DIR
   文件夹 ``VIDEO_DIR`` 和 ``TEX_DIR`` 创建的位置（如果他们没有被选项更改的话）
VIDEO_DIR
   存放manim渲染结果视频的文件夹，当一个场景渲染结束，它会存放在
   ``VIDEO_DIR/<module_name>/<scene_name>/<quality>/<scene_name>.mp4``.
   默认根据 ``MEDIA_DIR`` 创建
TEX_DIR
   使用LaTeX创建的文件（tex/svg/log/xdv/aux），会作为缓存，来防止多次重写LaTeX
TEXT_DIR
   使用 ``Text`` 类时，通过cairo创建的文字的svg，会作为缓存

这些文件夹如果不存在会被创建

当你第一次运行一个动画时，你会看到下面的信息::

    Media will be stored in media/. You can change this behavior by writing a different directory to media_dir.txt.

这是因为动画文件会被保存到 ``media`` 文件夹中，在manim文件夹中，你会自动生成一个文件夹和两个文件：

::

    .
    ├── manim/imports.py
    ├── manim.py
    ├── stage_scenes.py 
    ├── media              # <- New directory
    ├── media_dir.txt      # <- New file
    └── manimlib
        └── media_dir.txt  # <- New file


更改目录的方法很多，可以新建文件media_dir.txt在这里设置视频保存路径，可以是绝对路径：C:\\manim\\media。
也可以在 ``constants.py`` 文件中配置。


在\ ``manimlib/constants.py``\ 中定义了一些常用的常量，如下

定义的渲染画质
--------------

.. code:: python

   PRODUCTION_QUALITY_CAMERA_CONFIG = { # -w的画质
       "pixel_height": 1440,
       "pixel_width": 2560,
       "frame_rate": 60,
   }

   HIGH_QUALITY_CAMERA_CONFIG = { # --high_quality的画质
       "pixel_height": 1080,
       "pixel_width": 1920,
       "frame_rate": 60,
   }

   MEDIUM_QUALITY_CAMERA_CONFIG = { # -m的画质
       "pixel_height": 720,
       "pixel_width": 1280,
       "frame_rate": 30,
   }

   LOW_QUALITY_CAMERA_CONFIG = { # -l的画质
       "pixel_height": 480,
       "pixel_width": 854,
       "frame_rate": 15,
   }

   # 默认画质
   DEFAULT_PIXEL_HEIGHT = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_height"]
   DEFAULT_PIXEL_WIDTH = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_width"]
   DEFAULT_FRAME_RATE = 60

点密度，线宽度
----------------------

.. code:: python

   DEFAULT_POINT_DENSITY_2D = 25
   DEFAULT_POINT_DENSITY_1D = 250

   DEFAULT_STROKE_WIDTH = 4

画面上坐标的宽高
------------------------

.. code:: python

   FRAME_HEIGHT = 8.0  # 画面高默认8个单位
   FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
   FRAME_Y_RADIUS = FRAME_HEIGHT / 2
   FRAME_X_RADIUS = FRAME_WIDTH / 2

buff
-----

.. code:: python

   SMALL_BUFF = 0.1
   MED_SMALL_BUFF = 0.25
   MED_LARGE_BUFF = 0.5
   LARGE_BUFF = 1

   DEFAULT_MOBJECT_TO_EDGE_BUFFER = MED_LARGE_BUFF # 物体和边的距离
   DEFAULT_MOBJECT_TO_MOBJECT_BUFFER = MED_SMALL_BUFF # 物体之间的距离

播放时间
-----------

.. code:: python

   DEFAULT_POINTWISE_FUNCTION_RUN_TIME = 3.0
   DEFAULT_WAIT_TIME = 1.0

.. _ref-directions:

位置坐标
---------

manim使用三维坐标，并且用 ``ndarray`` 的类型

.. code:: python

   ORIGIN = np.array((0., 0., 0.))
   UP = np.array((0., 1., 0.))
   DOWN = np.array((0., -1., 0.))
   RIGHT = np.array((1., 0., 0.))
   LEFT = np.array((-1., 0., 0.))
   IN = np.array((0., 0., -1.))
   OUT = np.array((0., 0., 1.))
   X_AXIS = np.array((1., 0., 0.))
   Y_AXIS = np.array((0., 1., 0.))
   Z_AXIS = np.array((0., 0., 1.))

   # Useful abbreviations for diagonals
   UL = UP + LEFT
   UR = UP + RIGHT
   DL = DOWN + LEFT
   DR = DOWN + RIGHT

   TOP = FRAME_Y_RADIUS * UP
   BOTTOM = FRAME_Y_RADIUS * DOWN
   LEFT_SIDE = FRAME_X_RADIUS * LEFT
   RIGHT_SIDE = FRAME_X_RADIUS * RIGHT

数学常数
--------

.. code:: python

   PI = np.pi
   TAU = 2 * PI
   DEGREES = TAU / 360

颜色
--------

这里是manim中定义的颜色的预览：(修改自 
`elteoremadebeethoven <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/_static/colors/colors.html>`_)

.. raw:: html

    <h3>BLUE</h3>
    <div class="colors BLUE_E"><p class="color-text">BLUE_E</p></div>
    <div class="colors BLUE_D"><p class="color-text">BLUE_D</p></div>
    <div class="colors BLUE_C"><p class="color-text">BLUE_C</p></div>
    <div class="colors BLUE_B"><p class="color-text">BLUE_B</p></div>
    <div class="colors BLUE_A"><p class="color-text">BLUE_A</p></div>
    <h3 style="margin-top: 6em">TEAL</h3>
    <div class="colors TEAL_E"><p class="color-text">TEAL_E</p></div>
    <div class="colors TEAL_D"><p class="color-text">TEAL_D</p></div>
    <div class="colors TEAL_C"><p class="color-text">TEAL_C</p></div>
    <div class="colors TEAL_B"><p class="color-text">TEAL_B</p></div>
    <div class="colors TEAL_A"><p class="color-text">TEAL_A</p></div>
    <h3 style="margin-top: 6em">GREEN</h3>
    <div class="colors GREEN_E"><p class="color-text">GREEN_E</p></div>
    <div class="colors GREEN_D"><p class="color-text">GREEN_D</p></div>
    <div class="colors GREEN_C"><p class="color-text">GREEN_C</p></div>
    <div class="colors GREEN_B"><p class="color-text">GREEN_B</p></div>
    <div class="colors GREEN_A"><p class="color-text">GREEN_A</p></div>
    <h3 style="margin-top: 6em">YELLOW</h3>
    <div class="colors YELLOW_E"><p class="color-text">YELLOW_E</p></div>
    <div class="colors YELLOW_D"><p class="color-text">YELLOW_D</p></div>
    <div class="colors YELLOW_C"><p class="color-text">YELLOW_C</p></div>
    <div class="colors YELLOW_B"><p class="color-text">YELLOW_B</p></div>
    <div class="colors YELLOW_A"><p class="color-text">YELLOW_A</p></div>
    <h3 style="margin-top: 6em">GOLD</h3>
    <div class="colors GOLD_E"><p class="color-text">GOLD_E</p></div>
    <div class="colors GOLD_D"><p class="color-text">GOLD_D</p></div>
    <div class="colors GOLD_C"><p class="color-text">GOLD_C</p></div>
    <div class="colors GOLD_B"><p class="color-text">GOLD_B</p></div>
    <div class="colors GOLD_A"><p class="color-text">GOLD_A</p></div>
    <h3 style="margin-top: 6em">RED</h3>
    <div class="colors RED_E"><p class="color-text">RED_E</p></div>
    <div class="colors RED_D"><p class="color-text">RED_D</p></div>
    <div class="colors RED_C"><p class="color-text">RED_C</p></div>
    <div class="colors RED_B"><p class="color-text">RED_B</p></div>
    <div class="colors RED_A"><p class="color-text">RED_A</p></div>
    <h3 style="margin-top: 6em">MAROON</h3>
    <div class="colors MAROON_E"><p class="color-text">MAROON_E</p></div>
    <div class="colors MAROON_D"><p class="color-text">MAROON_D</p></div>
    <div class="colors MAROON_C"><p class="color-text">MAROON_C</p></div>
    <div class="colors MAROON_B"><p class="color-text">MAROON_B</p></div>
    <div class="colors MAROON_A"><p class="color-text">MAROON_A</p></div>
    <h3 style="margin-top: 6em">PURPLE</h3>
    <div class="colors PURPLE_E"><p class="color-text">PURPLE_E</p></div>
    <div class="colors PURPLE_D"><p class="color-text">PURPLE_D</p></div>
    <div class="colors PURPLE_C"><p class="color-text">PURPLE_C</p></div>
    <div class="colors PURPLE_B"><p class="color-text">PURPLE_B</p></div>
    <div class="colors PURPLE_A"><p class="color-text">PURPLE_A</p></div>
    <h3 style="margin-top: 6em">Others</h3>
    <div class="colors WHITE"><p class="color-text" style="color: BLACK">WHITE</p></div>
    <div class="colors BLACK"><p class="color-text">BLACK</p></div>
    <div class="colors LIGHT_GREY"><p class="color-text-small">LIGHT_GREY</p></div>
    <div class="colors LIGHT_GRAY"><p class="color-text-small">LIGHT_GRAY</p></div>
    <div class="colors GREY"><p class="color-text">GREY</p></div>
    <div class="colors GRAY"><p class="color-text">GRAY</p></div>
    <div class="colors DARK_GREY"><p class="color-text-small">DARK_GREY</p></div>
    <div class="colors DARK_GRAY"><p class="color-text-small">DARK_GRAY</p></div>
    <div class="colors DARKER_GREY"><p class="color-text-small">DARKER_GREY</p></div>
    <div class="colors DARKER_GRAY"><p class="color-text-small">DARKER_GRAY</p></div>
    <div class="colors GREY_BROWN"><p class="color-text-small">GREY_BROWN</p></div>
    <div class="colors DARK_BROWN"><p class="color-text-small">DARK_BROWN</p></div>
    <div class="colors LIGHT_BROWN"><p class="color-text-small">LIGHT_BROWN</p></div>
    <div class="colors DARK_BLUE"><p class="color-text-small">DARK_BLUE</p></div>
    <div class="colors PINK"><p class="color-text">PINK</p></div>
    <div class="colors LIGHT_PINK"><p class="color-text-small">LIGHT_PINK</p></div>
    <div class="colors GREEN_SCREEN"><p class="color-text-small">GREEN_SCREEN</p></div>
    <div class="colors ORANGE"><p class="color-text">ORANGE</p></div>

.. raw:: html

   <div style="margin-top: 27em;"></div>

另外，在pycharm编辑器中颜色会警告，可以调小警告等级。
在vscode中如果你安装了python扩展也会发出警告，其原因是vscode在检测变量时并不会识别在运行时添加的变量，
所以需要将COLOR_MAP中的颜色提取出来作为常量令vscode识别。你需要注释这两行代码：

.. code:: python

   # for name in [s for s in list(COLOR_MAP.keys()) if s.endswith("_C")]:
   #     locals()[name.replace("_C", "")] = locals()[name]

并将下方代码复制在constants.py中：

.. code:: python

   DARK_BLUE = "#236B8E"
   DARK_BROWN = "#8B4513"
   LIGHT_BROWN = "#CD853F"
   BLUE_E = "#1C758A"
   BLUE_D = "#29ABCA"
   BLUE_C = "#58C4DD"
   BLUE_B = "#9CDCEB"
   BLUE_A = "#C7E9F1"
   TEAL_E = "#49A88F"
   TEAL_D = "#55C1A7"
   TEAL_C = "#5CD0B3"
   TEAL_B = "#76DDC0"
   TEAL_A = "#ACEAD7"
   GREEN_E = "#699C52"
   GREEN_D = "#77B05D"
   GREEN_C = "#83C167"
   GREEN_B = "#A6CF8C"
   GREEN_A = "#C9E2AE"
   YELLOW_E = "#E8C11C"
   YELLOW_D = "#F4D345"
   YELLOW_C = "#FFFF00"
   YELLOW_B = "#FFEA94"
   YELLOW_A = "#FFF1B6"
   GOLD_E = "#C78D46"
   GOLD_D = "#E1A158"
   GOLD_C = "#F0AC5F"
   GOLD_B = "#F9B775"
   GOLD_A = "#F7C797"
   RED_E = "#CF5044"
   RED_D = "#E65A4C"
   RED_C = "#FC6255"
   RED_B = "#FF8080"
   RED_A = "#F7A1A3"
   MAROON_E = "#94424F"
   MAROON_D = "#A24D61"
   MAROON_C = "#C55F73"
   MAROON_B = "#EC92AB"
   MAROON_A = "#ECABC1"
   PURPLE_E = "#644172"
   PURPLE_D = "#715582"
   PURPLE_C = "#9A72AC"
   PURPLE_B = "#B189C6"
   PURPLE_A = "#CAA3E8"
   WHITE = "#FFFFFF"
   BLACK = "#000000"
   LIGHT_GRAY = "#BBBBBB"
   LIGHT_GREY = "#BBBBBB"
   GRAY = "#888888"
   GREY = "#888888"
   DARK_GREY = "#444444"
   DARK_GRAY = "#444444"
   DARKER_GREY = "#222222"
   DARKER_GRAY = "#222222"
   GREY_BROWN = "#736357"
   PINK = "#D147BD"
   LIGHT_PINK = "#DC75CD"
   GREEN_SCREEN = "#00FF00"
   ORANGE = "#FF862F"
   BLUE = "#58C4DD"
   TEAL = "#5CD0B3"
   GREEN = "#83C167"
   YELLOW = "#FFFF00"
   GOLD = "#F0AC5F"
   RED = "#FC6255"
   MAROON = "#C55F73"
   PURPLE = "#9A72AC"

