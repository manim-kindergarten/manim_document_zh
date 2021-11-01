着色代码 shaders (TODO)
==========================

.. admonition:: 注意

    本部分与 manim 入门的关联不算很大，因为涉及到大量的 OpenGL Shading Language 的成分，主要用于图形的上色。

    有能力的读者，可以先下面的网站学习一下
    
    - `<https://thebookofshaders.com/>`_ 
    - `<https://shadertoy.com/>`_ 
    - `<https://smoothstep.io/>`_


set_color_by_code
*********************
该方法为 :class:`~manimlib.mobject.mobject.Mobject` 的成员函数

也许你会用到这个方法来进行上色，这里仅给出一些提示，详细的教程请自行学习 glsl.

glsl 中的变量
-------------

- ``vec4 color`` : 颜色，rgba的范围均为 [0.0, 1.0]

  - ``float r`` : 红色
  - ``float g`` : 绿色
  - ``float b`` : 蓝色
  - ``float a`` : 透明度

- ``vec3 points`` : 三维坐标

  - ``float x``
  - ``float y``
  - ``float z``

- ``vec3 unit_normal`` : 单位法线

- ``vec3 light_coords`` : 光源坐标

- ``float gloss`` : 光泽

- ``float shadow`` : 阴影

下面的代码可以将一个正方形从左到右渐变上色

.. code:: python

    class TestGlsl(Scene):
        def construct(self):
            square = Square(side_length=4)
            square.set_color_by_code(f"""
                vec3 blue = vec3{tuple(hex_to_rgb(BLUE))};
                vec3 red = vec3{tuple(hex_to_rgb(RED))};
                color.rgb = mix(blue, red, (point.x + 1.5) / 3);
            """)
            self.add(square)

            # hex_to_rgb 会将 16 进制颜色字符串转变为 RGB 三元列表，其值范围均为 [0,1]
            # 利用 tuple 将它们用圆括号括起来，翻译后的字符串就变为（这里仅展示一部分）
            # vec3 blue = vec3(0.345, 0.769, 0.867);