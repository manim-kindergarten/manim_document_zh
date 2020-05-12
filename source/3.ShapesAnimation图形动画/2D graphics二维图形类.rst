2D graphics二维图形类
======================

.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是想把Markdown、pdf等资料整合编辑成方便的文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。


二维图形类
-------------

** \\manimlib\\mobject\\geometry.py **

TODO：待完善



1 点Dot
~~~~~~~~~

.. code:: python

   CONFIG = {
           "radius": DEFAULT_DOT_RADIUS,
           "stroke_width": 0,
           "fill_opacity": 1.0,
           "color": WHITE
       }



2 圆形Circle
~~~~~~~~~~~~~~

继承自Arc

.. code:: python

   CONFIG = {
           "color": RED,
           "close_new_points": True,
           "anchors_span_full_range": False
       }



3 环Annulus
~~~~~~~~~~~~~

继承自圆形

.. code:: python

   CONFIG = {
           "inner_radius": 1,
           "outer_radius": 2,
           "fill_opacity": 1,
           "stroke_width": 0,
           "color": WHITE,
           "mark_paths_closed": False,
       }



4 长方形Rectangle
~~~~~~~~~~~~~~~~~~~

.. code:: python

   CONFIG = {
           "color": WHITE,
           "height": 2.0,
           "width": 4.0,
           "mark_paths_closed": True,
           "close_new_points": True,
       }



5 方形Square
~~~~~~~~~~~~~~

继承自长方形

.. code:: python

    CONFIG = {
        	# 边长
           "side_length": 2.0,
       }



6 椭圆Ellipse
~~~~~~~~~~~~~~~

继承自圆形

.. code:: python

   CONFIG = {
           "width": 2,
           "height": 1
       }



7 弧Arc
~~~~~~~~~

.. code:: python

   CONFIG = {
           "radius": 1.0,
           "num_components": 9,
           "anchors_span_full_range": True,
           "arc_center": ORIGIN,
       }



8 线Line
~~~~~~~~~~

**Line(start=LEFT, end=RIGHT, \*\*kwargs)**

start,end:起点终点，形式是np向量

kwargs为配置信息，继承自VMobject

.. code:: python

   CONFIG = {
           "fill_color": None,
           "fill_opacity": 0.0,
           "stroke_color": None,
           "stroke_opacity": 1.0,
           "stroke_width": DEFAULT_STROKE_WIDTH,
           # The purpose of background stroke is to have
           # something that won't overlap the fill, e.g.
           # For text against some textured background
           "background_stroke_color": BLACK,
           "background_stroke_opacity": 1.0,
           "background_stroke_width": 0,
           # When a color c is set, there will be a second color
           # computed based on interpolating c to WHITE by with
           # sheen_factor, and the display will gradient to this
           # secondary color in the direction of sheen_direction.
           "sheen_factor": 0.0,
           "sheen_direction": UL,
           # Indicates that it will not be displayed, but
           # that it should count in parent mobject's path
           "close_new_points": False,
           "pre_function_handle_to_anchor_scale_factor": 0.01,
           "make_smooth_after_applying_functions": False,
           "background_image_file": None,
           "shade_in_3d": False,
           # This is within a pixel
           # TODO, do we care about accounting for
           # varying zoom levels?
           "tolerance_for_point_equality": 1e-6,
           "n_points_per_cubic_curve": 4,
       }
