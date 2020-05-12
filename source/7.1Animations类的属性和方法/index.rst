Animations类的属性和方法
========================


.. admonition:: 声明

   这一页是elteoremadebeethoven写的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animation.html>`_  我翻译+做笔记，把资料整合编辑成方便的文档格式，以方便查阅使用Manim。

详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>`  。

.. autoclass:: manimlib.animation.animation.Animation

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
   indication.rst
   
   movement.rst

Rate functions
--------------

See

::

    manimlib/utils/rate_functions.py

.. literalinclude:: ../manimlib/utils/rate_functions.py
    :lines: 7-77

Submobject modes
----------------

::

    "lagged_start"
    "smoothed_lagged_start"
    "one_at_a_time"
    "all_at_once"

See ``get_sub_alpha`` from:

::

    manimlib/animation/animation.py

.. literalinclude:: ../manimlib/animation/animation.py
    :lines: 94-107
    :lineno-start: 107

Tree
----

::

    .
    ├── AnimationGroup
    │   ├── AnimationOnSurroundingRectangle
    │   │   ├── ShowCreationThenDestructionAround
    │   │   ├── ShowCreationThenFadeAround
    │   │   └── ShowPassingFlashAround
    │   └── Flash
    ├── ApplyToCenters
    ├── ChangingDecimal
    │   └── ChangeDecimalToValue
    ├── DrawBorderThenFill
    │   └── Write
    ├── EmptyAnimation
    ├── Homotopy
    │   ├── ApplyWave
    │   ├── ComplexHomotopy
    │   └── SmoothedVectorizedHomotopy
    ├── LaggedStart
    ├── MaintainPositionRelativeTo
    ├── MoveAlongPath
    ├── PhaseFlow
    ├── Rotating
    ├── ShowIncreasingSubsets
    ├── ShowPartial
    │   ├── ShowCreation
    │   │   └── Uncreate
    │   └── ShowPassingFlash
    │       └── ShowCreationThenDestruction
    ├── Succession
    │   └── ShowCreationThenFadeOut
    ├── Transform
    │   ├── FadeIn
    │   ├── FadeInAndShiftFromDirection
    │   │   └── FadeInFromDown
    │   ├── FadeInFromLarge
    │   ├── FadeOut
    │   │   └── FadeOutAndShift
    │   │       └── FadeOutAndShiftDown
    │   ├── FocusOn
    │   ├── GrowFromPoint
    │   │   ├── GrowArrow
    │   │   ├── GrowFromCenter
    │   │   │   └── SpinInFromNothing
    │   │   └── GrowFromEdge
    │   ├── Indicate
    │   │   └── CircleIndicate
    │   ├── Rotate
    │   ├── ShrinkToCenter
    │   └── TurnInsideOut
    ├── UpdateFromAlphaFunc
    ├── UpdateFromFunc
    ├── VFadeIn
    ├── Vibrate
    └── WiggleOutThenIn
