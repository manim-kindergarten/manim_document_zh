GraphScene二维坐标类 
====================


.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是想把Markdown、pdf等资料整合编辑成方便的文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。

二维坐标类 GraphScene
------------------------

**\\manimlib\scene\graph_scene.py**

继承自Scene类，用来绘制坐标

属性如下：

.. code:: python

   CONFIG = {
           "x_min": -1,
           "x_max": 10,
           "x_axis_width": 9,
           "x_tick_frequency": 1,
           "x_leftmost_tick": None,  # Change if different from x_min
           "x_labeled_nums": None,
           "x_axis_label": "$x$",
           "y_min": -1,
           "y_max": 10,
           "y_axis_height": 6,
           "y_tick_frequency": 1,
           "y_bottom_tick": None,  # Change if different from y_min
           "y_labeled_nums": None,
           "y_axis_label": "$y$",
           "axes_color": GREY,
           "graph_origin": 2.5 * DOWN + 4 * LEFT,
           "exclude_zero_label": True,
           "default_graph_colors": [BLUE, GREEN, YELLOW],
           "default_derivative_color": GREEN,
           "default_input_color": YELLOW,
           "default_riemann_start_color": BLUE,
           "default_riemann_end_color": GREEN,
           "area_opacity": 0.8,
           "num_rects": 50,
       }

一般流程是：

.. code:: python

   class Graph2D(GraphScene):
   	def x_2(self, x):
   		return x**2

   	def construct(self):
   		self.setup_axes(animate=True)
   		graph = self.get_graph(self.x_2,color = GREEN,x_min = 2,x_max = 4)
   		self.play(ShowCreation(graph),run_time = 2)
   		self.wait()

.. figure:: ../assets/image/1565835900946.png
   :alt: 



1 setup_axes()
~~~~~~~~~~~~~~~~

**setup_axes(animate=Bool)：**

默认没有动画效果，setup_axes(animate=True)则会显示动画



2 get_graph()
~~~~~~~~~~~~~~~

**get\ graph(func, color=None,x\ min=None,x_max=None, \*\*kwargs)**

得到坐标系的句柄，并设置值



3 coords\ *to*\ point()
~~~~~~~~~~~~~~~~~~~~~~~~~

**coords\ to\ point(x, y)**

坐标变成对应的帧中的点



4 point\ *to*\ coords()
~~~~~~~~~~~~~~~~~~~~~~~~~

**point\ to\ coords(point)**

帧中的点转换为坐标，返回x,y组成的元组



5 get\ *graph*\ label()
~~~~~~~~~~~~~~~~~~~~~~~~~

**get\ graph\ label(graph,label="f(x)", x\ val=None,direction=RIGHT,
buff=MED\ SMALL_BUFF, color=None)**

graph：从graph中获得坐标标签

label默认为“f(x)”,可以改成自己想要的函数

x_val：x的取值范围

buff：距离边界的距离

color：颜色



6 get\ *vertical*\ line\ *to*\ graph()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**get\ vertical\ line\ to\ graph(x,
graph,line\ class=Line,\*\*line\ kwargs)**

得到竖直线，起点为(x,0)终点为(x,f(x))

返回line_class类型的图像



7 get\ *vertical*\ lines\ *to*\ graph()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**get\ vertical\ lines\ to\ graph( graph,x\ min=None,x\ max=None,
num_lines=20, \*\*kwargs)**

同时得到画多条竖直线

返回line_class类型的VGroup



8 改变坐标标签的颜色
~~~~~~~~~~~~~~~~~~~~~~

   https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/6a\ *plots*\ 2D/change\ *label*\ colors.md#change-labels-colors-in-graphscene

   Change labels colors in ``GraphScene``

   Add this to the ``CONFIG`` dictionary:在CONFIG中加入：

   .. code:: 

       "x_label_color":RED,
       "y_label_color":BLUE

   In the ``setup_axes`` method change the
   lines：在源码的setup_axes中的两句：

   .. code:: 

               x_label = TextMobject(self.x_axis_label)
               # and
               y_label = TextMobject(self.y_axis_label)

   with改为

   .. code:: 

               x_label = TextMobject(self.x_axis_label,color=self.x_label_color)
               # and
               y_label = TextMobject(self.x_axis_label,color=self.y_label_color)

效果：

.. figure:: ../assets/image/ChanceColorLabels.png
   :alt: 




补充一个类似的案例：from  `manim-tutorial <https://github.com/malhotra5/Manim-Tutorial>`_   .  

.. literalinclude:: ../assets/code/manim-tutorial/graphing.py
   :linenos:


.. raw:: html

    <video width="700" height="394" controls>
        <source src="../_static/manim-tutorial/Graphing.mp4" type="video/mp4">
    </video>
