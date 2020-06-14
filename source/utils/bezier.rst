Bezier
======

``manimlib/utils/bezier.py`` 这个文件中主要实现了和贝塞尔曲线、插值有关的函数

------

.. autofunction:: manimlib.utils.bezier.bezier

| 返回由点集(锚点，控制点)确定的参数方程
| 贝塞尔曲线的次数由points中点的个数确定

------

.. autofunction:: manimlib.utils.bezier.partial_bezier_points

| 给出贝塞尔曲线的点数组和两个01之间的数ab
| 返回一个大小相同的数组，该数组描述原始贝塞尔曲线在间隔[a,b]上的部分

------

.. autofunction:: manimlib.utils.bezier.interpolate

线性插值

------

.. autofunction:: manimlib.utils.bezier.integer_interpolate

整数插值，返回两个数，第一个为插值结果(整数)，第二个为和线性插值相差的小数部分

------

.. autofunction:: manimlib.utils.bezier.mid

返回(start+end)/2，start和end可以是任意类型

------

.. autofunction:: manimlib.utils.bezier.inverse_interpolate

由插值的结果value，返回alpha

------

.. autofunction:: manimlib.utils.bezier.match_interpolate

| 匹配插值，给出原插值范围old_start,old_end和结果old_value
| 返回以相同比例，插值范围为new_start,new_end的插值结果

------

.. autofunction:: manimlib.utils.bezier.get_smooth_handle_points

给出一系列锚点points，返回经过points的平滑贝塞尔曲线的一系列控制点

------

.. autofunction:: manimlib.utils.bezier.diag_to_matrix

| 用矩阵以对角线形式填充矩阵
| l,u为非零下上对角线数，diag为将以对角线形式填充的矩阵

------

.. autofunction:: manimlib.utils.bezier.is_closed

检查曲线是否闭合(首尾锚点重合)