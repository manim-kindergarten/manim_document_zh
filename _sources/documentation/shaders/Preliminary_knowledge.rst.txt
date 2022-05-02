.. _OpenGL 预备知识:

OpenGL 预备知识
======================

.. admonition:: 注意

    本部分为 shader 学习的一些预备知识，读者需要对这一部分有所了解，才能得以继续深入。



OpenGL 运行流程
********************

.. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/OpenGL-sequence.svg



GLSL 函数
********************

这些函数主要用于片段着色

.. cpp:function:: genType smoothstep(genType edge_0, genType edge_1, genType x)

    - 当 ``x <= edge_0`` 时返回 0.0
    - 当 ``x >= edge_1`` 时返回 1.0
    - 当 ``edge_0 < x < edge_1`` 时形成一个从 0 到 1 的平滑插值

    .. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/functions/smoothstep1.svg

    特别的，当 ``egde_0 > edge_1`` 时，图像会翻转，即满足下面的情况

    - 当 ``x <= edge_1`` 时返回 1.0
    - 当 ``x >= edge_0`` 时返回 0.0
    - 当 ``edge_1 < x < edge_0`` 时形成一个从 1 到 0 的平滑插值

    .. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/functions/smoothstep2.svg

--------------------

.. cpp:function:: genType mix(genType x, genType y, float a)

    - 返回值为 ``x * (1 - a) + y * a``，即为 ``x`` 到 ``y`` 的插值

--------------------

.. cpp:function:: genType clamp(genType x, genType minVal, genType maxVal)

    将自变量 ``x`` 限制在给定的范围内，即有 

    - 当 ``x < minVal`` 时返回 ``minVal``
    - 当 ``x > maxVal`` 时返回 ``maxVal``
    - 当 ``minVal < x < maxVal`` 时返回 ``x``

--------------------



一些概念
********************

sdf 符号距离函数
--------------------

对一个圆上色，我们可能会这么考虑：当半径小于等于 radius 时，就对它上色，其他不上色。此时，也就有了伪代码

.. code-block:: cpp

    if (length(point) <= radius) {
        // 圆内着色
    } else {
        // 圆外不着色
    }

但是当有更加复杂的图形时，这样就会形成相当复杂的 if-else 树，这样不仅代码不美观，性能上也较差。因此我们寻求更加高效的方案：sdf

同样是画圆，我们这样定义

.. code-block:: cpp

    float sdfCircle(vec2 point, float radius) {
        return length(p) - radius;
    }

此时我们仔细分析一下

    - 在圆内的点，返回的结果均小于 0
    - 在圆上的点，返回值为 0
    - 在圆外的点，返回值均大于 0

此时， 0 就成了一个分界点，我们可以使用一些其他的函数来进一步处理，即可得到理想的效果了。我们使用上面提到的 smoothstep 函数

.. code-block:: cpp

    float f = smoothstep(0.01, 0., sdfCircle(coords, 0.5))

这一步得到 ``f`` ，它的结果为：当点在圆内，则返回 1 ，在圆外，则返回 0，可以得到一个近似的圆的坐标集

.. code-block:: cpp

    color = mix(color, vec3(1., 1., 0.), f);


这一步中，将原有的片段颜色和圆的颜色（黄色）混合，混合的依据就是 ``f``，值为 0 的像素，使用原有的颜色，值为 1 的像素，使用圆的颜色。

这样我们就可以在坐标系中画一个圆。
