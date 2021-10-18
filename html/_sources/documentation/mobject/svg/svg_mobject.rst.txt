SVGMobject
==================

:class:`~manimlib.mobject.svg.svg_mobject.SVGMobject` 用于解析输入的SVG文件，并生成一个
:class:`~manimlib.mobject.types.vectorized_mobject.VMobject`。由于其方法都比较内部，
主要是根据SVG的元素来生成点集，这里就不列出文档字符串了。

MK做了一个关于常用 :class:`~manimlib.mobject.svg.svg_mobject.SVGMobject` 的的视频：
`〔manim教程〕第四讲 SVG、图片与文字  <https://www.bilibili.com/video/BV1CC4y1H7kp>`__

SVGMobject
**********
.. autoclass:: manimlib.mobject.svg.svg_mobject.SVGMobject

**关于传入SVG**：

- 使用相对于运行位置的相对路径，或使用绝对路径，或把图片放在 ``assets/svg_images`` 文件夹中
- 和绘图相关的元素目前只支持 ``path,rect,circle,ellipse,polygon,polyline``，不支持 ``text,line`` 等其他元素
- 自己制作svg，推荐使用 ``Adobe Illustrator`` ，并直接选择存储为（不选导出）

VMobjectFromSVGPathstring
*************************
.. autoclass:: manimlib.mobject.svg.svg_mobject.VMobjectFromSVGPathstring
