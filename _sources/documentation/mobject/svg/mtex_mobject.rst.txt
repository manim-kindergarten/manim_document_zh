MTex
====

该类由凡人忆拾编写和完善，使用 ``latex/xelatex`` 生成公式。该类继承自 :class:`~manimlib.mobject.svg.string_mobject.StringMobject` ，
因而支持 :class:`~manimlib.animation.transform_matching_parts.TransformMatchingStrings` 动画。

:class:`~manimlib.mobject.svg.mtex_mobject.MTex` 提供的参数有：
-  ``font_size: float = 48``: 全局字号。
-  ``alignment: str = "\\centering"``: 对齐方向。
-  ``tex_environment: str | tuple[str, str] | None = "align*"``: tex 环境。 :class:`~manimlib.mobject.svg.mtex_mobject.MTexText` 类中该参数默认为 ``None``。
-  ``tex_to_color_map: dict[Selector, ManimColor] = {}``: 局部颜色。
-  ``isolate: Selector = ()``: 预指定子串。
-  ``base_color: ManimColor = WHITE``: 全局颜色。

该类指定子串的可选方式有（``Selector`` 类型可参阅 :class:`~manimlib.mobject.svg.string_mobject.StringMobject` ）：

- ``isolate`` 参数（``Selector`` 类型）；
- ``tex_to_color_map`` 字典的键（``Selector`` 类型）；
- 双大括号内部的内容。

下面给出用不同方式指定子串的示例：

.. manim-example:: MTexSpecifySubstrings
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/mobject/svg/mtex/MTexSpecifySubstrings.png
  
  class MTexSpecifySubstrings(Scene): 
      def construct(self):
          tex = MTex("\\sqrt{{s}}").shift(UP)
          tex.select_part("s").set_fill(TEAL)
          self.add(tex)
          poly = MTex(
              "p(x) = a_0 x^0 + a_1 x^1 + \\cdots + a_{n-1} x^{n-1} + a_n x^n",
              tex_to_color_map={re.compile(r"a_(.+?) x\^\1"): ORANGE}
          )
          self.add(poly)

MTex
****

.. autoclass:: manimlib.mobject.svg.mtex_mobject.MTex
    :members:


MTexText
********

.. autoclass:: manimlib.mobject.svg.mtex_mobject.MTexText
    :members:


JTex
****

.. admonition:: 注意

    在 manimgl 中并不包含，但可以通过一些方式引入。


由 Fran 编写，继承自 MTex，基于 mathjax 生成公式，可以通过链接查看使用方法 `<https://github.com/manim-kindergarten/manimgl-mathjax.git>`__

由于该类基于 mathjax 生成公式，因此相比 LaTeX，该类会有更快的生成速度。同时对于公式的需求没有那么高的情况下，甚至可以不用安装 LaTeX，所以力推 ``JTex``。但这个类并不支持中文。
