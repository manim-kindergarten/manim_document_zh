Mathematical Objects数学对象
================================


.. admonition:: 声明

   这一页是EulerTour写的教程,我只是翻译+学习笔记，github早就有很多教程，但是为了方便查询使用，我才整合这么一份文档。

Mathematical Objects就是Mobject,每个Mobject有3种成分。
Everything that appears on screen in a manim video is a
:class:`~mobject.mobject.Mobject`, or Mathematical Object. A
:class:`~mobject.mobject.Mobject`'s appearance is determined by 3
factors:

* ``m.points``, an Nx3 ``numpy.array`` specifying how to draw ``m``.存成 ``numpy.array`` 决定画出来形状的点集。
* ``m``'s style attributes, such as ``m.color``, ``m.stroke_width``, and  ``m.fill_opacity``.属性，可以在VisualStudioCode中ctrl+click看父类定义py文件获得详情。
* ``m.submobjects``, a list of :class:`~mobject.mobject.Mobject` instances that are considered part of ``m`` .子对象 

这里是简要的的介绍，可以看后面很多的例子体会，宏观认知有助于理解和设计。详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>`  。
