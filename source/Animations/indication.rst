Indication
==========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 

FocusOn
***********************
.. autoclass:: manimlib.animation.indication.FocusOn
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FocusOnExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FocusOnExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Dot(),
              TexMobject("x")
          )
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          mobject_or_coord = [
              *mobjects,                    # Mobjects: Dot and "x"
              mobjects.get_right()+RIGHT*2  # Coord
          ]
  
          colors=[GRAY,RED,BLUE]
  
          self.add(mobjects)
  
          for obj,color in zip(mobject_or_coord,colors):
              self.play(FocusOn(obj,color=color))
  
          self.wait(0.3)

Indicate
***********************
.. autoclass:: manimlib.animation.indication.Indicate
    :members:

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/IndicateExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class IndicateExample(Scene):
      def construct(self):
          #                     0    1   2
          formula = TexMobject("f(","x",")")
          dot = Dot()
  
          VGroup(formula,dot)\
                             .scale(3)\
                             .arrange_submobjects(DOWN,buff=3)
  
          self.add(formula,dot)
  
          for mob in [formula[1],dot]:
              self.play(Indicate(mob))
  
          self.wait(0.3)

Flash
***********************
.. autoclass:: manimlib.animation.indication.Flash
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/FlashExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class FlashExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Dot(),
              TexMobject("x")
          ).scale(2)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          mobject_or_coord = [
              *mobjects,                    # Mobjects: Dot and "x"
              mobjects.get_right()+RIGHT*2  # Coord
          ]
  
          colors=[GRAY,RED,BLUE]
  
          self.add(mobjects)
  
          for obj,color in zip(mobject_or_coord,colors):
              self.play(Flash(obj,color=color,flash_radius=0.5))
  
          self.wait(0.3)

CircleIndicate
***********************
.. autoclass:: manimlib.animation.indication.CircleIndicate
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/CircleIndicateExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class CircleIndicateExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Dot(),
              TexMobject("x")
          ).scale(2)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
          self.wait(0.2)
  
          for obj in mobjects:
              self.play(CircleIndicate(obj))

ShowPassingFlash
***********************
.. autoclass:: manimlib.animation.indication.ShowPassingFlash
    :members:

ShowCreationThenDestruction
********************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenDestruction
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShowCreationThenDestructionExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShowCreationThenDestructionExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[ShowCreationThenDestruction(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

ShowCreationThenFadeOut
****************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenFadeOut
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShowCreationThenFadeOutExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShowCreationThenFadeOutExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[ShowCreationThenFadeOut(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

AnimationOnSurroundingRectangle
*****************************************
.. autoclass:: manimlib.animation.indication.AnimationOnSurroundingRectangle
    :members:

ShowPassingFlashAround
******************************
.. autoclass:: manimlib.animation.indication.ShowPassingFlashAround
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShowPassingFlashAroundExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShowPassingFlashAroundExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.play(
              *[ShowPassingFlashAround(mob) for mob in mobjects]
          )
  
          self.wait()

ShowCreationThenDestructionAround
******************************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenDestructionAround
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShowCreationThenDestructionAroundExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShowCreationThenDestructionAroundExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.play(
              *[ShowCreationThenDestructionAround(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

ShowCreationThenFadeAround
**********************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenFadeAround
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ShowCreationThenFadeAroundExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ShowCreationThenFadeAroundExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.play(
              *[ShowCreationThenFadeAround(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

ApplyWave
***********************
.. autoclass:: manimlib.animation.indication.ApplyWave
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/ApplyWaveExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ApplyWaveExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.play(
              *[ApplyWave(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

WiggleOutThenIn
***********************
.. autoclass:: manimlib.animation.indication.WiggleOutThenIn
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/WiggleOutThenInExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class WiggleOutThenInExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.play(
              *[WiggleOutThenIn(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

TurnInsideOut
***********************
.. autoclass:: manimlib.animation.indication.TurnInsideOut
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/TurnInsideOutExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class TurnInsideOutExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  TextMobject("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.play(
              *[TurnInsideOut(mob) for mob in mobjects]
          )
  
          self.wait()
  
          self.wait(0.3)

