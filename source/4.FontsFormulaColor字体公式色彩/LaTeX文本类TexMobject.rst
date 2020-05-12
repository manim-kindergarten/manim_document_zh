

LaTeX文本类TexMobject 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库配套源码和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程的MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是想把Markdown、pdf等资料整合编辑成方便的文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。

LaTeX文本类 TexMobject
 

**\\manimlib\\mobject\\svg\\tex_mobject.py**

显示为LaTeX格式(在想要LaTeX字符串按照数组显示时必须使用这个实现)

.. code:: python

   CONFIG = {
           "template_tex_file_body": TEMPLATE_TEX_FILE_BODY,
           # 笔画宽度
           "stroke_width": 0,
           # 填充不透明度
           "fill_opacity": 1.0,
           # 笔画的描边宽度
           "background_stroke_width": 1,
           # 笔画的描边颜色
           "background_stroke_color": BLACK,
           "should_center": True,
           "height": None,
           "organize_left_to_right": False,
           "alignment": "",
       }

例：

.. code:: python

   class Formula(Scene): 
       def construct(self): 
           formula = TexMobject("This is a sentence")
           self.play(Write(formula))
           self.wait(3)

.. figure:: ../assets/image/1565769340216.png
   :alt: 1565769340216

   This is a sentence







