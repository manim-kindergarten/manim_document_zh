二阶贝塞尔曲线轮廓线着色 Quadratic bezier stroke
====================================================


Vertex shader
***********************

参数列表
-----------------------

=========  ===============  =========================  ======================
参数类型     数据类型          变量名                       说明
=========  ===============  =========================  ======================
in          ``vec3``        ``point``
in          ``vec3``        ``prev_point``
in          ``vec3``        ``next_point``
in          ``vec3``        ``unit_normal``
in          ``float``       ``stroke_width``
in          ``vec4``        ``color``
out         ``vec3``        ``bp``
out         ``vec3``        ``prev_bp``
out         ``vec3``        ``next_bp``
out         ``vec3``        ``v_global_unit_normal``
out         ``float``       ``v_stroke_width``
out         ``vec4``        ``v_color``
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

=========  ===============  ============================  ========================
参数类型     数据类型          变量名                          说明
=========  ===============  ============================  ========================
uniform     此处省略           此处省略                       用于坐标变换和光照
in          ``vec3``         ``bp[3]``                      bezier s[3], vec2 prev[3], vec2 prev[3], vec2 next[3],  point
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
out         ``float``        ``bevel_start``                斜边起点
out         ``float``        ``bevel_end``                  斜边终点
out         ``float``        ``angle_from_prev``            
out         ``float``        ``angle_to_next``
out         ``float``        ``bezier_degree``              贝塞尔曲线阶数
out         ``vec2``         ``uv_coords``                  uv 坐标系
out         ``vec2``         ``uv_b2``                      uv 坐标下的顶点 b2
=========  ===============  ============================  ========================

函数列表
-----------------------

.. cpp:function:: void flatten_points(vec3 points[3], vec2 flat_points[3])

    - ``points`` 为输入参数
    - ``flat_point`` 为输出参数

    似乎是透视投影

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

    寻找贝塞尔曲线边界的角，可以作为三角扇形发出

    - 当图形的边为直线时，生成的角落是一个四边形
    - 当图形的边为曲线时，生成的角落为五边形

.. cpp:function:: void set_adjascent_info(vec2 c0, vec2 tangent, int degree, vec2 adj[3], float bevel, float angle)

    - ``bevel`` 和 ``angle`` 为输出参数

.. cpp:function:: void find_joint_info(vec2 controls[3], vec2 prev[3], vec2 prev[3], vec2 next[3], int degree)


