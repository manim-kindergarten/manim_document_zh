MTex
=============

该类由凡人忆拾编写和完善，使用 ``latex/xelatex`` 生成公式。不同的是，``MTex`` 能够更加方便的给 Tex 上色。

由于该类并非继承 ``Tex`` ，所以 ``TransfromMatchingTex`` 方法会出一些问题，因此这个类还在完善中。


MTex
*******
.. autoclass:: manimlib.mobject.svg.mtex_mobject.MTex
    :members:


MTexText
*********

.. autoclass:: manimlib.mobject.svg.mtex_mobject.MTexText
    :members:


JTex
******

.. admonition:: 注意

    在 manimgl 中并不包含，但可以通过一些方式引入。


由 Fran 编写，继承自 MTex，基于 mathjax 生成公式，可以通过链接查看使用方法 `<https://github.com/manim-kindergarten/manimgl-mathjax.git>`__


