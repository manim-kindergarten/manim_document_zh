Manim Constants常量
=====================
.. admonition:: 声明

   这一页是EulerTour写的教程,整合elteoremadebeethoven写的 `manim_3feb_docs <https://github.com/Elteoremadebeethoven/manim_3feb_docs.github.io/tree/master/source>`_  我翻译+做笔记，把资料整合编辑成方便的文档格式，以方便查阅使用Manim。

编辑manimlib/constants.py相关定义即可。
The ``constants.py`` under ``manimlib/`` contains variables that are used
during setup and running manim. Some variables are not documented here as they are
only used internally by manim.

Directories配置目录
----------------------

    MEDIA_DIR
              The directory where ``VIDEO_DIR`` and ``TEX_DIR`` will be created,
              if they aren't specified via flags.
    VIDEO_DIR
              Used to store the scenes rendered by Manim. When a scene is
              finished rendering, it will be stored under
              ``VIDEO_DIR/module_name/scene_name/quality/scene_name.mp4``.
              Created under ``MEDIA_DIR`` by default.
    TEX_DIR
              Files written by Latex are stored here. It also acts as a cache
              so that the files aren't rewritten each time Latex is needed.

Those directories are created if they don't exist.运行一次看文件就知道怎么回事了。


When you run an animation for first time you can see this message::

    Media will be stored in media/. You can change this behavior by writing a different directory to media_dir.txt.

That is because the animation file has been saved in a directory called ``media``, in the manim directory, then you have a new directory and two new files:

::

    .
    ├── manim/imports.py
    ├── manim.py
    ├── stage_scenes.py 
    ├── media              # <- New directory
    ├── media_dir.txt      # <- New file
    └── manimlib
        └── media_dir.txt  # <- New file

You should have not to see that message again, but, in case that you see it again, then you can change the content of the ``media_dir.txt`` files with ``/`` and change the line 14 of ``manimlib/constants.py``:

.. literalinclude:: ./manimlib/constants.py
    :lines: 4-53
    :lineno-start: 4
    :emphasize-lines: 26

with:

.. code-block:: python
    :lineno-start: 23

            "/"

方法很多，可以新建文件media_dir.txt在这里设置视频保存路径，可以是绝对路径：C:\\manim\\media。也可以在常量py文件中配置，或者manimlib/scene/media_dir.txt中设置。

If you want to learn how change the ``media`` directory see:

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/I9rHHiKqTWY?rel=0" frameborder="0" allowfullscreen></iframe>

Resolution
----------
分辨率

.. literalinclude:: ./manimlib/constants.py
    :lines: 116-141
    :lineno-start: 116

Frame dimensions
----------------

默认横七（\* 2）竖八

.. literalinclude:: ./manimlib/constants.py
    :lines: 141-155
    :lineno-start: 141

Buffs
-----

.. literalinclude:: ./manimlib/constants.py
    :lines: 155-163
    :lineno-start: 155



Tex配置文本
---------------

    TEX_USE_CTEX
              A boolean value. Change it to True if you need to use Chinese typesetting.
    TEX_TEXT_TO_REPLACE
              Placeholder text used by manim when generating tex files
    TEMPLATE_TEX_FILE
              By default ``manimlib/tex_template.tex`` is used. If ``TEX_USE_CTEX``
              is set to True then ``manimlib/ctex_template.tex`` is used.

Numerical Constants数值常量
------------------------------

编辑manimlib/constants.py相关定义，即可添加自己常用的的数学常量。
    PI
            alias to ``numpy.pi``
    TAU
            PI * 2

    DEGREES
            TAU / 360

Camera Configuration配置相机
-----------------------------------------

Render setting presets

    PRODUCTION_QUALITY_CAMERA_CONFIG
            2560x1440 @ 60fps # This is the default when rendering a scene默认
    HIGH_QUALITY_CAMERA_CONFIG
            1920x1080 @ 60fps. # Used when the ``-h`` or ``--high_quality`` flag
            is passed.
    MEDIUM_QUALITY_CAMERA_CONFIG
            1280x720 @ 30fps. # Used when the ``-m`` or ``--medium_quality``
            flag is passed.
    LOW_QUALITY_CAMERA_CONFIG
            854x480 @ 15fps. # Used when the ``-l`` or ``--low_quality`` flag is
            passed.

.. _ref-directions:


Coordinates坐标Vectors
-------------------------

.. literalinclude:: ./manimlib/constants.py
    :lines: 169-191
    :lineno-start: 169


Used for 2d/3d animations and placements::

    ORIGIN#中心
    UP#上np.array((0., 1., 0.))
    DOWN#下
    RIGHT#右
    LEFT#左
    IN # 3d camera only, away from camera，np.array((0., 0., -1.))
    OUT # 3d camera only, close to camera，np.array((0., 0., 1.))

    UL = UP + LEFT #左上 diagonal abbreviations对角缩写. You can use either one
    UR = UP + RIGHT#右上
    DL = DOWN + LEFT#左下
    DR = DOWN + RIGHT#右下

    TOP #上边界FRAME_Y_RADIUS * UP
    BOTTOM #下边界
    LEFT_SIDE 
    RIGHT_SIDE``

Color palette
-------------------

编辑manimlib/constants.py相关定义即可，任意色彩的16进制可以随便找在线工具取色器。
    COLOR_MAP
            A predefined color maps
    PALETTE
            A list of color hex strings, derived from COLOR_MAP


.. raw:: html

    <a href="./_static/html/colors.html"> Check this page </a> to see the color palette.

.. note::
    
    ``COLOR = COLOR_C``

.. literalinclude:: ./manimlib/constants.py
    :lines: 197-258
    :lineno-start: 197

..

