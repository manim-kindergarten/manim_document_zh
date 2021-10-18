变更
===========

尚未发布
----------

BUG 修复 
^^^^^^^^^^

- `#1653 <https://github.com/3b1b/manim/pull/1653>`__: 修复 ``Mobject.stretch_to_fit_depth``

新特性
^^^^^^^^^^^^

- `e10f850 <https://github.com/3b1b/manim/commit/e10f850d0d9f971931cc85d44befe67dc842af6d>`__: 添加命令行参数 ``--log-level`` 以指定日志级别


v1.2.0
------

BUG 修复
^^^^^^^^^^

- `#1592 <https://github.com/3b1b/manim/pull/1592>`__: 修复 3D ``put_start_and_end_on``
- `#1601 <https://github.com/3b1b/manim/pull/1601>`__: 修复 ``DecimalNumber`` 在缩放大小时的问题
- `56df154 <https://github.com/3b1b/manim/commit/56df15453f3e3837ed731581e52a1d76d5692077>`__: 修复所有 ``CoordinateSystem`` 使用通用范围数组的错误
- `8645894 <https://github.com/3b1b/manim/commit/86458942550c639a241267d04d57d0e909fcf252>`__: 修复 ``CoordinateSystem`` 初始化问题
- `0dc096b <https://github.com/3b1b/manim/commit/0dc096bf576ea900b351e6f4a80c13a77676f89b>`__: 修复单值 ``ValueTracker`` 的 bug
- `54ad355 <https://github.com/3b1b/manim/commit/54ad3550ef0c0e2fda46b26700a43fa8cde0973f>`__: 修复 SVG rectangles 的 bug
- `d45ea28 <https://github.com/3b1b/manim/commit/d45ea28dc1d92ab9c639a047c00c151382eb0131>`__: 修复 ``DotCloud.set_radii``
- `b543cc0 <https://github.com/3b1b/manim/commit/b543cc0e32d45399ee81638b6d4fb631437664cd>`__: 暂时修复 ``PMobject`` 数组重置大小的 bug
- `5f878a2 <https://github.com/3b1b/manim/commit/5f878a2c1aa531b7682bd048468c72d2835c7fe5>`__: 修复 ``match_style``
- `719c81d <https://github.com/3b1b/manim/commit/719c81d72b00dcf49f148d7c146774b22e0fe348>`__: 修复 ``path_arc`` 为负数的情况
- `c726eb7 <https://github.com/3b1b/manim/commit/c726eb7a180b669ee81a18555112de26a8aff6d6>`__: 修复 ``CoordinateSystem.get_lines_parallel_to_axis``
- `7732d2f <https://github.com/3b1b/manim/commit/7732d2f0ee10449c5731499396d4911c03e89648>`__: 修复 ``ComplexPlane`` -i 显示 bug

新特性
^^^^^^^^^^^^

- `#1598 <https://github.com/3b1b/manim/pull/1598>`__: ``SVGMobject`` 支持椭圆弧命令 ``A``
- `#1607 <https://github.com/3b1b/manim/pull/1607>`__: 新增 :class:`~manimlib.animation.indication.FlashyFadeIn`
- `#1607 <https://github.com/3b1b/manim/pull/1607>`__: 保存三角剖分
- `#1625 <https://github.com/3b1b/manim/pull/1625>`__: 添加新的 ``Code`` 物件
- `#1637 <https://github.com/3b1b/manim/pull/1637>`__: 添加警告部分并使用 ``rich`` 模块显示日志
- `bd356da <https://github.com/3b1b/manim/commit/bd356daa99bfe3134fcb192a5f72e0d76d853801>`__: 添加 ``VCube``
- `6d72893 <https://github.com/3b1b/manim/commit/6d7289338234acc6658b9377c0f0084aa1fa7119>`__: 支持 ``ValueTracker`` 追踪向量
- `3bb8f3f <https://github.com/3b1b/manim/commit/3bb8f3f0422a5dfba0da6ef122dc0c01f31aff03>`__: 给 ``Mobject`` 添加了 ``set_max_width``, ``set_max_height``, ``set_max_depth``
- `a35dd5a <https://github.com/3b1b/manim/commit/a35dd5a3cbdeffa3891d5aa5f80287c18dba2f7f>`__: 添加 ``TracgTail`` 自动减淡追踪路径
- `acba13f <https://github.com/3b1b/manim/commit/acba13f4991b78d54c0bf93cce7ca3b351c25476>`__: 添加 ``Scene.point_to_mobject``
- `f84b8a6 <https://github.com/3b1b/manim/commit/f84b8a66fe9e8b3872e5c716c5c240c14bb555ee>`__: 添加 poly_fractal 材质
- `b24ba19 <https://github.com/3b1b/manim/commit/b24ba19dec48ba4e38acbde8eec6d3a308b6ab83>`__: 给 ``TipableVMobject.set_length`` 添加参数
- `17c2772 <https://github.com/3b1b/manim/commit/17c2772b84abf6392a4170030e36e981de4737d0>`__: 添加 ``Mobject.replicate``
- `33fa76d <https://github.com/3b1b/manim/commit/33fa76dfac36e70bb5fad69dc6a336800c6dacce>`__: 添加 mandelbrot 分形材质
- `f22a341 <https://github.com/3b1b/manim/commit/f22a341e8411eae9331d4dd976b5e15bc6db08d9>`__: 在每次 embed 前保存状态
- `e10a752 <https://github.com/3b1b/manim/commit/e10a752c0001e8981038faa03be4de2603d3565f>`__: 允许释放纹理
- `14fbed7 <https://github.com/3b1b/manim/commit/14fbed76da4b493191136caebb8a955e2d41265b>`__: 合并并重命名 newton_fractal shader
- `6cdbe0d <https://github.com/3b1b/manim/commit/6cdbe0d67a11ab14a6d84840a114ae6d3af10168>`__: ``ImageMoject`` 保存图像的文件路径

重构
^^^^^^^^

- `#1601 <https://github.com/3b1b/manim/pull/1601>`__: ``Mobject.scale`` 改为更简单的实现
- `b667db2 <https://github.com/3b1b/manim/commit/b667db2d311a11cbbca2a6ff511d2c3cf1675486>`__: 简化 ``Square``
- `40290ad <https://github.com/3b1b/manim/commit/40290ada8343f10901fa9151cbdf84689667786d>`__: 移除未使用的参数 ``triangulation_locked``
- `8647a64 <https://github.com/3b1b/manim/commit/8647a6429dd0c52cba14e971b8c09194a93cfd87>`__: 重构 ``Arrow`` （为啥又重构了）
- `d8378d8 <https://github.com/3b1b/manim/commit/d8378d8157040cd797cc47ef9576beffd8607863>`__: 使用 ``make_approximately_smooth`` 作为 ``set_points_smoothly`` 的默认值
- `7b4199c <https://github.com/3b1b/manim/commit/7b4199c674e291f1b84678828b63b6bd4fcc6b17>`__: 重构了 ``_handle_scale_side_effects``，在缩放后调用以解决一些遗留的问题
- `7356a36 <https://github.com/3b1b/manim/commit/7356a36fa70a8279b43ae74e247cbd43b2bfd411>`__: ``get_start_and_end`` 抛出异常时只调用一次 ``throw_error_if_no_points``
- `0787c4f <https://github.com/3b1b/manim/commit/0787c4f36270a6560b50ce3e07b30b0ec5f2ba3e>`__: 确保预览场景的帧率为 30
- `c635f19 <https://github.com/3b1b/manim/commit/c635f19f2a33e916509e53ded46f55e2afa8f5f2>`__: 将 ``pixel_coords_to_space_coords`` 方法移动到 ``Window`` 中
- `d5a88d0 <https://github.com/3b1b/manim/commit/d5a88d0fa457cfcf4cb9db417a098c37c95c7051>`__: 给 uniforms 变量传递 ``tuple`` 而不是 ``array``
- `9483f26 <https://github.com/3b1b/manim/commit/9483f26a3b056de0e34f27acabd1a946f1adbdf9>`__:  重构 ``Mobject.copy`` 中 uniform 数组的拷贝
- `ed1fc4d <https://github.com/3b1b/manim/commit/ed1fc4d5f94467d602a568466281ca2d0368b506>`__:  从点云图物件（ PointCloud Mobject ）中排除 ``bounding_box`` 关键字
- `329d2c6 <https://github.com/3b1b/manim/commit/329d2c6eaec3d88bfb754b555575a3ea7c97a7e0>`__: 确保轮廓线宽度（ stroke width ）为浮点数


v1.1.0
-------

Bug 修复
^^^^^^^^^^

- 修复了当 ``length=0`` 时 :func:`~manimlib.utils.iterables.resize_with_interpolation` 的bug
- 修复了 :class:`~manimlib.mobject.geometry.Elbow` 中 ``__init__`` 的错误用法
- 无法选择显示器时使用存在的显示器
- 确保 ``mobject.data`` 在每个动画结束后锁定
- 修复了中心不在原点的向量场出现的bug
- 使 ``Mobject.match_points`` 返回自身 ``self``
- 修复了 ``example_scenes.py`` 中的 ``AnimatingMethods``

新特性
^^^^^^^^^^^^

- 新增了 :class:`~manimlib.animation.indication.VShowPassingFlash`
- 新增了 ``COLORMAP_3B1B``
- 新增了一些获取坐标系统所有轴范围和中心的方法
  
  - :meth:`~manimlib.mobject.coordinate_systems.CoordinateSystem.get_origin`
  - :meth:`~manimlib.mobject.coordinate_systems.CoordinateSystem.get_all_ranges`
- 新增了 :meth:`~manimlib.mobject.mobject.Mobject.set_color_by_rgba_func`
- 更新了 :class:`~manimlib.mobject.vector_field.VectorField` 和 :class:`~manimlib.mobject.vector_field.StreamLines`
- 允许 ``3b1b_colormap`` 作为 :func:`~manimlib.utils.color.get_colormap_list` 的一个选项
- 使 ``stroke_width`` 返回一个一维数组（支持可变线宽）
- 新增了 :meth:`~manimlib.mobject.svg.text_mobject.Text.get_parts_by_text`
- ``Brace`` 使用 ``Text`` 而非 ``TexText``
- 更新 ``Cross`` 默认使用可变线宽
- 新增了 :class:`~manimlib.animation.indication.FlashAround` and :class:`~manimlib.animation.indication.FlashUnder`
- 允许向 ``Brace.get_text`` 中传入 ``Text`` 的配置
- 新增了 :meth:`~manimlib.camera.camera.CameraFrame.reorient` 来快速设定相机角度
- 为 :meth:`~manimlib.camera.camera.CameraFrame.set_euler_angles` 新增了单位参数 ``units``
- 允许任何 ``VMobject`` 传入 ``TransformMatchingTex``
- 删除了 ``Tex`` 和 ``TexText`` 中双大括号自动分割的用法