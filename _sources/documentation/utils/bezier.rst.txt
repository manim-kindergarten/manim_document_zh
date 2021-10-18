Bezier
======

``manimlib/utils/bezier.py`` 这个文件中主要实现了和贝塞尔曲线、插值有关的函数

------

.. autofunction:: manimlib.utils.bezier.bezier

| 返回由点集(锚点，控制点)确定的参数方程
| 贝塞尔曲线的次数由 points 中点的个数确定

------

.. autofunction:: manimlib.utils.bezier.partial_bezier_points

| 给出贝塞尔曲线的点数组和两个 01 之间的数 ab
| 返回一个大小相同的数组，该数组描述原始贝塞尔曲线在间隔 [a,b] 上的部分

------

.. autofunction:: manimlib.utils.bezier.partial_quadratic_bezier_points

| 给出二阶贝塞尔曲线的点数组和两个 01 之间的数 ab
| 返回一个大小相同的数组，该数组描述原始二阶贝塞尔曲线在间隔 [a,b] 上的部分

------

.. autofunction:: manimlib.utils.bezier.interpolate

线性插值

------

.. autofunction:: manimlib.utils.bezier.set_array_by_interpolation

传入两个大小相同的数组，返回一个相同大小的数组，其中包含的元素为每个对应元素的插值

------

.. autofunction:: manimlib.utils.bezier.integer_interpolate

整数插值，返回两个数，第一个为插值结果(整数)，第二个为和线性插值相差的小数部分

------

.. autofunction:: manimlib.utils.bezier.mid

返回 (start+end)/2，start 和 end 可以是任意类型

------

.. autofunction:: manimlib.utils.bezier.inverse_interpolate

由插值的结果 value，返回 alpha

------

.. autofunction:: manimlib.utils.bezier.match_interpolate

| 匹配插值，给出原插值范围 old_start, old_end 和结果 old_value
| 返回以相同比例，插值范围为 new_start, new_end 的插值结果

------

.. autofunction:: manimlib.utils.bezier.get_smooth_quadratic_bezier_handle_points

给出一系列锚点 points，返回经过 points 的平滑贝塞尔曲线的一系列控制点

------

.. autofunction:: manimlib.utils.bezier.diag_to_matrix

| 用矩阵以对角线形式填充矩阵
| l, u 为非零下上对角线数，diag 为将以对角线形式填充的矩阵

------

.. autofunction:: manimlib.utils.bezier.is_closed

检查曲线是否闭合(首尾锚点重合)