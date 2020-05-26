Coordinate坐标系基础
====================

.. admonition:: 声明

    这一页是EulerTour写的教程,我只是翻译+学习笔记，github早就有很多教程，但是为了方便查询使用，我才整合这么一份文档。

By default, the scene in manim is made up by 8 x 14 grid. 在manimlib/constants.py中定义，可修改

高度FRAME_HEIGHT = 8.0，

宽度14=FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT=8*2560/1440）


The grid is addressed using a numpy
array in the form of [x, y, z]. For 2D animations only the x and y axes are used.

.. literalinclude:: ../assets/code/Coordinate/DotMap.py
    :linenos:

.. raw:: html

    <video width="700" height="394" controls>
        <source src="../_static/coordinate/DotMap.mp4" type="video/mp4">
    </video>

.. note::
  You can place objects outside this boundary, but it won't show up in the render.

Using Coordinates使用坐标系
--------------------------------

Coordinates are used for creating geometries (`VMobject` in manim) and animations.

Here coordinates are used to create this Polygon

.. literalinclude:: ../assets/code/Coordinate/CoorPolygon.py
   :linenos:



.. Image:: ../assets/coordinate/CoorPolygon.png
   :width: 700px

Coordinate Aliasing坐标别名
-----------------------------

From some animations typing a ``np.array`` everytime you need a coordinate can be tedious.
在manimlib/constants.pyy中，Manim provides aliases to the most common coordinates::

  UP == np.array([0, 1, 0])
  DOWN == np.array([0, -1, 0])
  LEFT ==  np.array([-1, 0, 0])
  RIGHT == np.array([1, 0, 0])
  UL == np.array([-1, 1, 0])
  DL == np.array([-1, -1, 0])
  UR == np.array([1, 1, 0])
  DR == np.array([1, -1, 0])

Here coordinates are used for animations

.. literalinclude:: ../assets/code/Coordinate/CoorAlias.py
   :linenos:

.. raw:: html

    <video width="700" height="394" controls>
        <source src="../_static/coordinate/CoorAlias.mp4" type="video/mp4">
    </video>

Coordinate Arithmetic坐标运算
----------------------------------------

Numpy array allows arithmetic operations::

  >>> numpy.array([2,2,0]) + 4
  array([6, 6, 4])

  >>> np.array([1, -3, 0]) + np.array([-4, 2, 0])
  array([-3, -1,  0])

  >>> np.array([2, 2, 0]) - np.array([3,6, 0])
  array([-1, -4,  0])

  >>> numpy.array([2,2,0]) - 3
  array([-1, -1, -3])

  >>> np.array([1, -3, 0]) * 3
  array([ 3, -9,  0])

  >>> numpy.array([2,2,0]) / 2
  array([1., 1., 0.])

  >>> numpy.array([2,2,0]) / numpy.array([1, 4, 0])
  __main__:1: RuntimeWarning: invalid value encountered in true_divide
  array([2. , 0.5, nan])


.. literalinclude:: ../assets/code/Coordinate/CoorArithmetic.py
   :linenos:


.. raw:: html

    <video width="700" height="394" controls>
        <source src="../_static/coordinate/CoorArithmetic.mp4" type="video/mp4">
    </video>
