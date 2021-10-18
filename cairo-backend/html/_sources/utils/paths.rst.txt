Paths
=====

``manimlib/utils/paths.py`` 这个文件中主要实现了和路径有关的函数


-----

.. autofunction:: manimlib.utils.paths.straight_path

直线路径，和线性插值相同

-----

.. autofunction:: manimlib.utils.paths.path_along_arc

| 以 ``axis`` 为轴， ``arc_angle`` 为圆心角的圆弧路径
| 返回含有三个参数 ``(start_points, end_points, alpha)`` 的函数

-----

.. autofunction:: manimlib.utils.paths.clockwise_path

| 顺时针圆路径
| 返回含有三个参数 ``(start_points, end_points, alpha)`` 的函数

-----

.. autofunction:: manimlib.utils.paths.counterclockwise_path

| 逆时针圆路径
| 返回含有三个参数 ``(start_points, end_points, alpha)`` 的函数
