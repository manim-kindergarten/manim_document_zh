Growing
========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 


GrowFromPoint
********************
.. autoclass:: manimlib.animation.growing.GrowFromPoint
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
.. autoclass:: manimlib.animation.growing.GrowFromCenter
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
.. autoclass:: manimlib.animation.growing.GrowFromEdge
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
.. autoclass:: manimlib.animation.growing.GrowArrow
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
.. autoclass:: manimlib.animation.growing.SpinInFromNothing
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

