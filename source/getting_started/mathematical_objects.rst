数学对象-Mathematical Objects
================================


.. admonition:: 声明

   这一页翻译自EulerTour的教程


屏幕上的所有物品叫做 :class:`~mobject.mobject.Mobject` （Mathematical Objects）, 每个 :class:`~mobject.mobject.Mobject` 有3个部分：

* ``m.points``, 一个三维 ``numpy.array`` 决定了 ``m`` 的形状

   - 对于 :class:`~mobject.types.vectorized_mobject.VMobject` ，其中存的是构建贝塞尔曲线的锚点和控制点
   - 对于 :class:`~mobject.types.point_cloud_mobject.PMobject` ，其中存的是点集中的所有点
   - 对于 :class:`~mobject.types.image_mobject.ImageMobject` ，其中存的是图片角落的点（用于定位）
* ``m`` 的样式属性，例如 ``m.color``, ``m.stroke_width``, 和 ``m.fill_opacity`` 等
* ``m.submobjects`` 一个由 :class:`~mobject.mobject.Mobject` 构成的列表，是 ``m`` 的子物体

这里是简要的的介绍，可以看后面很多的例子体会，宏观认知有助于理解和设计。
