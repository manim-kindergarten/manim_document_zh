Code
====

:class:`~manimlib.mobject.svg.code_mobject.Code` 使用 ``pygments`` 给代码生成带语法高亮
的html文件，然后再转换为物体。

Code
****
.. autoclass:: manimlib.mobject.svg.code_mobject.Code

:class:`~manimlib.mobject.svg.code_mobject.Code` 的结构如下：

1. ``Code[0]`` 是代码的背景 ( ``Code.background_mobject`` )

   1. 如果 ``background == "rectangle"`` 则是一个Rectangle

   2. 如果 ``background == "window"`` 则是一个带有矩形和三个点的VGroup

2. ``Code[1]`` 是行号 ( ``Code.line_numbers`` 一个Paragraph)，可以使用 ``Code.line_numbers[0]`` 或者 ``Code[1][0]`` 来访问行号中的第一个数字

3. ``Code[2]`` 是代码 (``Code.code``)，一个带有颜色的Paragraph

.. manim-example:: CodeExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/Code.gif

  class CodeExample(Scene):
      def construct(self):
          heading = TextMobject("\"Hello, World\" Program", stroke_width=0).scale(1.3)
          heading.to_edge(UP)
          helloworldc = Code(
              "helloworldc.c",
              run_time=1,
              line_spacing=0.2,
              insert_line_no=False,
              style=code_styles_list[4],
              background="rectangle",
              language=code_languages_list["c"],
          )
          helloworldcpp = Code(
              "helloworldcpp.cpp",
              run_time=1,
              line_spacing=0.2,
              margin=0.3,
              line_no_from=8,
              style=code_styles_list[9],
              background="window",
              corner_radius=0.2,
              language=code_languages_list["cpp"],
          )
          helloworldc.move_to(np.array([-3.6, 0, 0]))
          helloworldcpp.move_to(np.array([3.1, 0, 0]))
          self.play(Write(heading), run_time=0.5)
          self.play(Write(helloworldc), run_time=1.3)
          self.draw_code_all_lines_at_a_time(helloworldcpp)
          self.wait()
  
      def draw_code_all_lines_at_a_time(self, Code):
          self.play(Write(Code.background_mobject), run_time=0.3)
          self.play(Write(Code.line_numbers), run_time=0.3)
          self.play(*[Write(Code.code[i]) for i in range(Code.code.__len__())],
                    run_time=Code.run_time)
