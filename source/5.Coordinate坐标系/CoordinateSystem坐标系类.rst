coordinate坐标3D
==================


.. admonition:: 声明

    早期Elteoremadebeethoven有个仓库和配套的youtude教学视频， `Animation course with Manim <https://github.com/Elteoremadebeethoven/AnimationsWithManim>`_ ，小破站有搬运 `BV1W4411Z7Zt <https://www.bilibili.com/video/BV1W4411Z7Zt>`_ ，
    然后cai-hust学习并且做了相关的教程MarkDown笔记   `cai-hust_manim-tutorial-CN <https://github.com/cai-hust/manim-tutorial-CN>`_ ，
    这部分不是我写的，我只是想把Markdown、pdf等资料整合编辑成方便的文档格式，以方便查阅使用Manim，cai-hust已授权，表示标明链接仓库就行。

坐标系类
------------



0 数轴类 NumberLine
~~~~~~~~~~~~~~~~~~~~~~

继承于Line,属性如下：

.. code:: python

   CONFIG = {
           "color": LIGHT_GREY,
           # X的范围
           "x_min": -FRAME_X_RADIUS,
           "x_max": FRAME_X_RADIUS,
           # 单元格的大小，默认和单位长度一致
           "unit_size": 1,
           # 是否包含刻度tick
           "include_ticks": True,
           # tick的尺寸，大小为：2个单位*tick_size
           "tick_size": 0.1,
           # tick的分布密度
           "tick_frequency": 1,
           # Defaults to value near x_min s.t. 0 is a tick
           # TODO, rename this
           "leftmost_tick": None,
           # Change name
           # 最长的tick,作者原意应该是作为数轴标识的tick,一般为中间的tick即原点，会画长一点
           "numbers_with_elongated_ticks": [0],
           # 标上数字
           "include_numbers": False,
           # 显示的数字格式
           "numbers_to_show": None,
           "longer_tick_multiple": 2,
           # 中间的数字
           "number_at_center": 0,
           "number_scale_val": 0.75,
           "label_direction": DOWN,
           "line_to_number_buff": MED_SMALL_BUFF,
           # 包含箭头
           "include_tip": False,
           # tip:箭头，下面两个是其尺寸设置
           "tip_width": 0.25,
           "tip_height": 0.25,
           "decimal_number_config": {
               "num_decimal_places": 0,
           },
           # 从数字标记中去掉0这个标记
           "exclude_zero_from_default_numbers": False,
       }

注意其中x\ *min，x*\ max均为帧的左右范围即每帧的最左边和最右边

.. figure:: ../assets/image/1567675075732.png
   :alt: 

本质上来说，数轴是一条线（Line），每一个间隔（tick）均为小的线(Line)

整个构建流程是，先画出横线作为坐标轴，然后从左到右画出一个个小竖线，最后增加数字，箭头等小部件



1 坐标系抽象类 CoordinateSystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   CONFIG = {
           "dimension": 2,
           "x_min": -FRAME_X_RADIUS,
           "x_max": FRAME_X_RADIUS,
           "y_min": -FRAME_Y_RADIUS,
           "y_max": FRAME_Y_RADIUS,
       }

主要的几个抽象方法：

**coords指的是坐标轴中的点的值,point指没有坐标轴时真实的坐标，在创建坐标轴时候中心设置在ORIGIN，坐标大小没有缩放的时候两者是一样的**

-  coords\ *to*\ point(\*coords)；c2p(\*coords):将坐标系中的点的坐标值转换为屏幕上的点

-  point\ *to*\ coords(point)；p2c(point)：coords\ *to*\ point逆方法

-  get_axes():得到CoordinateSystem对象，一般为包含x,y,z坐标的数组

-  get_axis(index):得到index对应的坐标，xyz坐标对应的index分别为1，2，3

-  get\ *x*\ axis();get\ *y*\ axis();get\ *z*\ axis()

-  get\ *axis*\ label一类：给对应的坐标（轴）添加标签，显示标签，并返回标签对象

   -  get\ *axis*\ label(label\ *tex, axis, edge, direction,
      buff=MED*\ SMALL_BUFF):

   -  get\ *axis*\ labels(x\ *label*\ tex="x", y\ *label*\ tex="y")：

   -  get\ *x*\ axis\ *label(label*\ tex, edge=RIGHT, direction=DL,
      \*\*kwargs)：

   -  get\ *y*\ axis\ *label(label*\ tex, edge=UP, direction=DR,
      \*\*kwargs):

   label_tex:坐标标签，使用latex字符串(TexMobject)

   axis:想获取的坐标标签的对应的坐标对象

   edge:四个边缘位置

   direction：在坐标轴的相对位置

   \*\*kwargs:其他在config内的配置，如颜色等，自行修改

get_graph(function, \*\*kwargs):给定方程，绘制图像并返回

get\ *parametric*\ curve(function,
\*\*kwargs):绘制给定参数曲线方程并返回

input\ *to*\ graph_point(x, graph):暂时没搞清楚啥玩意



2 二维坐标类 Axes
~~~~~~~~~~~~~~~~~~~~

继承CoordinateSystem

实质是创造两个NumberLine数轴，然后将其中一个按照中心旋转90度，作为Y轴，然后对X，Y轴进行其他的属性进行调整，所以配置里面有"number\ *line*\ config"

**Axes(\*\*kwargs)**

.. code:: python

   CONFIG = {
       	# 数轴的配置
           "number_line_config": {
               "color": LIGHT_GREY,
               "include_tip": True,
               "exclude_zero_from_default_numbers": True,
           },
       	# 横坐标轴和数轴的默认配置一样不需要修改
           "x_axis_config": {},
           "y_axis_config": {
               # 默认将“y”这个标签放在纵坐标轴的左侧
               "label_direction": LEFT,
           },
       	# 原点默认和帧图的中心点一致
           "center_point": ORIGIN,
       }

实现了：

1. coords\ *to*\ point(\*coords)；c2p(\*coords):将坐标系中的点的坐标值转换为屏幕（帧图）上的点

   分析一下源码：

.. code:: python

   def coords_to_point(self, *coords):
           # 将坐标轴中的原点0换算为对应的帧图中的坐标
           origin = self.x_axis.number_to_point(0)
           # 将帧图坐标转换为向量
           result = np.array(origin)
           # result = 原点对应的帧图的坐标+coord相对帧图中原点的坐标 = coord在帧图中的实际坐标
           for axis, coord in zip(self.get_axes(), coords):
               result += (axis.number_to_point(coord) - origin)
           return result

1. point\ *to*\ coords(point)；p2c(point)

增加了方法：

get\ *coordinate*\ labels(x\ *vals=None,
y*\ vals=None)：传入x,y标签的latex字符串，得到对应的x,y坐标轴的标签的对象

add\ *coordinates(x*\ vals=None,
y\ *vals=None):和get*\ coordinate_labels相似，但是将其加入了自己的成员变量并返回了自己



3 三维坐标系类 ThreeDAxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

继承自Axes

**ThreeDAxes(\*\*kwargs)**

.. code:: python

   CONFIG = {
           "dimension": 3,
           "x_min": -5.5,
           "x_max": 5.5,
           "y_min": -5.5,
           "y_max": 5.5,
           "z_axis_config": {},
           "z_min": -3.5,
           "z_max": 3.5,
           "z_normal": DOWN,
           "num_axis_pieces": 20,
           "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
       }



4 NumberPlane
~~~~~~~~~~~~~~~~



5 ComplexPlane
~~~~~~~~~~~~~~~~~

复数坐标系，继承于NumberPlane

.. code:: python

   # author:TB
   class ComplexPlaneScene(Scene):
       def construct(self):
           # See manimlib/mobject/number_line.py and coordinate_systems.py
           cp = ComplexPlane(
                           y_axis_config={"decimal_number_config":{"unit": "i"}},
                           number_line_config={"include_numbers":True}
                           )

           x_axis = cp[-2]
           y_axis = cp[-1]
           x_axis.set_color(RED)
           y_axis.set_color(PURPLE)

           x_labels = x_axis[1]
           x_labels.set_color(ORANGE)

           y_labels = y_axis[1]
           y_labels.set_color(YELLOW)
           for y in y_labels:
               y.rotate(-PI/2)

           x_label = TexMobject("x")
           x_label.move_to(cp.c2p(6.8,x_label.get_height()))
           y_label = TexMobject("y")
           y_label.move_to(cp.c2p(-y_label.get_width(),3.8))

           self.add(cp,x_label,y_label)

           self.wait()

