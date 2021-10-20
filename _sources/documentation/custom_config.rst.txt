默认配置 custom_config
=======================

``directories``
---------------

- ``mirror_module_path``
    （``True`` 或者 ``False``）是否在 ``output`` 路径下创建名为运行文件的名的文件夹，
    并在其中保存输出（``images/`` 或 ``videos/``）

- ``output``
    输出文件路径，视频会保存在其下 ``videos/`` 文件夹中，图片会保存在其下 ``images/`` 文件夹中

    例如，如果你把 ``output`` 设置为 ``"/.../manim/output"`` ，把 
    ``mirror_module_path`` 设置为 ``False``, 之后导出代码中的 ``Scene1`` 
    视频和最后一帧, 最后的目录结构将是:

    .. code-block:: text
        :emphasize-lines: 9, 11

            manim/
            ├── manimlib/
            │   ├── animation/
            │   ├── ...
            │   ├── default_config.yml
            │   └── window.py
            ├── output/
            │   ├── images
            │   │   └── Scene1.png
            │   └── videos
            │       └── Scene1.mp4
            ├── code.py
            └── custom_config.yml

    但是如果你把 ``mirror_module_path`` 设置为 ``True``, 目录结构则将是:

    .. code-block:: text
        :emphasize-lines: 8

            manim/
            ├── manimlib/
            │   ├── animation/
            │   ├── ...
            │   ├── default_config.yml
            │   └── window.py
            ├── output/
            │   └── code/
            │       ├── images
            │       │   └── Scene1.png
            │       └── videos
            │           └── Scene1.mp4
            ├── code.py
            └── custom_config.yml

- ``raster_images`` 
    存放代码中要使用的像素图像（包括 ``.jpg``，``.jpeg``，`` .png`` 和 ``.gif``）的目录，
    将由 ``ImageMobject`` 读取

- ``vector_images``
    存放代码中要使用的矢量图像（包括 ``.svg`` 和 ``.xdv``）的目录，将由 ``SVGMobject`` 读取

- ``sounds``
    存放代码中要使用的声音文件（包括 ``.wav`` 和 ``.mp3``）的目录，使用 ``Scene.add_sound()`` 读取 .

- ``temporary_storage``
    存储临时产生的缓存文件的目录，包含 ``Tex`` 的缓存、``Text`` 的缓存和物体点集的存储

``tex``
-------

- ``executable``
    编译LaTeX使用的可执行程序（推荐 ``latex`` 或 ``xelatex -no-pdf``）

- ``template_file``
    使用的LaTeX模板，在 ``manimlib/tex_templates`` 中

- ``intermediate_filetype``
    编译后产生的中间矢量文件的类型（若使用 ``latex`` 则为 ``dvi``，若使用 ``xelatex`` 即为 ``xdv``）
    
- ``text_to_replace``
    模板中待替换的文字（默认即可）

``universal_import_line``
-------------------------

在直接进入交互模式下需要引入包的语句

``style``
---------

- ``font`` 
    ``Text`` 的默认字体

- ``background_color``
    默认背景颜色

``window_position``
-------------------

反馈窗口在显示器上的相对位置（两个字母，第一个字母表示 上U/中O/下D，第二个字母表示 左L/中O/右R）

``window_monitor``
------------------

反馈窗口出现的显示器的编号

``break_into_partial_movies``
-----------------------------

是否在导出视频的时候为每个 self.play 和 self.wait 生成一个视频片段

设为 ``True`` 方便后期剪辑，设为 ``False`` 速度更快效率更高


``camera_qualities``
--------------------

导出质量

- ``low``
    低质量（默认 480p15）

- ``medium``
    中等质量（默认 720p30）

- ``high``
    高质量（默认 1080p30）

- ``ultra_high``
    超高质量（默认 4K60）

- ``default_quality``
    默认质量（选填以上四种之一）