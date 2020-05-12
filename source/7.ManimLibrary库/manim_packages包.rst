Manim packages库包
====================

.. admonition:: 声明

    这页内容是elteoremadebeethoven写的 `manim_3feb_docs <https://github.com/Elteoremadebeethoven/manim_3feb_docs.github.io/tree/master/source>`_ 我翻译+manim版本更新+做笔记，把资料整合编辑成方便的文档格式，以方便查阅使用Manim。




Ubication位置
---------------------------

导入包All packages of this version are in::

    manimlib/imports.py


.. literalinclude:: ../manimlib/imports.py
    :linenos:


Tree文件树
------------

The files that we really need are:

* ``manimlib/imports.py``
* ``manimlib/``
* ``manim.py``
* ``stage_scenes.py``

The rest files we can delete it.不需要的东西可以删除，但是修改删除前记得备份，或者git恢复。

::

    │  config.py
    │  constants.py        # manimlab/constants.py设置更多常量
    │  ctex_template.tex   # 中文设置可以先试试LaTeX运行模板，测试能否正常生成中文
    │  tex_template.tex
    ├── README.md          # <- Don't needed
    ├── requirements.txt   # <- 安装需要的库时用
    ├── LICENSE            # <- Don't needed
    │  docker-compose.yml  # <- Docker安装时使用
    │  Dockerfile
    │  environment.yml
    ├── example_scenes.py  # <- Don't needed
    │  extract_scene.py
    │  manim.py
    │  media_dir.txt       # 可以新建文件media_dir.txt在这里设置视频保存路径，可以是绝对路径：C:\manim\media\。也可以在常量py文件中配置，或者manimlib/scene/media_dir.txt中设置
    |  perf_scenes.py    
    │  setup.cfg
    │  setup.py
    │  stage_scenes.py
    │  stream_starter.py
    │  __init__.py
    │
    ├─animation
    │  │  animation.py
    │  │  composition.py
    │  │  creation.py
    │  │  fading.py
    │  │  growing.py
    │  │  indication.py
    │  │  movement.py
    │  │  numbers.py
    │  │  rotation.py
    │  │  specialized.py
    │  │  transform.py
    │  │  update.py
    │  │
    │  └─__pycache__
    │          animation.cpython-37.pyc # pyc文件是py文件对应编译后生成的字节码文件(byte code)，加载运行快点，也能让商业软件保密，这里为了查看整洁的代码文件树，在后续的目录树中的删*。pyc掉。
    │
    ├─camera
    │  │  camera.py
    │  │  mapping_camera.py
    │  │  moving_camera.py
    │  │  multi_camera.py
    │  └─  three_d_camera.py
    │  
    │
    ├─container
    │  └─container.py
    │
    │
    ├─for_3b1b_videos
    │  │  
    │  │common_scenes.py
    │  │  pi_class.py
    │  │  pi_creature.py
    │  │  pi_creature_animations.py
    │  └─ pi_creature_scene.py
    │
    ├─mobject
    │  │  changing.py
    │  │  coordinate_systems.py
    │  │  frame.py
    │  │  functions.py
    │  │  geometry.py
    │  │  matrix.py
    │  │  mobject.py
    │  │  mobject_update_utils.py
    │  │  numbers.py
    │  │  number_line.py
    │  │  probability.py
    │  │  shape_matchers.py
    │  │  three_dimensions.py
    │  │  three_d_shading_utils.py
    │  │  three_d_utils.py
    │  │  value_tracker.py
    │  │  vector_field.py
    │  │
    │  ├─svg
    │  │  │  
    │  │  │  brace.py
    │  │  │  drawings.py
    │  │  │  svg_mobject.py
    │  │  │  text_mobject.py
    │  │  └─ tex_mobject.py
    │  │
    │  └─ types
    │     │  
    │     │  image_mobject.py
    │     │  point_cloud_mobject.py
    │     └─  vectorized_mobject.py
    │  
    │
    ├─once_useful_constructs
    │  │  arithmetic.py
    │  │  combinatorics.py
    │  │  complex_transformation_scene.py
    │  │  counting.py
    │  │  fractals.py
    │  │  graph_theory.py
    │  │  light.py
    │  │  matrix_multiplication.py
    │  │  NOTE.md
    │  └─  region.py
    │
    ├─scene
    │  │  
    │  │
    │  |  graph_scene.py
    │  │  media_dir.txt
    │  │  moving_camera_scene.py
    │  │  reconfigurable_scene.py
    │  │  sample_space_scene.py
    │  │  scene.py
    │  │  scene_file_writer.py
    │  │  scene_from_video.py
    │  │  three_d_scene.py
    │  │  vector_space_scene.py
    │  └─ zoomed_scene.py
    │
    ├─utils
    │  │  
    │  │
    │  |  bezier.py
    │  │  color.py
    │  │  config_ops.py
    │  │  debug.py
    │  │  file_ops.py
    │  │  images.py
    │  │  iterables.py
    │  │  paths.py
    │  │  rate_functions.py
    │  │  simple_functions.py
    │  │  sounds.py
    │  │  space_ops.py
    │  │  strings.py
    │  └─ tex_file_writing.py
    │
    └─__pycache__
            config.cpython-37.pyc
            constants.cpython-37.pyc
            extract_scene.cpython-37.pyc
            imports.cpython-37.pyc
            manim.cpython-37.pyc
            stream_starter.cpython-37.pyc
            __init__.cpython-37.pyc 
            # __init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。导入一个包时，实际上是导入了它的__init__.py文件。这样可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。
            #模块通常为单独的.py文件，可以用import直接引用，可以作为模块的文件类型有.py、.pyo、.pyc、.pyd、.so、.dll
            #import语句引入机制可以导入的对象类型:模块文件（.py文件）C或C++扩展（已编译为共享库或DLL文件）包（包含多个模块）内建模块（使用C编写并已链接到Python解释器中）

You can delete ``README.md``, ``requirements.txt``, ``Dockerfile``, ``example_scenes.py`` and ``LICENSE``.

..