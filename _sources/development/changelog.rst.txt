变更
===========

v1.6.1
------

修复 Bug
^^^^^^^^^^
- 修复 ``MTex`` 多行 tex 的 bug (`#1785 <https://github.com/3b1b/manim/pull/1785>`__)
- 修复 ``interpolate`` (`#1788 <https://github.com/3b1b/manim/pull/1788>`__)
- 修复 ``ImageMobject`` (`#1791 <https://github.com/3b1b/manim/pull/1791>`__)

重构
^^^^^^^^
- 将 ``\overset`` 作为 ``Tex`` 的一个特殊的符号 (`#1783 <https://github.com/3b1b/manim/pull/1783>`__)
- 添加 ``outer_interpolate`` 方法对数组使用 ``np.outer`` 方法 (`#1788 <https://github.com/3b1b/manim/pull/1788>`__)

v1.6.0
------

Breaking changes
^^^^^^^^^^^^^^^^
- **Python 3.6 不再支持** (`#1736 <https://github.com/3b1b/manim/pull/1736>`__)

修复 Bug
^^^^^^^^^^
- 修复黎曼矩形的宽度问题 (`#1762 <https://github.com/3b1b/manim/pull/1762>`__)
- 修复空数组传入 shader 的 bug (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/fa38b56fd87f713657c7f778f39dca7faf15baa8>`__)
- 修复 ``AddTextWordByWord`` (`#1772 <https://github.com/3b1b/manim/pull/1772>`__)
- 修复 ``ControlsExample`` (`#1781 <https://github.com/3b1b/manim/pull/1781>`__)


新 Bug
^^^^^^^^^^^^
- 给 ``Text`` 添加了更多方法 (details: `#1751 <https://github.com/3b1b/manim/pull/1751>`__)
- 允许 ``interpolate`` 作用于一组 alpha 上 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/bf2d9edfe67c7e63ac0107d1d713df7ae7c3fb8f>`__)
- 允许 ``Numberline.number_to_point`` 和 ``CoordinateSystem.coords_to_point`` 方法作用于一系列的输入 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/c3e13fff0587d3bb007e71923af7eaf9e4926560>`__)
- 添加基本图形 ``Prismify``，将平面图形 ``VMobject`` 转变为带有深度的图形 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/f249da95fb65ed5495cd1db1f12ece7e90061af6>`__)
- 添加 ``GlowDots``,  与 ``GlowDot`` 类似 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/e19f35585d817e74b40bc30b1ab7cee84b24da05>`__)
- 添加 ``TransformMatchingStrings`` 动画类，同时适用于 ``Text`` 和 ``MTex`` (`#1772 <https://github.com/3b1b/manim/pull/1772>`__)
- 给 ``LabelledString.get_parts_by_string`` 添加 ``substring`` 和 ``case_sensitive`` 的参数支持 (`#1780 <https://github.com/3b1b/manim/pull/1780>`__) 


重构
^^^^^^^^
- 添加类型提示 (`#1736 <https://github.com/3b1b/manim/pull/1736>`__)
- 指定 tex 文件的 UTF-8 编码 (`#1748 <https://github.com/3b1b/manim/pull/1748>`__)
- 使用最新版 manimpango 重构 ``Text`` (`#1751 <https://github.com/3b1b/manim/pull/1751>`__)
- 对 ``ParametricCurve`` 的 getter 进行重组 (`#1757 <https://github.com/3b1b/manim/pull/1757>`__)
- 使用 ``scipy.spatial.transform.Rotation`` 重构 ``CameraFrame`` (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/625460467fdc01fc1b6621cbb3d2612195daedb9>`__)
- 使用 ``scipy.spatial.transform.Rotation`` 重构 ``CameraFrame`` 的旋转方法 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/7bf3615bb15cc6d15506d48ac800a23313054c8e>`__)
- 使用 ``stroke_color`` 来初始化 ``Arrow`` 的颜色 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/c0b7b55e49f06b75ae133b5a810bebc28c212cd6>`__)
- 重构 ``Mobject.set_rgba_array_by_color`` (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/8b1f0a8749d91eeda4b674ed156cbc7f8e1e48a8>`__)
- 使平移对鼠标移动更敏感 (`#1764 <https://github.com/3b1b/manim/pull/1764/commits/9d0cc810c5fcb4252990e706c6bf880d571cb1a2>`__)
- 增加了大型 SVG 图片的加载进度 (`#1766 <https://github.com/3b1b/manim/pull/1766>`__)
- 为 ``CameraFrame`` 添加了 ``field_of_view`` 的 getter/setter (`#1770 <https://github.com/3b1b/manim/pull/1770/commits/0610f331a4f7a126a3aae34f8a2a86eabcb692f4>`__)
- 重命名 ``focal_distance`` 为 ``focal_dist_to_height`` 并添加 getter/setter (`#1770 <https://github.com/3b1b/manim/pull/1770/commits/0610f331a4f7a126a3aae34f8a2a86eabcb692f4>`__)
- 为 ``VMobject.joint_type`` 添加 getter/setter (`#1770 <https://github.com/3b1b/manim/pull/1770/commits/2a7a7ac5189a14170f883533137e8a2ae09aac41>`__)
- 重构 ``VCube`` (`#1770 <https://github.com/3b1b/manim/pull/1770/commits/0f8d7ed59751d42d5011813ba5694ecb506082f7>`__)
- 重构 ``Prism``，接收 ``width height depth`` 而不是 ``dimensions`` (`#1770 <https://github.com/3b1b/manim/pull/1770/commits/0f8d7ed59751d42d5011813ba5694ecb506082f7>`__)
- 基于 ``LabelledString`` 重构 ``Text``, ``MarkupText`` 和 ``MTex`` (`#1772 <https://github.com/3b1b/manim/pull/1772>`__)
- 重构 ``LabelledString`` 和相关的类 (`#1779 <https://github.com/3b1b/manim/pull/1779>`__)


v1.5.0
------

Bug 修复
^^^^^^^^^^
- 修复了 ``Write`` 作用于空物件的 bug (`#1740 <https://github.com/3b1b/manim/pull/1740>`__)


新特性
^^^^^^^^^^^^
- 添加 ``TransformMatchingMTex`` 以适配 ``MTex`` 类 (`#1725 <https://github.com/3b1b/manim/pull/1725>`__)
- 添加 ``ImplicitFunction`` (`#1727 <https://github.com/3b1b/manim/pull/1727>`__)
- 添加 ``Polyline`` (`#1731 <https://github.com/3b1b/manim/pull/1731>`__)
- 允许 ``Mobject.set_points`` 方法接受一个空的列表，添加 ``Mobject.add_point`` 方法 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/a64259158538eae6043566aaf3d3329ff4ac394b>`__)
- 添加 ``Scene.refresh_locked_data`` 方法 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/33d2894c167c577a15fdadbaf26488ff1f5bff87>`__)
- 添加「演讲模式」，使用 ``-p`` 命令行参数 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/9a9cc8bdacb7541b7cd4a52ad705abc21f3e27fe>`__ and `#1742 <https://github.com/3b1b/manim/pull/1742>`__)
- 允许在交互过程中按 ``ctrl+shift+e`` 进行嵌入 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/9df12fcb7d8360e51cd7021d6877ca1a5c31835e>`__ and `#1746 <https://github.com/3b1b/manim/pull/1746>`__)
- 添加 ``Mobject.set_min_width/height/depth`` 方法 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/2798d15591a0375ae6bb9135473e6f5328267323>`__)
- 允许 ``Mobject.match_coord/x/y/z`` 接受一个点 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/29a4d3e82ba94c007c996b2d1d0f923941452698>`__)
- 给 ``DecimalNumber`` 添加了 ``text_config`` 参数 (`#1744 <https://github.com/3b1b/manim/pull/1744>`__)


重构
^^^^^^^^
- 重构 ``MTex`` (`#1725 <https://github.com/3b1b/manim/pull/1725>`__)
- 用 svg 元素重构了 ``SVGMobject`` (`#1731 <https://github.com/3b1b/manim/pull/1731>`__)
- 确保 ``ParametricCurve`` 至少含有一个坐标点 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/2488b9e866fb1ecb842a27dd9f4956ec167e3dee>`__)
- ``Axes`` 坐标系默认无箭头 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/6c6d387a210756c38feca7d34838aa9ac99bb58a>`__)
- 编译 tex 字符串时不再在命令行显示 (`#1739 <https://github.com/3b1b/manim/pull/1739/commits/58e06e8f6b7c5059ff315d51fd0018fec5cfbb05>`__)
- 重新组织 SVGMobject (`#1745 <https://github.com/3b1b/manim/pull/1745>`__)


依赖
^^^^^^^^^^^^
- 添加 ``isosurfaces`` 的依赖 (`#1727 <https://github.com/3b1b/manim/pull/1727>`__)
- 移除 ``argparse`` 的依赖，因为这个模块成为了 python 内置模块 (`#1728 <https://github.com/3b1b/manim/pull/1728>`__)
- 移除 ``pyreadline`` 依赖 (`#1728 <https://github.com/3b1b/manim/pull/1728>`__)
- 移除 ``cssselect2`` 依赖 (`#1731 <https://github.com/3b1b/manim/pull/1731>`__)
- 添加 ``svgelements`` 依赖 (`#1731 <https://github.com/3b1b/manim/pull/1731>`__)


v1.4.1
------

修复 BUG
^^^^^^^^^^
- 暂时修复了 ``BooleanOps`` 的填充色 BUG  (`#1724 <https://github.com/3b1b/manim/pull/1724>`__)
- 从 ``collections.abc`` 引入 ``Iterable`` 而不是从 ``collections`` 引入，因为后者在 python 3.9 之后被废弃 (`d2e0811 <https://github.com/3b1b/manim/commit/d2e0811285f7908e71a65e664fec88b1af1c6144>`__)

v1.4.0
------

修复 BUG
^^^^^^^^^^
- 暂时修复了 ``Lightbulb`` (`f1996f8 <https://github.com/3b1b/manim/pull/1697/commits/f1996f8479f9e33d626b3b66e9eb6995ce231d86>`__)
- 修复了 ``SVGMobject`` 的一些 BUG (`#1712 <https://github.com/3b1b/manim/pull/1712>`__)
- 修复了 SVG 路径字符串解析器的一些 BUG (`#1717 <https://github.com/3b1b/manim/pull/1717>`__)
- 修复了 ``MTex`` 的一些 BUG (`#1720 <https://github.com/3b1b/manim/pull/1720>`__)

新特性
^^^^^^^^^^^^
- 添加了一个选项，使得能够在 ``BarChart`` 添加 x 坐标轴的刻度 (`#1694 <https://github.com/3b1b/manim/pull/1694>`__)
- 添加 ``Brace`` 的配置参数 ``lable_buff`` (`#1704 <https://github.com/3b1b/manim/pull/1704>`__)
- 添加 SVG 的变化方法 ``rotate skewX skewY``  (`#1712 <https://github.com/3b1b/manim/pull/1712>`__)
- 添加 ``SVGMobject`` 的样式支持 (`#1717 <https://github.com/3b1b/manim/pull/1717>`__)
- 添加 SVG 的 <style> 元素解析器 (`#1719 <https://github.com/3b1b/manim/pull/1719>`__)
- 添加 ``SVGMobject`` 的 <line> 元素解析器 (`#1719 <https://github.com/3b1b/manim/pull/1719>`__)

重构 
^^^^^^^^
- 在音频支持上使用 ``FFMPEG_BIN`` 代替 ``"ffmpeg"`` (`5aa8d15 <https://github.com/3b1b/manim/pull/1697/commits/5aa8d15d85797f68a8f169ca69fd90d441a3abbe>`__)
- 将 ``CoordinateSystem.get_axes`` 和 ``.get_all_ranges`` 方法装饰为抽象方法 (`#1709 <https://github.com/3b1b/manim/pull/1709>`__)
- 重构 SVG 路径解析器 (`#1712 <https://github.com/3b1b/manim/pull/1712>`__)
- 允许 ``Mobject.scale`` 接受可迭代的 ``scale_factor`` 参数 (`#1712 <https://github.com/3b1b/manim/pull/1712>`__)
- 重构 ``MTex`` (`#1716 <https://github.com/3b1b/manim/pull/1716>`__)
- 完善了初始化配置的提示 (``manimgl --config``) (`#1721 <https://github.com/3b1b/manim/pull/1721>`__)
- 重构 ``MTex`` (`#1723 <https://github.com/3b1b/manim/pull/1723>`__)

依赖
^^^^^^^^^^^^
- 添加 `cssselect2 <https://github.com/Kozea/cssselect2>`__ (`#1719 <https://github.com/3b1b/manim/pull/1719>`__)


v1.3.0
------

Bug 修复 
^^^^^^^^^^

- `#1653 <https://github.com/3b1b/manim/pull/1653>`__: 修复 ``Mobject.stretch_to_fit_depth``
- `#1655 <https://github.com/3b1b/manim/pull/1655>`__: 修复旋转相机的 bug
- `c73d507 <https://github.com/3b1b/manim/pull/1688/commits/c73d507c76af5c8602d4118bc7538ba04c03ebae>`__: 修复 ``SurfaceMesh``
- `82bd02d <https://github.com/3b1b/manim/pull/1688/commits/82bd02d21fbd89b71baa21e077e143f440df9014>`__: 修复 ``angle_between_vectors`` 和 ``rotation_between_vectors``
- `a717314 <https://github.com/3b1b/manim/pull/1688/commits/a7173142bf93fd309def0cc10f3c56f5e6972332>`__: 修复 ``VMobject.fade``
- `fbc329d <https://github.com/3b1b/manim/pull/1688/commits/fbc329d7ce3b11821d47adf6052d932f7eff724a>`__: 修复 ``angle_between_vectors``
- `bcd0990 <https://github.com/3b1b/manim/pull/1688/commits/bcd09906bea5eaaa5352e7bee8f3153f434cf606>`__: 修复 ``ShowSubmobjectsOneByOne``
- `7023548 <https://github.com/3b1b/manim/pull/1691/commits/7023548ec62c4adb2f371aab6a8c7f62deb7c33c>`__: 修复 ``TransformMatchingParts``


新特性
^^^^^^^^^^^^

- `e10f850 <https://github.com/3b1b/manim/commit/e10f850d0d9f971931cc85d44befe67dc842af6d>`__: 添加命令行参数 ``--log-level`` 以指定日志级别
- `#1667 <https://github.com/3b1b/manim/pull/1667>`__: 为 ``Mobject`` 添加运算符 (``+`` 和 ``*``)
- `#1675 <https://github.com/3b1b/manim/pull/1675>`__: 在 ``manimlib/mobject/boolean_ops.py`` 中为 ``VMobject`` 添加四种布尔运算 

  - ``Union(*vmobjects, **kwargs)``
  - ``Difference(subject, clip, **kwargs)`` 
  - ``Intersection(*vmobjects, **kwargs)`` 
  - ``Exclusion(*vmobjects, **kwargs)`` 
- `81c3ae3 <https://github.com/3b1b/manim/pull/1688/commits/81c3ae30372e288dc772633dbd17def6e603753e>`__: 添加 ``reflectiveness``
- `2c7689e <https://github.com/3b1b/manim/pull/1688/commits/2c7689ed9e81229ce87c648f97f26267956c0bc9>`__: 在 ``DotCloud`` 上启用 ``glow_factor``
- `d065e19 <https://github.com/3b1b/manim/pull/1688/commits/d065e1973d1d6ebd2bece81ce4bdf0c2fff7c772>`__: 添加 ``-e`` 选项，可以从命令行插入代码进入交互模式
- `0e78027 <https://github.com/3b1b/manim/pull/1688/commits/0e78027186a976f7e5fa8d586f586bf6e6baab8d>`__: 针对弧形改进 ``point_from_proportion`` 
- `781a993 <https://github.com/3b1b/manim/pull/1688/commits/781a9934fda6ba11f22ba32e8ccddcb3ba78592e>`__: 添加设置黑色背景线条的缩写 ``set_backstroke``
- `0b898a5 <https://github.com/3b1b/manim/pull/1688/commits/0b898a5594203668ed9cad38b490ab49ba233bd4>`__: 添加 ``Suface.always_sort_to_camera``
- `e899604 <https://github.com/3b1b/manim/pull/1688/commits/e899604a2d05f78202fcb3b9824ec34647237eae>`__: 添加获取相机欧拉角的方法
- `407c53f <https://github.com/3b1b/manim/pull/1688/commits/407c53f97c061bfd8a53beacd88af4c786f9e9ee>`__: 改进 ``rotation_between_vectors``
- `49743da <https://github.com/3b1b/manim/pull/1688/commits/49743daf3244bfa11a427040bdde8e2bb79589e8>`__: 添加 ``Mobject.insert_submobject`` 方法
- `9dd1f47 <https://github.com/3b1b/manim/pull/1688/commits/9dd1f47dabca1580d6102e34e44574b0cba556e7>`__: 为整个场景的渲染创建全局进度条
- `264f7b1 <https://github.com/3b1b/manim/pull/1691/commits/264f7b11726e9e736f0fe472f66e38539f74e848>`__: 添加 ``Circle.get_radius``
- `83841ae <https://github.com/3b1b/manim/pull/1691/commits/83841ae41568a9c9dff44cd163106c19a74ac281>`__: 添加 ``Dodecahedron``
- `a1d5147 <https://github.com/3b1b/manim/pull/1691/commits/a1d51474ea1ce3b7aa3efbe4c5e221be70ee2f5b>`__: 添加 ``GlowDot``
- `#1678 <https://github.com/3b1b/manim/pull/1678>`__: 添加 ``MTex`` , 具体见 `#1678 <https://github.com/3b1b/manim/pull/1678>`__

重构
^^^^^^^^

- `#1662 <https://github.com/3b1b/manim/pull/1662>`__: 重构 SVG 对于 ``A`` 指令的处理
- `#1662 <https://github.com/3b1b/manim/pull/1662>`__: 重构 ``SingleStringTex.balance_braces``
- `8b454fb <https://github.com/3b1b/manim/pull/1688/commits/8b454fbe9335a7011e947093230b07a74ba9c653>`__: 微调牛顿分形的 ``saturation_factor``
- `317a5d6 <https://github.com/3b1b/manim/pull/1688/commits/317a5d6226475b6b54a78db7116c373ef84ea923>`__: 支持设置默认全屏预览
- `e764da3 <https://github.com/3b1b/manim/pull/1688/commits/e764da3c3adc5ae2a4ce877b340d2b6abcddc2fc>`__: 对于图上的点使用 ``quick_point_from_proportion``
- `d2182b9 <https://github.com/3b1b/manim/pull/1688/commits/d2182b9112300558b6c074cefd685f97c10b3898>`__: 使 ``Line.set_length`` 返回 self
- `eea3c6b <https://github.com/3b1b/manim/pull/1688/commits/eea3c6b29438f9e9325329c4355e76b9f635e97a>`__: 更好的使 ``SurfaceMesh`` 与关联的面对齐
- `ee1594a <https://github.com/3b1b/manim/pull/1688/commits/ee1594a3cb7a79b8fc361e4c4397a88c7d20c7e3>`__: 为 ``FlashAround`` 同步 ``fix_in_frame`` 状态
- `ba23fbe <https://github.com/3b1b/manim/pull/1688/commits/ba23fbe71e4a038201cd7df1d200514ed1c13bc2>`__: 使 ``Mobject.is_fixed_in_frame`` 保持和 uniforms 更新
- `98b0d26 <https://github.com/3b1b/manim/pull/1691/commits/98b0d266d2475926a606331923cca3dc1dea97ad>`__: 使 ``skip_animations`` 和 ``start_at_animation_number`` 可以同时使用
- `f8e6e7d <https://github.com/3b1b/manim/pull/1691/commits/f8e6e7df3ceb6f3d845ced4b690a85b35e0b8d00>`__: 优化全局进度条
- `8f1dfab <https://github.com/3b1b/manim/pull/1691/commits/8f1dfabff04a8456f5c4df75b0f97d50b2755003>`__: 使 ``VectorizedPoint`` 调用两个父类的 ``__init__``
- `758f329 <https://github.com/3b1b/manim/pull/1691/commits/758f329a06a0c198b27a48c577575d94554305bf>`__: 在检查是否刷新三角剖分时使用点集的拷贝


依赖
^^^^^^^^^^^^

- `#1675 <https://github.com/3b1b/manim/pull/1675>`__: 添加 python 包依赖 `skia-pathops <https://github.com/fonttools/skia-pathops>`__

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