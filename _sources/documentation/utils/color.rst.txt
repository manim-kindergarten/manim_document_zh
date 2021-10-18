Color
=====

``manimlib/utils/color.py`` 这个文件中主要实现了和颜色处理有关的函数

关于颜色，MK 有一个视频教程：
`〔manim 教程〕第三讲 颜色的表示、运算与设置  <https://www.bilibili.com/video/BV1vZ4y1x7hT>`__


-----

.. autofunction:: manimlib.utils.color.color_to_rgb

将颜色转换为 RGB 值，color 可以为字符串(例“#66CCFF”)，也可以为 Color 类

-----

.. autofunction:: manimlib.utils.color.color_to_rgba

将颜色转换为 RGB 加上 alpha 透明度

-----

.. autofunction:: manimlib.utils.color.rgb_to_color

将 RGB 颜色转换为 Color 类

-----

.. autofunction:: manimlib.utils.color.rgba_to_color

将 RGBA 前三个数 RGB 转换为 Color 类

-----

.. autofunction:: manimlib.utils.color.rgb_to_hex

将 RGB 转换为十六进制字符串表示

-----

.. autofunction:: manimlib.utils.color.hex_to_rgb

将十六进制字符串转换为 RGB

-----

.. autofunction:: manimlib.utils.color.invert_color

返回 color 的反色

-----

.. autofunction:: manimlib.utils.color.color_to_int_rgb

将颜色转化为整数 RGB

-----

.. autofunction:: manimlib.utils.color.color_to_int_rgba

将颜色转化为整数 RGBA

-----

.. autofunction:: manimlib.utils.color.color_gradient

返回长度为 length_of_output 的颜色梯度数组

-----

.. autofunction:: manimlib.utils.color.interpolate_color

在 color1 和 color2 之间插值，返回 Color 类表示的颜色

-----

.. autofunction:: manimlib.utils.color.average_color

返回 colors 的平均颜色

-----

.. autofunction:: manimlib.utils.color.random_bright_color

随机亮色

-----

.. autofunction:: manimlib.utils.color.random_color

在 COLOR_MAP 中随机选取颜色

-----

.. autofunction:: manimlib.utils.color.get_shaded_rgb(rgb, point, unit_normal_vect, light_source)

获取从光源 light_source 到 point 着色的 RGB

