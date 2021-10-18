Transform
==========

Transform
*****************
.. autoclass:: manimlib.animation.transform.Transform
    :members:
    
.. manim-example:: TransformExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/TransformExample.mp4

  class TransformExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(3)
          B = Text("Text-B").scale(3)
          C = Text("C-Text").scale(3)
  
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
    
.. manim-example:: ReplacementTransformExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ReplacementTransformExample.mp4

  class ReplacementTransformExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(3)
          B = Text("Text-B").scale(3)
          C = Text("C-Text").scale(3)
  
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
    
.. manim-example:: TransformFromCopyExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/TransformFromCopyExample.mp4

  class TransformFromCopyExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(3)
          B = Text("Text-B").scale(3).shift(UP*2)
  
          self.add(A)
          self.wait()
          self.play(TransformFromCopy(A, B))
          self.wait()


ClockwiseTransform
******************
.. autoclass:: manimlib.animation.transform.ClockwiseTransform
    :members:
    
.. manim-example:: ClockwiseTransformExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ClockwiseTransformExample.mp4

  class ClockwiseTransformExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(3)
          B = Text("Text-B").scale(3).shift(UP*2)
  
          self.add(A)
          self.wait()
          self.play(ClockwiseTransform(A, B))
          self.wait()


CounterclockwiseTransform
*************************
.. autoclass:: manimlib.animation.transform.CounterclockwiseTransform
    :members:
    
.. manim-example:: CounterclockwiseTransformExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/CounterclockwiseTransformExample.mp4

  class CounterclockwiseTransformExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(3)
          B = Text("Text-B").scale(3).shift(UP*2)
  
          self.add(A)
          self.wait()
          self.play(CounterclockwiseTransform(A, B))
          self.wait()


MoveToTarget
*****************
.. autoclass:: manimlib.animation.transform.MoveToTarget
    :members:
    
.. manim-example:: MoveToTargetExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/MoveToTargetExample.mp4

  class MoveToTargetExample(Scene):
      def construct(self):
          A = Text("Text-A").to_edge(LEFT)
          A.generate_target()  # copyA自身形成A的target属性
          A.target.scale(3).shift(RIGHT*7+UP*2) # 操作A的target
  
          self.add(A)
          self.wait()
          self.play(MoveToTarget(A))
          self.wait()

另外，直接使用 ``self.play(mob.method, ...)`` 相当于给mob创建target，然后根据method
操作target。并且这样能对同一个mobject多次操作。当然，也可以用 ``self.play(mob.animate.shift(UP).scale(2))`` 进行链式操作（而 ``ApplyMethod`` 不可以，见下）

.. manim-example:: SelfPlayExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/SelfPlayExample.mp4

  class SelfPlayExample(Scene):
      def construct(self):
          A = TextMobject("Text-A").to_edge(LEFT)
  
          self.add(A)
          self.wait()
          self.play(
              A.scale, 3,
              A.shift, RIGHT*7+UP*2,
          )
          # self.play(
                A.animate.scale(3).shift(RIGHT*7+UP*2)
          )
          self.wait()


ApplyMethod
*****************
.. autoclass:: manimlib.animation.transform.ApplyMethod
    :members:
    
.. manim-example:: ApplyMethodExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ApplyMethodExample.mp4

  class ApplyMethodExample(Scene):
      def construct(self):
          A = Text("Text-A").to_edge(LEFT)
  
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
    
.. manim-example:: ShrinkToCenterExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/ShrinkToCenterExample.mp4

  class ShrinkToCenterExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Square(),
                  RegularPolygon(fill_opacity=1),
                  Text("Text").scale(2)
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
    
.. manim-example:: RestoreExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/RestoreExample.mp4

  class RestoreExample(Scene):
      def construct(self):
          A = Text("Text-A").to_edge(LEFT)
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
    
.. manim-example:: ApplyFunctionExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ApplyFunctionExample.mp4

  class ApplyFunctionExample(Scene):
      def construct(self):
          A = Text("Text-A").to_edge(LEFT)
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
    
.. manim-example:: ApplyMatrixExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ApplyMatrixExample.mp4

  class ApplyMatrixExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(2)
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
    
.. manim-example:: CyclicReplaceExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/CyclicReplaceExample.mp4

  class CyclicReplaceExample(Scene):
      def construct(self):
          A = Text("Text-A").scale(3)
          B = Text("Text-B").scale(3)
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

