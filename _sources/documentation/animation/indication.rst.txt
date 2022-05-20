Indication
==========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 

FocusOn
***********************
.. autoclass:: manimlib.animation.indication.FocusOn
    :members:
    
.. manim-example:: FocusOnExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/FocusOnExample.mp4

  class FocusOnExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Dot(),
              Tex("x")
          )
          mobjects.arrange(RIGHT,buff=2)
  
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
    
.. manim-example:: IndicateExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/IndicateExample.mp4

  class IndicateExample(Scene):
      def construct(self):
          #              0     1    2
          formula = Tex("f(", "x", ")")
          dot = Dot()

          VGroup(formula, dot)\
              .scale(3)\
              .arrange(DOWN, buff=3)

          self.add(formula, dot)

          for mob in [formula[1], dot]:
              self.play(Indicate(mob))

          self.wait(0.3)

Flash
***********************
.. autoclass:: manimlib.animation.indication.Flash
    :members:
    
.. manim-example:: FlashExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/FlashExample.mp4

  class FlashExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Dot(),
              Tex("x")
          ).scale(2)
          mobjects.arrange(RIGHT, buff=2)

          mobject_or_coord = [
              *mobjects,                    # Mobjects: Dot and "x"
              mobjects.get_right()+RIGHT*2  # Coord
          ]

          colors = [GREY, RED, BLUE]

          self.add(mobjects)

          for obj, color in zip(mobject_or_coord, colors):
              self.play(Flash(obj, color=color, flash_radius=0.5))

          self.wait(0.3)

CircleIndicate
***********************
.. autoclass:: manimlib.animation.indication.CircleIndicate
    :members:
    
.. manim-example:: CircleIndicateExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/CircleIndicateExample.mp4

  class CircleIndicateExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Dot(),
              Tex("x")
          ).scale(2)
          mobjects.arrange(RIGHT,buff=2)
  
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
    
.. manim-example:: ShowCreationThenDestructionExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/ShowCreationThenDestructionExample.mp4

  class ShowCreationThenDestructionExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.play(
              *[ShowCreationThenDestruction(mob) for mob in mobjects]
          )

          self.wait()

ShowCreationThenFadeOut
****************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenFadeOut
    :members:
    
.. manim-example:: ShowCreationThenFadeOutExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/ShowCreationThenFadeOutExample.mp4

  class ShowCreationThenFadeOutExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.play(
              *[ShowCreationThenFadeOut(mob) for mob in mobjects]
          )

          self.wait()

AnimationOnSurroundingRectangle
*****************************************
.. autoclass:: manimlib.animation.indication.AnimationOnSurroundingRectangle
    :members:

ShowPassingFlashAround
******************************
.. autoclass:: manimlib.animation.indication.ShowPassingFlashAround
    :members:
    
.. manim-example:: ShowPassingFlashAroundExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/ShowPassingFlashAroundExample.mp4

  class ShowPassingFlashAroundExample(Scene):
      # 目前有显示不全的 bug
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)

          self.play(
              *[ShowPassingFlashAround(mob) for mob in mobjects]
          )

          self.wait()

ShowCreationThenDestructionAround
******************************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenDestructionAround
    :members:
    
.. manim-example:: ShowCreationThenDestructionAroundExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/ShowCreationThenDestructionAroundExample.mp4

  class ShowCreationThenDestructionAroundExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)

          self.play(
              *[ShowCreationThenDestructionAround(mob) for mob in mobjects]
          )

          self.wait()

ShowCreationThenFadeAround
**********************************
.. autoclass:: manimlib.animation.indication.ShowCreationThenFadeAround
    :members:
    
.. manim-example:: ShowCreationThenFadeAroundExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/ShowCreationThenFadeAroundExample.mp4

  class ShowCreationThenFadeAroundExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)

          self.play(
              *[ShowCreationThenFadeAround(mob) for mob in mobjects]
          )

          self.wait()

ApplyWave
***********************
.. autoclass:: manimlib.animation.indication.ApplyWave
    :members:
    
.. manim-example:: ApplyWaveExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/ApplyWaveExample.mp4

  class ApplyWaveExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)

          self.play(
              *[ApplyWave(mob) for mob in mobjects]
          )

          self.wait()

WiggleOutThenIn
***********************
.. autoclass:: manimlib.animation.indication.WiggleOutThenIn
    :members:
    
.. manim-example:: WiggleOutThenInExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/WiggleOutThenInExample.mp4

  class WiggleOutThenInExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)

          self.play(
              *[WiggleOutThenIn(mob) for mob in mobjects]
          )

          self.wait()

TurnInsideOut
***********************
.. autoclass:: manimlib.animation.indication.TurnInsideOut
    :members:
    
.. manim-example:: TurnInsideOutExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/TurnInsideOutExample.mp4

  class TurnInsideOutExample(Scene):
      # 对文字使用会造成非常大的问题
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)

          self.play(
              *[TurnInsideOut(mob) for mob in mobjects]
          )

          self.wait()

FlashyFadeIn
***********************
.. autoclass:: manimlib.animation.indication.FlashyFadeIn
    :members: