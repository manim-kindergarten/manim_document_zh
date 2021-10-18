svg
==============

``SVG`` 是一种基于xml格式表示的矢量图形，因此可以直接转化为
:class:`~manimlib.mobject.types.vectorized_mobject.VMobject` 中的点集。

``manimlib/mobject/svg/`` 文件夹中包含了解析SVG文件的 
:class:`~manimlib.mobject.svg.svg_mobject.SVGMobject`，和一些基于SVG的常用子类(例如文字)。

但是manim对SVG的解析目前不完善，所以可能不能很好的解析出正常的图像。

另外，关于SVG与文字的使用方法，这里有一个视频教程：
`〔manim教程〕第四讲 SVG、图片与文字  <https://www.bilibili.com/video/BV1CC4y1H7kp>`__

.. toctree::
   :maxdepth: 2
   :caption: 目录

   brace
   drawings
   svg_mobject
   tex_mobject
   text_mobject