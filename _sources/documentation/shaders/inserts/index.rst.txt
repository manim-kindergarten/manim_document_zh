Inserts 
===================

在 C++ 中，OpenGL 着色器中没有类似 ``#include`` 的替代品。虽然有其他选择，但是很多不好，特别是如果目标是在着色器文件中共享代码，这种方式不是很好。
因此，manim 目前的方式是使用 ``#INSERT <file_name>`` 的方式来将 ``insert`` 目录下的代码插入到对应的文件中。

这个文件的函数包含了对 uniform 变量的引用，通过这种插入的方式将 uniform 变量引入到 glsl 代码上下文中。简言之，相当于在 glsl 中使用了 ``#include``。


add light
*************

添加光照

- 该文件可插入 color_map function

-----------------

.. cpp:function:: vec4 add_light(vec4 color, vec3 point, vec3 unit_normal, vec3 light_coords, float gloss, float shadow)
    
    - 可插入 color function

-----------------

.. cpp:function:: vec4 finalize_color(vec4 color, vec3 point, vec3 unit_normal, vec3 light_coords, float gloss, float shadow)

-----------------


camera uniform delarations
*******************************

声明与相机有关的全局变量

==============  ======================  ===================================
数据类型          变量名                    说明
==============  ======================  ===================================
``vec2``        ``frame_shape``         帧大小
``float``       ``anti_alias_width``    抗锯齿宽度
``vec3``        ``camera_offset``       相机偏移量
``mat3``        ``camera_rotation``     相机旋转矩阵
``float``       ``is_fixed_in_frame``   是否固定在场景中
``float``       ``focal_distance``      焦距
==============  ======================  ===================================


complex functions
*******************************

复数运算

.. cpp:function:: vec2 complex_mult(vec2 z, vec2 w)

    复数相乘

-----------------

.. cpp:function:: vec2 complex_div(vec2 z, vec2 w)

    复数相除

-----------------

.. cpp:function:: vec2 complex_pow(vec2 z, int n)

    复数幂次

-----------------

finalize color
*******************************

确定颜色

.. cpp:function:: vec3 float_to_color(float value, float min_val, float max_val, vec3 colormap_data[9])

    将输入的浮点数值在给定范围 ``[min_val, max_bal]`` 内映射到 color_map 上，返回的是颜色的 rgb 值

-----------------

.. cpp:function:: vec4 add_light(vec4 color, vec3 point, vec3 unit_normal, vec3 light_coords, vec3 cam_coords, float reflectiveness, float gloss, float shadow)

-----------------

.. cpp:function:: vec4 finalize_color(vec4 color, vec3 point, vec3 unit_normal, vec3 light_coords, vec3 cam_coords, float reflectiveness, float gloss, float shadow)

    - 可插入 color function

-----------------

get gl Position
*******************************

.. cpp:var:: const vec2 DEFAULT_FRAME_SHAPE = vec2(8.0 * 16.0 / 9.0, 8.0)

    默认帧大小

-----------------

.. cpp:function:: float perspective_scale_factor(float z, float focal_distance)

    透视缩放倍率

-----------------

.. cpp:function:: vec4 get_gl_Position(vec3 point)

    将 manim 的坐标转换到 OpenGL 中的坐标

-----------------


get rotated surface unit normal vector
**************************************************************

.. cpp:function:: vec3 get_rotated_surface_unit_normal_vector(vec3 point, vec3 du_point, vec3 dv_point)

    获取旋转的曲面单位法向量

-----------------


get unit normal
**************************************************************

.. cpp:function:: vec3 get_unit_normal(vec3 points[3])

    根据平面上的三个点，获取该平面的单位法向量

-----------------


position point into frame
**************************************************************

.. cpp:function:: vec3 rotate_point_into_frame(vec3 point)

    将坐标映射到相机旋转下的点坐标

-----------------

.. cpp:function:: vec3 position_point_into_frame(vec3 point)

    调用了上面的方法，将点放到帧中

-----------------


quadratic bezier distance
**************************************************************

.. cpp:function:: vec2 bezier(float t, vec2 b2)

    假设 ``b0 = (0, 0)`` , ``b1 = (1, 0)`` , ``b2 = (x, y)`` ，返回 b0, b1, b2 之间的二阶贝塞尔插值。
    即有 :math:`\begin{bmatrix} 2t(1-t)+t^2 x \\ t^2 y \end{bmatrix}`

-----------------

.. cpp:function:: float cube_root(float x)

    计算立方根

-----------------

.. cpp:function:: int cubic_solve(float a, float b, float c, float d, float roots[3])

    - ``roots[3]`` 为输出参数

    解出一元三次方程的实根，返回值为实根个数

-----------------

.. cpp:function:: float dist_to_line(vec2 p, vec2 b2)

    点到线段的距离

-----------------

.. cpp:function:: float dist_to_point_on_curve(vec2 p, float t, vec2 b2)

    点到贝塞尔曲线上某一点的距离

-----------------

.. cpp:function:: float min_dist_to_curve(vec2 p, vec2 b2, float degree)

    点到贝塞尔曲线上的最小距离

-----------------


quadratic bezier geometry functions
**************************************************************

.. cpp:function:: float cross2d(vec2 v, vec2 w)

    二维向量点乘

-----------------

.. cpp:function:: mat3 get_xy_to_uv(vec2 b0, vec2 b1)

    从 manim 坐标系变换映射到 uv 变换

-----------------

.. cpp:function:: mat4 get_xyz_to_uv(vec3 b0, vec3 b1, vec3 unit_normal)

    将正交矩阵转换为定义好的 uv 空间使 b0 变成 [0,0], b1 变成 [1,0]

-----------------

.. cpp:function:: float get_reduced_control_points(vec3 points[3], vec3 new_points[3])

    - ``points[3]`` 为输入参数
    - ``new_points[3]`` 为输出参数

    - 对于零曲线
        - ``new_points`` 均为 ``points[0]``
        - 返回 0
    - 对于单线段
        - ``new_points[0]`` 为 ``points[0]``
        - ``new_points[1]`` 为 ``(points[0] + points[2]) / 2``
        - ``new_points[2]`` 为 ``points[2]``
        - 返回 1
    - 对于二次贝塞尔曲线
        - ``new_points[i]`` 分别为 ``points[i]``, ``i = 0, 1, 2``
        - 返回 2




