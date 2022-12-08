Tex
=============

:class:`~manimlib.mobject.svg.tex_mobject.Tex` 和 :class:`~manimlib.mobject.svg.tex_mobject.TexText`
使用 ``latex/xelatex`` 来讲输入的字符串根据LaTeX语法编译为 ``dvi/xdv`` 文件，
再通过 ``dvisvgm`` 将其转换为 ``svg`` 文件，通过 :class:`~manimlib.mobject.svg.svg_mobject.SVGMobject`
转换为物体，实现添加文字/公式的效果。

关于 :class:`~manimlib.mobject.svg.tex_mobject.Tex` 和 :class:`~manimlib.mobject.svg.tex_mobject.TexText`
的区别，还有 ``LaTeX`` 发行版安装和文字字体问题，常见问题中有更详细的解答：

- `manimgl 常见问题：LaTeX 问题 <https://manim.org.cn/problems/manimgl#%F0%9F%93%8C-2.2-latex-%E9%97%AE%E9%A2%98>`__
- `manimgl 常见问题：dvisvgm 问题 <https://manim.org.cn/problems/manimgl#2.3-dvisvgm-%E9%97%AE%E9%A2%98>`__
- `manim 常见问题：LaTeX 问题 <https://manim.org.cn/problems/manim-cairo#2.2.-latex-%E9%97%AE%E9%A2%98>`__
- `manim 常见问题：中文显示问题 <https://manim.org.cn/problems/manim-cairo#2.4.-%E4%B8%AD%E6%96%87%E6%98%BE%E7%A4%BA%E9%97%AE%E9%A2%98>`__
- `manim 常见问题：文字问题 <https://manim.org.cn/problems/manim-cairo#2.5.-%E6%96%87%E5%AD%97%E9%97%AE%E9%A2%98>`__

MK做了一个关于常用 :class:`~manimlib.mobject.svg.tex_mobject.Tex` 和 :class:`~manimlib.mobject.svg.tex_mobject.TexText` 的视频（该视频适用于旧版，但新版也能凑合着看）：
`〔manim教程〕第四讲 SVG、图片与文字  <https://www.bilibili.com/video/BV1CC4y1H7kp>`__

另外，`凡人忆拾 <https://github.com/YishiMichael>`__ 正在写 ``MTex`` 类，针对 ``Tex`` 类的上色做了相当多的优化，目前还在测试期间，可以先尝试下载他的分支体验一下，待 Grant 合并分支后，我们将会把这一部分文档一并更新。

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

