Creation
========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 


Draw
----

ShowPartial
***************
.. autoclass:: manimlib.animation.creation.ShowPartial
    :members:

ShowCreation
***************
.. autoclass:: manimlib.animation.creation.ShowCreation
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShowCreationExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShowCreationExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[ShowCreation(mob) for mob in mobjects]
          )
  
          self.wait()

Uncreate
*********
.. autoclass:: manimlib.animation.creation.Uncreate
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/UncreateExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class UncreateExample(Scene):
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
              *[Uncreate(mob) for mob in mobjects]
          )
  
          self.wait()

DrawBorderThenFill
**********************
.. autoclass:: manimlib.animation.creation.DrawBorderThenFill
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/DrawBorderThenFillExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class DrawBorderThenFillExample(Scene):
      def construct(self):
          vmobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          vmobjects.scale(1.5)
          vmobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[DrawBorderThenFill(mob) for mob in vmobjects]
          )
  
          self.wait()

Write
*****************
.. autoclass:: manimlib.animation.creation.Write
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/WriteExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class WriteExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[Write(mob) for mob in mobjects]
          )
  
          self.wait()

Fade
----

FadeOut
*****************
.. autoclass:: manimlib.animation.creation.FadeOut
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
.. autoclass:: manimlib.animation.creation.FadeIn
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
.. autoclass:: manimlib.animation.creation.FadeInFrom
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
.. autoclass:: manimlib.animation.creation.FadeInFromDown
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
.. autoclass:: manimlib.animation.creation.FadeOutAndShift
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
.. autoclass:: manimlib.animation.creation.FadeOutAndShiftDown
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

FadeInFromLarge
*********************
.. autoclass:: manimlib.animation.creation.FadeInFromLarge
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
.. autoclass:: manimlib.animation.creation.VFadeIn
    :members:

VFadeOut
*****************
.. autoclass:: manimlib.animation.creation.VFadeOut
    :members:

Grow
----

GrowFromPoint
********************
.. autoclass:: manimlib.animation.creation.GrowFromPoint
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/GrowFromPointExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class GrowFromPointExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          directions=[UP,LEFT,DOWN,RIGHT]
  
          for direction in directions:
              self.play(
                  *[GrowFromPoint(mob,mob.get_center()+direction*3) for mob in mobjects]
              )
  
          self.wait()

GrowFromCenter
*****************
.. autoclass:: manimlib.animation.creation.GrowFromCenter
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/GrowFromCenterExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class GrowFromCenterExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[GrowFromCenter(mob) for mob in mobjects]
          )
  
          self.wait()

GrowFromEdge
*****************
.. autoclass:: manimlib.animation.creation.GrowFromEdge
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/GrowFromEdgeExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class GrowFromEdgeExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          directions=[UP,LEFT,DOWN,RIGHT]
  
          for direction in directions:
              self.play(
                  *[GrowFromEdge(mob,direction) for mob in mobjects]
              )
  
          self.wait()

GrowArrow
***************
.. autoclass:: manimlib.animation.creation.GrowArrow
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/GrowArrowExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class GrowArrowExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Arrow(LEFT,RIGHT),
                  Vector(RIGHT*2)
              )
          mobjects.scale(3)
          mobjects.arrange_submobjects(DOWN,buff=2)
  
          self.play(
              *[GrowArrow(mob)for mob in mobjects]
          )
  
          self.wait()

SpinInFromNothing
***********************
.. autoclass:: manimlib.animation.creation.SpinInFromNothing
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/SpinInFromNothingExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class SpinInFromNothingExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Square(),
                  RegularPolygon(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[SpinInFromNothing(mob) for mob in mobjects]
          )
  
          self.wait()

ShrinkToCenter
*****************
.. autoclass:: manimlib.animation.creation.ShrinkToCenter
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