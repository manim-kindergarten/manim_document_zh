TeX and Text
============
.. admonition:: 声明

   这一页是elteoremadebeethoven写的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/mobjects/tex.html>`_  我翻译+做笔记，把资料整合编辑成方便的文档格式，以方便查阅使用Manim。

详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>`  。

There are two commands to create text, ``TexMobject`` and ``TextMobject``. In both parameters the text is written in TeX format, but while in ``TextMobject`` you write in normal mode, in ``TexMobject`` you are writing within the ``align*`` environment.


The LaTeX packages that Manim uses are in:

::

    manimlib/tex_template.tex

..

They are the following by default:

.. literalinclude:: ../manimlib/tex_template.tex
    :lines: 3-18

TexMobject
----------

.. autoclass:: manimlib.mobject.svg.tex_mobject.TexMobject
.. automethod:: manimlib.mobject.svg.tex_mobject.TexMobject.get_tex_string
.. automethod:: manimlib.mobject.svg.tex_mobject.TexMobject.set_color_by_tex

..

TextMobject
-----------

.. autoclass:: manimlib.mobject.svg.tex_mobject.TextMobject
.. automethod:: manimlib.mobject.svg.tex_mobject.TextMobject.get_tex_string
.. automethod:: manimlib.mobject.svg.tex_mobject.TextMobject.set_color_by_tex
