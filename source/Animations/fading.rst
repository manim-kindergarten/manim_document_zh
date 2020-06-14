Fading
========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 
   
   部分为鹤翔万里补充


FadeOut
*****************
.. autoclass:: manimlib.animation.fading.FadeOut
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeOutExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeOutExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
          self.wait(0.3)
  
          self.play(
              *[FadeOut(mob) for mob in mobjects]
          )
  
          self.wait()

FadeIn
*****************
.. autoclass:: manimlib.animation.fading.FadeIn
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeInExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeInExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[FadeIn(mob) for mob in mobjects]
          )
  
          self.wait()

FadeInFrom
***************************
.. autoclass:: manimlib.animation.fading.FadeInFrom
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeInFromExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeInFromExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          directions=[UP,LEFT,DOWN,RIGHT]
  
          for direction in directions:
              self.play(
                  *[FadeInFrom(mob,direction) for mob in mobjects]
              )
  
          self.wait()

FadeInFromDown
*****************
.. autoclass:: manimlib.animation.fading.FadeInFromDown
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeInFromDownExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeInFromDownExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[FadeInFromDown(mob) for mob in mobjects]
          )
  
          self.wait()

FadeOutAndShift
**********************
.. autoclass:: manimlib.animation.fading.FadeOutAndShift
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeOutAndShiftExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeOutAndShiftExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          directions=[UP,LEFT,DOWN,RIGHT]
  
          self.add(mobjects)
          self.wait(0.3)
  
          for direction in directions:
              self.play(
                  *[FadeOutAndShift(mob,direction) for mob in mobjects]
              )
  
          self.wait()

FadeOutAndShiftDown
****************************
.. autoclass:: manimlib.animation.fading.FadeOutAndShiftDown
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeOutAndShiftDownExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeOutAndShiftDownExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[FadeOutAndShiftDown(mob) for mob in mobjects]
          )
  
          self.wait()

FadeInFromPoint
*********************
.. autoclass:: manimlib.animation.fading.FadeInFromPoint
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/FadeInFromPointExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeInFromPointExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              TextMobject("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.wait()
          self.play(
              *[FadeInFromPoint(mob, UP*3) for mob in mobjects]
          )
          self.wait()


FadeInFromLarge
*********************
.. autoclass:: manimlib.animation.fading.FadeInFromLarge
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FadeInFromLargeExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FadeInFromLargeExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          scale_factors=[0.3,0.8,1,1.3,1.8]
  
          for scale_factor in scale_factors:
              t_scale_factor = TextMobject(f"\\tt scale\\_factor = {scale_factor}")
              t_scale_factor.to_edge(UP)
  
              self.add(t_scale_factor)
  
              self.play(
                  *[FadeInFromLarge(mob,scale_factor) for mob in mobjects]
              )
  
              self.remove(t_scale_factor)
  
          self.wait(0.3)

VFadeIn
*****************
.. autoclass:: manimlib.animation.fading.VFadeIn
    :members:

VFadeOut
*****************
.. autoclass:: manimlib.animation.fading.VFadeOut
    :members:


VFadeInThenOut
*****************
.. autoclass:: manimlib.animation.fading.VFadeInThenOut
    :members:

**Fade和VFade的区别**：

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/FadeAndVFade.mp4" type="video/mp4">
    </video>

``FadeIn`` 的边从细变粗，从暗变亮。 ``VFadeIn`` 的边始终是正常粗细，从暗变亮。

``FadeOut`` 和 ``VFadeOut`` 无区别
