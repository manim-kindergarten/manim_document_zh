Manim结构
=================


Manim目录结构
---------------------------

manim的目录看起来很复杂，文件很多，但是结构非常清晰

下面是manim的目录结构：

.. code-block:: text

    manimlib/ # manim库
    ├── __init__.py
    ├── __main__.py
    ├── default_config.yml   # 默认配置文件
    ├── config.py            # 在这里处理命令传入的参数
    ├── constants.py         # 一些定义的常量
    ├── extract_scene.py     # 提取、运行场景
    ├── shader_wrapper.py    # Shader包装器
    ├── window.py            # 反馈窗口
    ├── tex_templates/ # LaTeX模板
    │   ├── tex_templates.tex   # tex模板(将使用latex编译，默认)
    │   └── ctex_templates.tex  # 支持中文的tex模板(将使用xelatex编译)
    ├── camera/ # 相机
    │   └── camera.py        # 包括Camera和CameraFrame
    ├── scene/ # 场景
    │   ├── scene_file_writer.py     # 用于将scene写入视频文件
    │   ├── scene.py                 # 最普通的场景
    │   ├── three_d_scene.py         # 三维场景
    │   ├── sample_space_scene.py    # 概率相关的样本空间场景
    │   └── vector_space_scene.py    # 向量场场景
    ├── animation/ # 动画
    │   ├── animation.py     # 动画的基类
    │   ├── composition.py   # 动画组
    │   ├── creation.py      # 和Create有关的动画
    │   ├── fading.py        # 和Fade有关的动画
    │   ├── growing.py       # 和Grow有关的动画
    │   ├── indication.py    # 一些用于强调的动画
    │   ├── movement.py      # 和移动有关的动画
    │   ├── numbers.py       # 实现对DecimalNumber数字的变化
    │   ├── rotation.py      # 和旋转有关的动画
    │   ├── specialized.py   # 一些针对特殊项目的不常用动画
    │   ├── transform_matching_parts.py # 自动匹配部分的Transform
    │   ├── transform.py     # 一些Transform变换
    │   └── update.py        # # 从函数实现update
    ├── mobject/ # 数学物品
    │   ├── mobject.py       # 所有mobject的父类
    │   ├── types/ # 4种子类mobject
    │   │   ├── dot_cloud.py            # Dot cloud (PMobject的一个子类)
    │   │   ├── image_mobject.py        # 插入图片
    │   │   ├── point_cloud_mobject.py  # PMobject (点集构成的mobject)
    │   │   ├── surface.py              # ParametricSurface
    │   │   └── vectorized_mobject.py   # VMobject (向量化的mobject)
    │   ├── svg/ # 和svg有关的mobject
    │   │   ├── svg_mobject.py          # SVGMobject
    │   │   ├── brace.py                # 大括号
    │   │   ├── drawings.py             # svg图像的一些特殊mobject
    │   │   ├── tex_mobject.py          # 依赖LaTeX实现的文字
    │   │   └── text_mobject.py         # 依赖cairo实现的文字
    │   ├── changing.py             # 动态变化的mobject
    │   ├── coordinate_systems.py   # 坐标系统
    │   ├── frame.py                # 和frame有关的mobject
    │   ├── functions.py            # 参数方程
    │   ├── geometry.py             # 几何图形的mobject
    │   ├── matrix.py               # 矩阵
    │   ├── mobject_update_utils.py # 一些定义的更新程序
    │   ├── number_line.py          # 数轴
    │   ├── numbers.py              # 可以变化的数字
    │   ├── probability.py          # 和概率有关的mobject
    │   ├── shape_matchers.py       # 适应其它物体大小的mobject
    │   ├── three_dimensions.py     # 三维物体
    │   ├── value_tracker.py        # ValueTracker(存储数的mobject)
    │   └── vector_field.py         # 向量场 
    ├── once_useful_constructs/  # 3b1b为某些视频写的常用场景
    │   └── ...
    ├── shaders/ # 渲染中使用的GLSL脚本
    │   ├── simple_vert.glsl    # 一个简单的对位置的glsl脚本
    │   ├── insert/ # 需要插入到其他脚本中的脚本片段
    │   │   ├── NOTE.md   # 描述了如何插入脚本
    │   │   └── ...       # 一些常用的脚本
    │   ├── image/ # 针对图像的glsl
    │   │   └── ... # 包含vertex shader和fragment shader
    │   ├── quadratic_bezier_fill/ # 针对二阶贝塞尔填充的glsl
    │   │   └── ... # 包含vertex shader、fragment shader和geometry shader
    │   ├── quadratic_bezier_stroke/ # 针对二阶贝塞尔线条的glsl
    │   │   └── ... # 包含vertex shader、fragment shader和geometry shader
    │   ├── surface/ # 针对三维面的glsl
    │   │   └── ... # 包含vertex shader和fragment shader
    │   ├── textured_surface/ # 针对纹理面的glsl
    │   │   └── ... # 包含vertex shader和fragment shader
    │   └── true_dot/ # 对于一个点的glsl
    │       └── ... # 包含vertex shader、fragment shader和geometry shader
    └── utils/ # 一些实用的工具函数
        ├── bezier.py             # 贝塞尔曲线
        ├── color.py              # 颜色
        ├── config_ops.py         # 处理CONFIG
        ├── customization.py      # 读取custom_config.yml
        ├── debug.py              # 在程序中debug的函数
        ├── directories.py        # 读取配置文件中目录相关内容
        ├── family_ops.py         # 处理family成员
        ├── file_ops.py           # 处理文件目录
        ├── images.py             # 读取图片
        ├── init_config.py        # 自动配置指南
        ├── iterables.py          # 和列表字典处理有关的函数
        ├── paths.py              # 路径
        ├── rate_functions.py     # 一些定义的rate_function
        ├── simple_functions.py   # 一些常用函数
        ├── sounds.py             # 处理声音
        ├── space_ops.py          # 空间坐标计算
        ├── strings.py            # 处理字符串
        └── tex_file_writing.py   # 将字符串利用LaTeX写成svg

Manim的类继承结构
----------------------------------------

`这里 <https://github.com/3b1b/manim/files/5824383/manim_shaders_structure.pdf>`_ 
整理了一个manim类继承的pdf，比较大，但是基本所有的类都有包含：

.. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/manim_shaders_structure.png

Manim运行过程
-----------------------

.. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/manim_shaders_process_cn.png
