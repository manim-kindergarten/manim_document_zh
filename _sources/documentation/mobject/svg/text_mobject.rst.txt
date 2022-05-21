Text
====

:class:`~manimlib.mobject.svg.text_mobject.MarkupText` 与 :class:`~manimlib.mobject.svg.text_mobject.MarkupText` 使用 ``ManimPango`` 
来生成文字的 svg ，所以它不需要 ``LaTeX`` 环境，而且可以方便地更改字体，但是不能够书写公式。该类继承自 :class:`~manimlib.mobject.svg.string_mobject.StringMobject` ，
因而支持 :class:`~manimlib.animation.transform_matching_parts.TransformMatchingStrings` 动画。

关于 Pango 提供的若干 markup 标签，详情参阅 `Pango Markup <https://docs.gtk.org/Pango/pango_markup.html>`__

:class:`~manimlib.mobject.svg.text_mobject.MarkupText` 提供的参数有：

-  ``is_markup: bool = True``: 决定是否解析 Pango markup 标签。 :class:`~manimlib.mobject.svg.text_mobject.Text` 类中该参数默认为 ``False``。
-  ``font_size: float = 48``: 全局字号。
-  ``lsh: float | None = None``: 行间距倍数，``line_spacing_height`` 的缩写。默认状态下视作 ``0.6``。
-  ``justify: bool = False``: 决定是否调整空格宽度使得段落左右侧同时对齐。
-  ``indent: int = 0``: 段首缩排。
-  ``alignment: "LEFT" | "CENTER" | "RIGHT" = "LEFT"``: 段落对齐方向。
-  ``line_width: float | None = None``: 段落宽度，即自动折行宽度，使用 manim 长度单位。默认状态下不折行。
-  ``font: str = ""``: 全局字体。
-  ``slant: str = "NORMAL"``: 全局倾斜样式。
-  ``weight: str = "NORMAL"``: 全局字重样式。
-  ``gradient: Iterable[ManimColor] | None = None``: 全局渐变色。
-  ``t2c: dict[Selector, ManimColor] = {}``: 局部颜色，``text2color`` 的缩写。
-  ``t2f: dict[Selector, ManimColor] = {}``: 局部字体，``text2font`` 的缩写。
-  ``t2s: dict[Selector, ManimColor] = {}``: 局部倾斜样式，``text2slant`` 的缩写。
-  ``t2w: dict[Selector, ManimColor] = {}``: 局部字重样式，``text2weight`` 的缩写。
-  ``global_config: dict[str, str] = {}``: 其它全局设置。
-  ``local_configs: dict[Selector, dict[str, str]] = {}``: 其它局部设置。
-  ``isolate: Selector = (re.compile(r"[a-zA-Z]+"), re.compile(r"\S+"))``: 预指定子串。
-  ``base_color: ManimColor = WHITE``: 全局颜色。

该类指定子串的可选方式有（``Selector`` 类型可参阅 :class:`~manimlib.mobject.svg.string_mobject.StringMobject` ）：

- ``isolate`` 参数（``Selector`` 类型）；
- ``t2c, t2f, t2s, t2w, local_configs`` 字典的键（``Selector`` 类型）；
- Pango markup 标签内部的内容（:class:`~manimlib.mobject.svg.text_mobject.Text` 不支持这种方式）。

一些示例如下：

.. manim-example:: TextExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/mobject/svg/text/TextExample.png

  from manimlib.imports import *
  
  class TextExample(Scene): 
      def construct(self): 
          text = Text('Hello, world!')
          self.add(text)


.. manim-example:: TextSlice
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/mobject/svg/text/TextSlice.png

  from manimlib.imports import *
  
  class TextSlice(Scene): 
      def construct(self):
          text = Text(
              'Google', 
              t2c={
                  (None,1):'#3174f0', (1,2):'#e53125', 
                  (2,3):'#fbb003', (3,4):'#3174f0', 
                  (4,5):'#269a43', (5,None):'#e53125',
              }
              # 注：当前可能还有 bug，None 和数值不能比较
              # 可暂时将这里的 None 改为 0 或字符串的长度
          )
          self.add(text)


.. manim-example:: TextUTF8
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/mobject/svg/text/MultilingualTextExample.png

  from manimlib.imports import *
  
  script = '''
  Hello
  你好
  こんにちは
  안녕하세요
  '''
  
  class MultilingualTextExample(Scene):
      def construct(self):
          text = Text(script, font='Source Han Sans')
          self.add(text)


MarkupText
**********

.. autoclass:: manimlib.mobject.svg.text_mobject.MarkupText
    :members:

Text
****

.. autoclass:: manimlib.mobject.svg.text_mobject.Text
    :members:

Code
****

.. autoclass:: manimlib.mobject.svg.text_mobject.Code
    :members:
