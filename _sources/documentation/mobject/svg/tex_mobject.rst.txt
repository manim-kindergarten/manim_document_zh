Tex
=============

:class:`~manimlib.mobject.svg.tex_mobject.Tex` 和 :class:`~manimlib.mobject.svg.tex_mobject.TexText`
使用 ``latex/xelatex`` 来讲输入的字符串根据LaTeX语法编译为 ``dvi/xdv`` 文件，
再通过 ``dvisvgm`` 将其转换为 ``svg`` 文件，通过 :class:`~manimlib.mobject.svg.svg_mobject.SVGMobject`
转换为物体，实现添加文字/公式的效果。

关于 :class:`~manimlib.mobject.svg.tex_mobject.Tex` 和 :class:`~manimlib.mobject.svg.tex_mobject.TexText`
的区别，还有 ``LaTeX`` 发行版安装和文字字体问题，常见问题中有更详细的解答：

- `manim常见问题：LaTeX问题 <https://docs.manim.org.cn/CommonProblems/v2.3.html#latex>`__
- `manim常见问题：中文显示问题 <https://docs.manim.org.cn/CommonProblems/v2.3.html#id7>`__
- `manim常见问题：文字问题 <https://docs.manim.org.cn/CommonProblems/v2.3.html#id8>`__

MK做了一个关于常用 :class:`~manimlib.mobject.svg.tex_mobject.Tex` 和 :class:`~manimlib.mobject.svg.tex_mobject.TexText` 的视频（该视频适用于旧版，但新版也能凑合着看）：
`〔manim教程〕第四讲 SVG、图片与文字  <https://www.bilibili.com/video/BV1CC4y1H7kp>`__


SingleStringTex
**********************
.. autoclass:: manimlib.mobject.svg.tex_mobject.SingleStringTex
    :members:

Tex
**********
.. autoclass:: manimlib.mobject.svg.tex_mobject.Tex
    :members:

.. TODO: 添加示例

TexText
***********
.. autoclass:: manimlib.mobject.svg.tex_mobject.TexText
    :members:

.. TODO: 添加示例

BulletedList
************
.. autoclass:: manimlib.mobject.svg.tex_mobject.BulletedList
    :members:

.. TODO: 添加示例

TexFromPresetString
********************
.. autoclass:: manimlib.mobject.svg.tex_mobject.TexFromPresetString
    :members:

.. TODO: 添加示例

Title
*****
.. autoclass:: manimlib.mobject.svg.tex_mobject.Title
    :members:

.. TODO: 添加示例

