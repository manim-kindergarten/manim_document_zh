Mobject类的属性和方法
======================

.. admonition:: 声明

   这一页是elteoremadebeethoven写的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/mobjects/mobjects.html>`_  我翻译+做笔记，把资料整合编辑成方便的文档格式，以方便查阅使用Manim。

详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>`  。

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tex.rst
   geometric.rst
   coord_system.rst
   brace.rst
   number_line_and_plane.rst
   value_tracker.rst
   decimal_numbers.rst
   functions.rst
   svgs_images.rst

Tree
----

::

    .
    ├── AbstractImage
    │   ├── ImageMobject
    │   └── ImageMobjectFromCamera
    ├── Mobject1D
    │   └── PointCloudDot
    ├── Mobject2D
    ├── PMobject
    │   └── Point
    ├── ValueTracker
    │   ├── ComplexValueTracker
    │   └── ExponentialValueTracker
    └── VMobject
        ├── AnnularSector
        │   └── Sector
        ├── Arc
        │   ├── ArcBetweenPoints
        │   │   ├── CurvedArrow
        │   │   └── CurvedDoubleArrow
        │   └── Circle
        │       ├── Annulus
        │       └── Dot
        ├── BraceLabel
        │   └── BraceText
        ├── CubicBezier
        ├── DashedMobject
        ├── Elbow
        ├── Ellipse
        ├── Grid
        ├── Line
        │   ├── Arrow
        │   │   ├── DoubleArrow
        │   │   └── Vector
        │   └── DashedLine
        ├── Matrix
        │   ├── DecimalMatrix
        │   ├── IntegerMatrix
        │   └── MobjectMatrix
        ├── NumberLine
        │   └── UnitInterval
        ├── NumberPlane
        │   └── ComplexPlane
        ├── ParametricFunction
        │   └── FunctionGraph
        ├── Polygon
        │   └── RegularPolygon
        ├── Rectangle
        │   ├── PictureInPictureFrame
        │   ├── RoundedRectangle
        │   ├── SampleSpace
        │   ├── ScreenRectangle
        │   │   └── FullScreenRectangle
        │   │       └── FullScreenFadeRectangle
        │   ├── Square
        │   └── SurroundingRectangle
        │       └── BackgroundRectangle
        ├── SVGMobject
        │   └── SingleStringTexMobject
        │       └── TexMobject
        │           ├── Brace
        │           ├── TexMobjectFromPresetString
        │           └── TextMobject
        │               ├── BulletedList
        │               └── Title
        ├── ThreeDVMobject
        ├── VectorizedPoint
        ├── VGroup
        │   ├── Axes
        │   │   └── ThreeDAxes
        │   ├── BarChart
        │   ├── Cross
        │   ├── Cube
        │   │   └── Prism
        │   └── ParametricSurface
        │       └── Sphere
        └── VMobjectFromSVGPathstring
            └── TexSymbol

.. automodule:: manimlib.mobject.mobject
    :members: Mobject,Group