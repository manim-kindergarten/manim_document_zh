Space_ops
=========

``manimlib/utils/space_ops.py`` 这个文件中主要实现了和空间坐标计算有关的函数


-----

.. autofunction:: manimlib.utils.space_ops.get_norm

返回向量vect的模长

-----

.. autofunction:: manimlib.utils.space_ops.quaternion_mult

返回两个 *四元数* q1,q2相乘的乘积

-----

.. autofunction:: manimlib.utils.space_ops.quaternion_from_angle_axis

根据 *轴-角* 确定用于旋转的 *四元数*
返回\ ``[cos(angle/2), sin(abgle/2)*axis]``

-----

.. autofunction:: manimlib.utils.space_ops.angle_axis_from_quaternion

返回从四元数确定旋转的轴和角

-----

.. autofunction:: manimlib.utils.space_ops.quaternion_conjugate

返回quaternion的共轭四元数

-----

.. autofunction:: manimlib.utils.space_ops.rotate_vector

返回将vector以axis为轴，旋转angle角度后的向量

-  若vector是二维ndarray，则使用复数运算
-  若vector是三维ndarray，则使用四元数运算


-----

.. autofunction:: manimlib.utils.space_ops.thick_diagonal

返回一个dim*dim大小，对角线宽度为thickness的方阵

-----

.. autofunction:: manimlib.utils.space_ops.rotation_matrix

返回通过角angle轴axis确定的旋转矩阵

-----

.. autofunction:: manimlib.utils.space_ops.rotation_about_z

返回沿z轴旋转angle的旋转矩阵

-----

.. autofunction:: manimlib.utils.space_ops.z_to_vector

返回可以使z轴方向旋转到vector方向的变换矩阵

-----

.. autofunction:: manimlib.utils.space_ops.angle_between

返回两向量v1,v2的夹角

-----

.. autofunction:: manimlib.utils.space_ops.angle_of_vector

返回vector在xy平面投影的极坐标系下的theta

-----

.. autofunction:: manimlib.utils.space_ops.angle_between_vectors

返回两向量v1,v2的夹角

-----

.. autofunction:: manimlib.utils.space_ops.normalize

返回vect的单位向量

-  若vect为零向量，且fall_back=None，返回零向量
-  若vect为零向量，且fall_back不为None，返回fall_back


-----

.. autofunction:: manimlib.utils.space_ops.cross

返回两向量v1,v2的叉积

-----

.. autofunction:: manimlib.utils.space_ops.get_unit_normal

返回向量v1,v2确定的平面的法向量

-----

.. autofunction:: manimlib.utils.space_ops.compass_directions

将TAU分成n份，从start_vect开始返回沿每个方向的单位向量

-----

.. autofunction:: manimlib.utils.space_ops.complex_to_R3

复数转化为坐标（z轴为0）

-----

.. autofunction:: manimlib.utils.space_ops.R3_to_complex

取坐标前两轴为复数

-----

.. autofunction:: manimlib.utils.space_ops.complex_func_to_R3_func

将针对复数的函数转化为针对坐标的函数

-----

.. autofunction:: manimlib.utils.space_ops.center_of_mass

返回点集points的重心

-----

.. autofunction:: manimlib.utils.space_ops.midpoint

返回point1，point2的中点

-----

.. autofunction:: manimlib.utils.space_ops.line_intersection

返回两直线交点

-  **注意：** 需要使用\ ``get_start_and_end()``


-----

.. autofunction:: manimlib.utils.space_ops.get_winding_number

返回卷绕数


