二阶贝塞尔曲线填充色 Quadratic bezier fill
============================================

Vertex shader
***********************

参数列表
-----------------------

=========  ===============  =========================  ======================
参数类型     数据类型          变量名                       说明
=========  ===============  =========================  ======================
in         ``vec3``         ``point``                  从 manim 传入的顶点坐标
in         ``vec3``         ``unit_normal``            单位法向量
in         ``vec4``         ``color``                  传入的颜色
in         ``float``        ``vert_index``             顶点索引
out        ``vec3``         ``bp``                     贝塞尔曲线控制点
out        ``vec3``         ``v_global_unit_normal``   传给 geom 单位法向量
out        ``vec4``         ``v_color``                传给 geom 顶点颜色
out        ``float``        ``v_vert_index``           传给 geom 顶点索引
=========  ===============  =========================  ======================


Geometry shader
***********************

几何图元
-----------------------

.. code-block:: cpp

    layout (triangle) in;                         // 输入图元
    layout (triangle_strip, max_vertices=5) out;  // 输出图元


参数列表
-----------------------

=========  ===============  ============================  ======================
参数类型     数据类型          变量名                          说明
=========  ===============  ============================  ======================
uniform    ``float``        ``anti_alias_width``          抗锯齿宽度
uniform    ``vec2``         ``frame_shape``               帧大小
uniform    ``float``        ``focal_distance``            焦距
uniform    ``float``        ``is_fixed_in_frame``         是否固定在画面上
uniform    ``vec3``         ``light_source_position``     光源位置
uniform    ``vec3``         ``camera_position``           相机位置
uniform    ``float``        ``reflectiveness``            反光度
uniform    ``float``        ``gloss``                     光泽
uniform    ``float``        ``shadow``                    阴影
in         ``vec3``         ``bp[3]``                     贝塞尔控制点
in         ``vec3``         ``v_global_unit_normal[3]``   单位法向量
in         ``vec4``         ``v_color[3]``                颜色
in         ``float``        ``v_vert_index[3]``           顶点索引
out        ``vec4``         ``color``                     颜色
out        ``float``        ``fill_all``                  是否填充
out        ``float``        ``uv_anti_alias_width``       uv 坐标下的抗锯齿宽度
out        ``vec3``         ``xyz_coords``                xyz 坐标系
out        ``float``        ``orientation``               方向
out        ``vec2``         ``uv_coords``                 uv 坐标系
out        ``vec2``         ``uv_b2``                     uv 坐标系下的点 b2
out        ``float``        ``bezier_degree``             曲线阶数
=========  ===============  ============================  ======================


Fragment shader
***********************

参数列表
-----------------------

=========  ===============  =======================  ======================
参数类型     数据类型          变量名                     说明
=========  ===============  =======================  ======================
in         ``vec4``         ``color``                由 geom 传入颜色
in         ``float``        ``fill_all``             是否填充
in         ``float``        ``uv_anti_alias_width``  uv 坐标系下的抗锯齿宽度
in         ``vec3``         ``xyz_coords``           xyz 坐标系
in         ``float``        ``orientation``          方向
in         ``vec2``         ``uv_coords``            uv 坐标系
in         ``vec2``         ``uv_b2``                uv 坐标系下的点 b2 坐标
in         ``float``        ``bezier_degree``        曲线阶数
out        ``vec4``         ``frag_color``           片段颜色
=========  ===============  =======================  ======================


函数
-----------------------

.. cpp:function:: float sdf()

    signed distance function 符号距离函数


程序流程
***********************

.. admonition:: 注意

    该部分为笔者的个人理解，若有不当之处，欢迎批评指正。

三角剖分
-----------------------

对于一个由贝塞尔曲线构成的 VMobject，首先需要根据其顶点进行剖分，将整个图形按照顶点分割成一系列三角形。
这一操作被称作 **三角剖分**，由 earcut 来完成，具体的原理可以查看
`WallBreaker5th <https://github.com/Wallbreaker5th>`_ 的视频 
`刵 <https://www.bilibili.com/video/BV16L411E7xK>`_ 。

三角剖分完成之后，就可以对 VMobject 上色了。我们需要对这一系列三角以及一些弓形着色。


顶点着色器
-----------------------

顶点着色器从程序中获取顶点的位置、颜色、顶点索引、法向量，并向下一层传递。


几何着色器
-----------------------

几何着色器接收一个基本图形——点，以这个点为中心，创建基本图形。在此处，该着色器接收的是 triangles ，并将
triangle_strip 作为输出，其顶点数量最大值为 5. 

Quadratic bezier fill 的几何着色器中的图元有三角形和五边形，而五边形是对三角形的边进行了抗锯齿的优化，
对于宏观的理解来说差别不是很大。

-   假设原先的三个控制点为 ``[p0, p1, p2]`` ，则五边形的控制点可以理解为 ``[p0, p0 + dt, p1, p2 +dt, p2]``

上面提到了三角剖分，而此处的图元大多为三角形或者五边形，这里引入 ``fill_all`` 变量，用于指定按照直接三角形绘制，
或者对贝塞尔曲线的控制点进行抗锯齿优化后，按照五边形绘制。当传入的顶点索引是相邻的正整数（例如 1, 2, 3 或 2, 3, 4 ），
那么就不使用直接三角形绘制。至于为什么这样做，下面解释其原因。

-   假设有一个圆，它由八段贝塞尔曲线拼接而成，每段由 3 个控制点构成。给这个圆上填充色之前，我们需要对它进行三角剖分，
    分割为一些三角形和边上的八个弓形。这些图形被称为“图元”，它们都是由 3 个控制点构成的。

    .. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/fill_with_sdf.png

    对于内部的这些三角形，注意到它们的三个顶点索引几乎都是不相邻的整数，我们可以直接采用直接三角形方案来上色。

    而对于外面的这些弓形，它们的三个控制点索引几乎都是相邻的整数，因此我们不采用 ``fill_all`` 的方案，
    而是而采用贝塞尔曲线的上色方案。

接下来真正上色的工作就留给片段着色器。


片段着色器
-----------------------

在此模块开始前，建议先看一看 :ref:`OpenGL 预备知识`

对于内部的这些三角形图元，片段着色器只需无脑地把颜色传递给 frag_color 即可，因为这些三角形图元不涉及到较为复杂的曲线上色。

而对于边缘上的弓形，我们就需要使用 sdf 符号距离函数来进行一些处理。我们采用这样的方案：

-   由三个控制点构成的贝塞尔曲线的弓形，可以被这三个控制点所构成的三角形覆盖，因此我们可以先无脑地不管是什么样的图元，
    我们都按照三角图元来上色，这样也就直接覆盖了上面的情况。

    .. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/fill_without_sdf.png

    而边缘的弓形也被涂成了三角形，这与我们的目标有一些偏差。此时 ``fill_all`` 参数的用途就得以体现了：当 ``fill_all == 1.0``
    说明此时是直接三角形绘制；否则，我们就按照贝塞尔曲线的上色方法，通过 sdf 计算，使得在弓形内部的像素点，保持其透明度不变；
    而在弓形外部的像素点，其透明度为 0 

    .. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/curve_fill_shader.png

    另外，还有一些细节，例如指定向曲线凹陷处填充等等，在此不过多阐述。

此时， VMobject 的填充色着色程序工作完成。


流程图
***********************

.. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/shaders/quadratic_bezier_fill_shader.svg


