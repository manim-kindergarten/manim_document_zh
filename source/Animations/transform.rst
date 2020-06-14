Transform
==========

Transform
*****************
.. autoclass:: manimlib.animation.transform.Transform
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/TransformExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class TransformExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(3)
          B = TextMobject("Text-B").scale(3)
          C = TextMobject("C-Text").scale(3)
  
          self.add(A)
          self.wait()
          self.play(Transform(A, B))
          self.wait()
          self.play(Transform(A, C)) # notice here
          self.wait()


ReplacementTransform
********************
.. autoclass:: manimlib.animation.transform.ReplacementTransform
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ReplacementTransformExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ReplacementTransformExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(3)
          B = TextMobject("Text-B").scale(3)
          C = TextMobject("C-Text").scale(3)
  
          self.add(A)
          self.wait()
          self.play(ReplacementTransform(A, B))
          self.wait()
          self.play(ReplacementTransform(B, C)) # notice here
          self.wait()

**Transform和ReplacementTransform的区别**：

1. ``Transform(A, B)`` 在画面上 ``A`` 变成了 ``B`` 的样子，但是画面上的物体名字还叫 ``A``

2. ``ReplacementTransform(A, B)`` 在画面上 ``A`` 变成了 ``B`` 的样子，并且画面上的物体名字叫 ``B``

所以以下两个效果相同

::

   self.play(Transform(A, B))
   self.play(Transform(A, C))

::

   self.play(ReplacementTransform(A, B))
   self.play(ReplacementTransform(B, C))

TransformFromCopy
*****************
.. autoclass:: manimlib.animation.transform.TransformFromCopy
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/TransformFromCopyExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class TransformFromCopyExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(3)
          B = TextMobject("Text-B").scale(3).shift(UP*2)
  
          self.add(A)
          self.wait()
          self.play(TransformFromCopy(A, B))
          self.wait()


ClockwiseTransform
******************
.. autoclass:: manimlib.animation.transform.ClockwiseTransform
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ClockwiseTransformExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ClockwiseTransformExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(3)
          B = TextMobject("Text-B").scale(3).shift(UP*2)
  
          self.add(A)
          self.wait()
          self.play(ClockwiseTransform(A, B))
          self.wait()


CounterclockwiseTransform
*************************
.. autoclass:: manimlib.animation.transform.CounterclockwiseTransform
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/CounterclockwiseTransformExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class CounterclockwiseTransformExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(3)
          B = TextMobject("Text-B").scale(3).shift(UP*2)
  
          self.add(A)
          self.wait()
          self.play(CounterclockwiseTransform(A, B))
          self.wait()


MoveToTarget
*****************
.. autoclass:: manimlib.animation.transform.MoveToTarget
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/MoveToTargetExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class MoveToTargetExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").to_edge(LEFT)
          A.generate_target()  # copyA自身形成A的target属性
          A.target.scale(3).shift(RIGHT*7+UP*2) # 操作A的target
  
          self.add(A)
          self.wait()
          self.play(MoveToTarget(A))
          self.wait()

另外，直接使用 ``self.play(mob.method, ...)`` 相当于给mob创建target，然后根据method
操作target。并且这样能对同一个mobject多次操作（而 ``ApplyMethod`` 不可以，见下）

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/SelfPlayExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class SelfPlayExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").to_edge(LEFT)
  
          self.add(A)
          self.wait()
          self.play(
              A.scale, 3,
              A.shift, RIGHT*7+UP*2,
          )
          self.wait()


ApplyMethod
*****************
.. autoclass:: manimlib.animation.transform.ApplyMethod
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ApplyMethodExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ApplyMethodExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").to_edge(LEFT)
  
          self.add(A)
          self.wait()
          self.play(
              ApplyMethod(A.scale, 3), # 这个不会执行
              ApplyMethod(A.shift, RIGHT*7+UP*2),
          )
          self.wait()

因为 ``ApplyMethod`` 是Transform的子类，所以每次只能对同一个物体执行一次操作（最后一次）


ApplyPointwiseFunction
**********************
.. autoclass:: manimlib.animation.transform.ApplyPointwiseFunction
    :members:


ApplyPointwiseFunctionToCenter
******************************
.. autoclass:: manimlib.animation.transform.ApplyPointwiseFunctionToCenter
    :members:


FadeToColor
*****************
.. autoclass:: manimlib.animation.transform.FadeToColor
    :members:


ScaleInPlace
*****************
.. autoclass:: manimlib.animation.transform.ScaleInPlace
    :members:


ShrinkToCenter
*****************
.. autoclass:: manimlib.animation.transform.ShrinkToCenter
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShrinkToCenterExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShrinkToCenterExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Square(),
                  RegularPolygon(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[ShrinkToCenter(mob) for mob in mobjects]
          )
  
          self.wait()


Restore
*****************
.. autoclass:: manimlib.animation.transform.Restore
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/RestoreExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class RestoreExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").to_edge(LEFT)
          A.save_state()  # 记录下现在状态，restore会回到此时
          A.scale(3).shift(RIGHT*7+UP*2)
  
          self.add(A)
          self.wait()
          self.play(Restore(A))
          self.wait()


ApplyFunction
*****************
.. autoclass:: manimlib.animation.transform.ApplyFunction
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ApplyFunctionExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ApplyFunctionExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").to_edge(LEFT)
          def function(mob):
              return mob.scale(3).shift(RIGHT*7+UP*2)
              # 需要return一个mobject
  
          self.add(A)
          self.wait()
          self.play(ApplyFunction(function, A))
          self.wait()


ApplyMatrix
*****************
.. autoclass:: manimlib.animation.transform.ApplyMatrix
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ApplyMatrixExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ApplyMatrixExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(2)
          mat = np.array([
              [1, 3, 1],
              [0.5, 1, 1],
              [1, 1, 1]
          ])
  
          self.add(A)
          self.wait()
          self.play(ApplyMatrix(mat, A))
          self.wait()


ApplyComplexFunction
*********************
.. autoclass:: manimlib.animation.transform.ApplyComplexFunction
    :members:


CyclicReplace
*****************
.. autoclass:: manimlib.animation.transform.CyclicReplace
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/CyclicReplaceExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class CyclicReplaceExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").scale(3)
          B = TextMobject("Text-B").scale(3)
          VGroup(A, B).arrange(RIGHT)
  
          self.add(A, B)
          self.wait()
          self.play(CyclicReplace(A, B)) # 或Swap(A, B)
          self.wait()


Swap
*****************
.. autoclass:: manimlib.animation.transform.Swap
    :members:


TransformAnimations
*******************
.. autoclass:: manimlib.animation.transform.TransformAnimations
    :members:

这个不常用，甚至Grant都怀疑它存在的意义

