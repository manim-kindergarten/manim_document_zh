Space_ops
=================

``manimlib/utils/space_ops.py`` 这个文件中主要实现了和空间坐标计算有关的函数


-----

.. autofunction:: manimlib.utils.space_ops.get_norm

返回向量 vect 的模长

-----

.. autofunction:: manimlib.utils.space_ops.quaternion_mult

返回两个 *四元数* q1, q2 相乘的乘积

-----

.. autofunction:: manimlib.utils.space_ops.quaternion_from_angle_axis

根据 *轴-角* 确定用于旋转的 *四元数*
返回\ ``[cos(angle/2), sin(angle/2)*axis]``

-----

.. autofunction:: manimlib.utils.space_ops.angle_axis_from_quaternion

返回从四元数确定旋转的轴和角

-----

.. autofunction:: manimlib.utils.space_ops.quaternion_conjugate

返回 quaternion 的共轭四元数

-----

.. autofunction:: manimlib.utils.space_ops.rotate_vector

返回将vector以axis为轴，旋转angle角度后的向量

-  若 vector 是二维 ndarray，则使用复数运算
-  若 vector 是三维 ndarray，则使用四元数运算


-----

.. autofunction:: manimlib.utils.space_ops.thick_diagonal

返回一个 dim*dim 大小，对角线宽度为 thickness 的方阵

-----

.. autofunction:: manimlib.utils.space_ops.rotation_matrix_transpose_from_quaternion

返回通过四元数确定的旋转矩阵（但是转置的）

-----

.. autofunction:: manimlib.utils.space_ops.rotation_matrix_from_quaternion

返回通过四元数确定的旋转矩阵

-----

.. autofunction:: manimlib.utils.space_ops.rotation_matrix_transpose

返回通过角 angle 轴 axis 确定的旋转矩阵（但是转置的）

-----

.. autofunction:: manimlib.utils.space_ops.rotation_matrix

返回通过角 angle 轴 axis 确定的旋转矩阵

-----

.. autofunction:: manimlib.utils.space_ops.rotation_about_z

返回沿 z 轴旋转 angle 的旋转矩阵

-----

.. autofunction:: manimlib.utils.space_ops.z_to_vector

返回可以使 z 轴方向旋转到 vector 方向的变换矩阵

-----

.. autofunction:: manimlib.utils.space_ops.angle_of_vector

返回 vector 在 xy 平面投影的极坐标系下的 theta

-----

.. autofunction:: manimlib.utils.space_ops.angle_between_vectors

返回两向量 v1, v2 的夹角

-----

.. autofunction:: manimlib.utils.space_ops.project_along_vector

点在向量上的投影

-----

.. autofunction:: manimlib.utils.space_ops.normalize

返回 vect 的单位向量

-  若 vect 为零向量，且 fall_back=None，返回零向量
-  若 vect 为零向量，且 fall_back不为None，返回 fall_back

-----

.. autofunction:: manimlib.utils.space_ops.normalize_along_axis

将所有向量沿 axis 单位化

-----

.. autofunction:: manimlib.utils.space_ops.cross

返回两向量 v1, v2 的叉积

-----

.. autofunction:: manimlib.utils.space_ops.get_unit_normal

返回向量 v1, v2 确定的平面的法向量

-----

.. autofunction:: manimlib.utils.space_ops.compass_directions

将 TAU 分成 n 份，从 start_vect 开始返回沿每个方向的单位向量

-----

.. autofunction:: manimlib.utils.space_ops.complex_to_R3

复数转化为坐标（z 轴为 0）

-----

.. autofunction:: manimlib.utils.space_ops.R3_to_complex

取坐标前两轴为复数

-----

.. autofunction:: manimlib.utils.space_ops.complex_func_to_R3_func

将针对复数的函数转化为针对坐标的函数

-----

.. autofunction:: manimlib.utils.space_ops.center_of_mass

返回点集 points 的重心

-----

.. autofunction:: manimlib.utils.space_ops.midpoint

返回 point1，point2 的中点

-----

.. autofunction:: manimlib.utils.space_ops.line_intersection

返回两直线交点

-  **注意：** 需要使用\ ``get_start_and_end()``

.. code:: python

    p = line_intersection(
        l1.get_start_and_end(),
        l2.get_start_and_end()
    )

-----

.. autofunction:: manimlib.utils.space_ops.find_intersection

过 p0 点，v0 向量方向上的射线 l1，与过 p1 点，v1 的向量上的射线 l2 的交点

如果是三维的情况，则返回两射线距离最近的点

-----

.. autofunction:: manimlib.utils.space_ops.get_closest_point_on_line

找到点 p 到 线段 ab 距离最近的点 x

- 如果 p 点投影在线段 ab 上，则返回垂足
- 如果 p 点投影不在线段 ab 上，则返回与投影最接近的线段端点

-----

.. autofunction:: manimlib.utils.space_ops.get_winding_number

返回卷绕数

-----

.. autofunction:: manimlib.utils.space_ops.cross2d

二阶矩阵相乘，如果 a 不是二阶矩阵，则返回 
``a[0] * b[1] - b[0] * a[1]``

-----

.. autofunction:: manimlib.utils.space_ops.tri_area

-----

.. autofunction:: manimlib.utils.space_ops.is_inside_triangle

判断点 p 是否在点 a, b, c 构成的三角形中

-----

.. autofunction:: manimlib.utils.space_ops.norm_squared

三维向量模长平方

（似乎可以用其他方法计算任意维度向量模长平方，例如 ``(v ** 2).sum()`` ）

-----

.. autofunction:: manimlib.utils.space_ops.earclip_triangulation

三角剖分

