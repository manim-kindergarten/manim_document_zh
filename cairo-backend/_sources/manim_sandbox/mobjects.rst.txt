自定义物体
============

angle.py
----------

.. autoclass:: manim_sandbox.utils.mobjects.angle.Angle

pdcxs写的关于角的类

用法: ``Angle(p1, p2, p3)``, ``p1, p2, p3`` 应该按逆时针顺序， 
``p2`` 是顶点， ``is_right=True`` 始终是直角， ``not_right`` 始终不是直角。
``is_right`` 和 ``not_right`` 都是 ``False`` 时，根据值来选择


Arc_group.py
-------------

.. autoclass:: manim_sandbox.utils.mobjects.Arc_group.Angle

cigar666写的关于角的类，更复杂好看一些


ColorText.py
---------------

.. autoclass:: manim_sandbox.utils.mobjects.ColorText.ColorText

自动呈现颜色，可以传入hex/rgb数组

.. autoclass:: manim_sandbox.utils.mobjects.ColorText.DecimalNumberText

同 ``DecimalNumber`` 使用 ``Text`` 代替 ``TextMobject``。
可以通过 ``text_config={"font": "..."}`` 来更换数字字体。


fractal_tree.py
-----------------

.. autoclass:: manim_sandbox.utils.mobjects.fractal_tree.BaseTree

可以看同文件里的其他例子


Grear.py
---------

几个齿轮类


intersection.py
------------------

1. 主要用来求解两圆和多圆相交的交集部分的示意（如果是空集会出问题）
2. ``Intersection_n_circle`` 是没有基于前两个类的，其实就用它也就行了
3. 可以用来做一些类似文氏图之类的，其他凸区域的交集可使用类似的方法写出来（如果谁有兴趣可以写一下


MyBoxes.py
-------------

.. autoclass:: manim_sandbox.utils.mobjects.MyBoxes.MyBox

单个Box，可以更新高度，上下位置，和类3D的颜色

.. autoclass:: manim_sandbox.utils.mobjects.MyBoxes.MyBoxes

一堆Box，可以根据数组或者函数更新高度、上下位置和颜色


MyText.py
-----------

.. autoclass:: manim_sandbox.utils.mobjects.MyText.MyText

可以修改字体的公式，根据TexMobject定位，然后用Unicode字符替换特殊符号


MyTriangle.py
---------------

.. autoclass:: manim_sandbox.utils.mobjects.MyTriangle.MyTriangle

由MATHEART_EVER和我是害羞的向量制作

功能：支持求三角形的周长，面积，五心，以及内切圆，外接圆，旁切圆，欧拉圆等


Object_Border.py
------------------

显示一个物体上下左右的边界，对教程有用

.. autoclass:: manim_sandbox.utils.mobjects.Object_Border.CtrlT

.. autoclass:: manim_sandbox.utils.mobjects.Object_Border.BorderNoneUpdate


PeriodicTable.py
------------------

.. autoclass:: manim_sandbox.utils.mobjects.PeriodicTable.PeriodicTable

基于 ``MyBoxes`` 的元素周期表


Right_angle.py
---------------

.. autoclass:: manim_sandbox.utils.mobjects.Right_angle.Right_angle

直角符号


Rubik_Cube.py
--------------

.. autoclass:: manim_sandbox.utils.mobjects.Rubik_Cube.Cube_array

方块序列

.. autoclass:: manim_sandbox.utils.mobjects.Rubik_Cube.Rubik_Cube

魔方类


Shadow_arround.py
---------------------

.. autoclass:: manim_sandbox.utils.mobjects.Shadow_around.Shadow_around

1. 这个类用来创建一个轮廓形状产生的阴影（有边缘的模糊效果）
2. 这个类尚不完善，对圆形、接近圆的椭圆和多边形等效果还凑合，对于其他形状可能和预期的阴影效果不一样
3. 本质上是一个渐变效果，所以通过改动CONFIG或其他参数可以用来表示其他类似渐变效果


ThreeBody.py
--------------

.. autoclass:: manim_sandbox.utils.mobjects.ThreeBody.Sun

恒星，带有阴影

.. autoclass:: manim_sandbox.utils.mobjects.ThreeBody.Three_Body

三体系统，实现自动模拟


ThreeDVector.py
-----------------

三维向量

.. autoclass:: manim_sandbox.utils.mobjects.ThreeDVector.ThreeDVector


Trail.py
---------

.. autoclass:: manim_sandbox.utils.mobjects.Trail.Trail

轨迹类，末尾轨迹自动变小到消失


VideoProgressBar.py
----------------------

.. autoclass:: manim_sandbox.utils.mobjects.VideoProgressBar.VideoProgressBar

教程系列的底端进度条

