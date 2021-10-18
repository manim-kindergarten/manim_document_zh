变更
===========

尚未发布
----------

Bug修复
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