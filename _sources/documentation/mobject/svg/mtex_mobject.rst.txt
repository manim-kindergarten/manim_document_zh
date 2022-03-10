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

由于该类基于 mathjax 生成公式，因此相比 LaTeX，该类会有更快的生成速度。同时对于公式的需求没有那么高的情况下，甚至可以不用安装 LaTeX，所以力推 ``JTex``。但这个类目前还有一些小问题需要完善：

- 不能在其中使用中文
- 由于该类还在开发过程中，因此可能会有一些渲染上的 bug
- 由于继承了 MTex，而 ``TransfromMatchingMTex`` 还需要完善，所以公式的对应变换还需要一段时间来修复
