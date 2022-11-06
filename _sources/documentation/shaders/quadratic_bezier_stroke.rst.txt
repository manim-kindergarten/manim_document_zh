二阶贝塞尔曲线轮廓线着色 Quadratic bezier stroke
====================================================


Vertex shader
***********************

参数列表
-----------------------

=========  ===============  =========================  ======================
参数类型     数据类型          变量名                       说明
=========  ===============  =========================  ======================
in          ``vec3``        ``point``                   顶点
in          ``vec3``        ``prev_point``              前驱顶点
in          ``vec3``        ``next_point``              后继顶点
in          ``vec3``        ``unit_normal``             单位法向量
in          ``float``       ``stroke_width``            线宽
in          ``vec4``        ``color``                   颜色
out         ``vec3``        ``bp``                      贝塞尔控制点
out         ``vec3``        ``prev_bp``                 前驱控制点
out         ``vec3``        ``next_bp``                 后继控制点
out         ``vec3``        ``v_global_unit_normal``    输出单位法向量
out         ``float``       ``v_stroke_width``          输出线宽
out         ``vec4``        ``v_color``                 输出颜色
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

=========  ===============  ==============================  ========================
参数类型     数据类型          变量名                           说明
=========  ===============  ==============================  ========================
uniform     此处省略           此处省略                        用于坐标变换和光照
in          ``vec3``         ``bp[3]``                      贝塞尔曲线控制点
in          ``vec3``         ``prev_bp[3]``                 前一组控制点
in          ``vec3``         ``next_bp[3]``                 下一组控制点
in          ``vec3``         ``v_global_unit_normal[3]``    单位法向量
in          ``vec4``         ``v_color[3]``                 顶点颜色
in          ``float``        ``v_stroke_width[3]``          顶点对应的轮廓线宽
out         ``vec4``         ``color``                      输出颜色
out         ``float``        ``uv_stroke_width``            uv 坐标下的轮廓线宽
out         ``float``        ``uv_anti_alias_width``        uv 坐标下抗锯齿宽度
out         ``float``        ``has_prev``                   是否有前驱
out         ``float``        ``has_next``                   是否有后继
out         ``float``        ``bevel_start``                起始斜边
out         ``float``        ``bevel_end``                  结束斜边
out         ``float``        ``angle_from_prev``            与前驱手柄的夹角
out         ``float``        ``angle_to_next``              与后继手柄的夹角
out         ``float``        ``bezier_degree``              贝塞尔曲线阶数
out         ``vec2``         ``uv_coords``                  uv 坐标系
out         ``vec2``         ``uv_b2``                      uv 坐标下的顶点 b2
=========  ===============  ==============================  ========================

函数列表
-----------------------

.. cpp:function:: void flatten_points(vec3 points[3], vec2 flat_points[3])

    - ``points`` 为输入参数
    - ``flat_point`` 为输出参数

    透视投影变换

.. cpp:function:: float angle_between_vectors(vec2 v1, vec2 v2)

    两向量之间的夹角

.. cpp:function:: bool find_intersection(vec2 p0, vec2 v0, vec2 p1, vec2 v1, vec2 intersection)

    - ``intersection`` 为输出参数

    过点 p0，方向为 v0 的直线与过点 p1，方向为 v1 的直线的交点

.. cpp:function:: void create_joint(float angle, vec2 unit_tan, float buff, vec2 static_c0, vec2 changing_c0, vec2 static_c1, vec2 changing_c1)

    - ``changing_c0`` 和 ``changing_c1`` 为输出参数

    创建接合处

.. cpp:function:: int get_corners(vec2 controls[2], int degree, float stroke_widths[3], vec2 corners[5])

    - ``corners`` 为输出参数

    寻找贝塞尔曲线边界的角，可以作为三角扇形发出（直接翻译真的看不懂）

    - 当图形的边为直线时，生成的图元是一个四边形
    - 当图形的边为曲线时，生成的图元为五边形

.. cpp:function:: void set_adjascent_info(vec2 c0, vec2 tangent, int degree, vec2 adj[3], float bevel, float angle)

    - ``bevel`` 和 ``angle`` 为输出参数

    计算邻边角度，并判断是否需要添加斜边来弥补缺失的接合处

.. cpp:function:: void find_joint_info(vec2 controls[3], vec2 prev[3], vec2 next[3], int degree)

    根据前驱曲线和后继曲线来计算出合适的接合处


着色器功能
---------------------


Fragment shader
***********************

参数列表
-----------------------

=========  ===============  =========================  =======================
参数类型     数据类型          变量名                       说明
=========  ===============  =========================  =======================
in          ``vec2``        ``uv_coords``               uv 坐标系
in          ``vec2``        ``uv_b2``                   uv 坐标系下的 b2 控制点
in          ``float``       ``uv_stroke_width``         uv 坐标系下的线宽
in          ``vec4``        ``color``                   颜色
in          ``float``       ``uv_anti_alias_width``     uv 坐标系下的抗锯齿宽度
in          ``float``       ``has_prev``                是否有前驱曲线
in          ``float``       ``has_next``                是否有后继曲线
in          ``float``       ``bevel_start``             起始斜边
in          ``float``       ``bevel_end``               结束斜边
in          ``float``       ``angle_from_prev``         与前驱手柄的夹角
in          ``float``       ``angle_to_next``           与后继手柄的夹角
in          ``float``       ``bezier_degree``           贝塞尔曲线阶数
out         ``vec4``        ``frag_color``              片段颜色
=========  ===============  =========================  =======================


程序流程
***********************

.. admonition:: 注意

    该部分为笔者的个人理解，若有不当之处，欢迎批评指正。

上面的参数列表和函数，读者一定都看懵了吧。没错，笔者看着也很懵，在此我们仅仅阐述一下它的着色思想。


顶点着色器
-----------------------

从程序中读取顶点、前驱顶点、后继顶点、法向量、线宽、颜色，并向后传递。


几何着色器
-----------------------

二阶贝塞尔曲线是由三个控制点构成的，因此想要绘制这段曲线，首先需要创建能够覆盖这段曲线的图元，之后再通过片段着色器，将多余的部分抹去。

那么我们就开始考虑下面的一些情况：

-   如果这条曲线是直线，即中间控制点恰好为两端的中点，那么这段直线我们就按照矩形来绘制，因为这个矩形刚好可以完美覆盖这条直线。
-   如果这条曲线是弯曲的，我们需要创建一个图形来将这段曲线完全覆盖。

    于是我们首先会想到用三角形，因为前面贝塞尔曲线填充也提到过用三角形来覆盖弓形。但仔细思考，这样还有什么漏洞？

    我们想要的效果是，曲线从首部到尾部的宽度都是均匀的，而只使用三角形来覆盖它，就会导致首部和尾部有一小块没有被覆盖到。
    因此，我们还需要对这条底边进行扩展，变成一个五边形，这样就能完全覆盖这条曲线了。

    .. image:: https://mkcdn.tonycrane.cc/manimgl_assets/shaders/curve_stroke_primitive.png

    另外，还有一些处理逻辑，是根据上一段曲线和下一段曲线来推测曲线之间的转接点图元，这部分也被包含在了图元处理中。
    由于它的处理逻辑较为复杂，在此不过多阐述（绝对是因为笔者看不懂）

由此，我们创建了一系列矩形和五边形的图元，传给片段着色器进行真正的着色操作。


片段着色器
-----------------------

从几何着色器传来的一系列图元，我们依然是无脑地，直接将传来的颜色涂在片段上。这样曲线就已经上色完成了。而接下来要做的处理，
和之前讨论过的曲线填充方法类似，只需将不需要的片段擦去即可。

此处使用的依然是 sdf 符号距离函数，计算出在线宽范围内的片段，将片段之外的部分透明度都设置为 0，也就完成了着色的操作。

.. image:: https://mkcdn.tonycrane.cc/manimgl_assets/shaders/curve_stroke_shader.png

除此以外，就是一些曲线转接处的细节，此处不过多阐述。


流程图
***********************

.. image:: https://mkcdn.tonycrane.cc/manimgl_assets/shaders/quadratic_bezier_stroke_shader.svg
