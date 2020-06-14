Color
=====

``manimlib/utils/color.py`` 这个文件中主要实现了和颜色处理有关的函数

-----

.. autofunction:: manimlib.utils.color.color_to_rgb

将颜色转换为RGB值，color可以为字符串(例“#66CCFF”)，也可以为Color类

-----

.. autofunction:: manimlib.utils.color.color_to_rgba

将颜色转换为RGB加上alpha透明度

-----

.. autofunction:: manimlib.utils.color.rgb_to_color

将RGB颜色转换为Color类

-----

.. autofunction:: manimlib.utils.color.rgba_to_color

将RGBA前三个数RGB转换为Color类

-----

.. autofunction:: manimlib.utils.color.rgb_to_hex

将RGB转换为十六进制字符串表示

-----

.. autofunction:: manimlib.utils.color.hex_to_rgb

将十六进制字符串转换为RGB

-----

.. autofunction:: manimlib.utils.color.invert_color

返回color的反色

-----

.. autofunction:: manimlib.utils.color.color_to_int_rgb

将颜色转化为整数RGB

-----

.. autofunction:: manimlib.utils.color.color_to_int_rgba

将颜色转化为整数RGBA

-----

.. autofunction:: manimlib.utils.color.color_gradient

返回长度为length_of_output的颜色梯度数组

-----

.. autofunction:: manimlib.utils.color.interpolate_color

在color1和color2之间插值，返回Color类表示的颜色

-----

.. autofunction:: manimlib.utils.color.average_color

返回colors的平均颜色

-----

.. autofunction:: manimlib.utils.color.random_bright_color

随机亮色

-----

.. autofunction:: manimlib.utils.color.random_color

在COLOR_MAP中随机选取颜色

-----

.. autofunction:: manimlib.utils.color.get_shaded_rgb(rgb, point, unit_normal_vect, light_source)

获取从光源light_source到point着色的RGB

