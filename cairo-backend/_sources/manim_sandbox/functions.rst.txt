自定义工具函数
====================

debugTeX.py
------------

.. autofunction:: manim_sandbox.utils.functions.debugTeX.debugTeX

用于显示TexMobject或TextMobject的下标，用法：

.. code:: python

    text = TextMobject("abc")
    self.add(text)
    debugTeX(self, text[0])

calculation.py
---------------

.. autofunction:: manim_sandbox.utils.functions.calculation.get_intersect

获取两直线 ``line1``, ``line2`` 的交点，如果平行，则返回 ``parallel``

**以下是一些rate_func**：

.. autofunction:: manim_sandbox.utils.functions.calculation.easeOutBounce

.. autofunction:: manim_sandbox.utils.functions.calculation.easeInBounce

.. autofunction:: manim_sandbox.utils.functions.calculation.easeInOutBounce

.. autofunction:: manim_sandbox.utils.functions.calculation.easeOutElastic
