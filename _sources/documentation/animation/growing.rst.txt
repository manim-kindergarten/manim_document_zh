Growing
========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 


GrowFromPoint
********************
.. autoclass:: manimlib.animation.growing.GrowFromPoint
    :members:
    
.. manim-example:: GrowFromPointExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/GrowFromPointExample.mp4

  class GrowFromPointExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          mobjects.arrange(RIGHT,buff=2)

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
    
.. manim-example:: GrowFromCenterExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/GrowFromCenterExample.mp4

  class GrowFromCenterExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT,buff=2)

          self.play(
              *[GrowFromCenter(mob) for mob in mobjects]
          )

          self.wait()

GrowFromEdge
*****************
.. autoclass:: manimlib.animation.growing.GrowFromEdge
    :members:
    
.. manim-example:: GrowFromEdgeExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/GrowFromEdgeExample.mp4

  class GrowFromEdgeExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          mobjects.arrange(RIGHT,buff=2)

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
    
.. manim-example:: GrowArrowExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/GrowArrowExample.mp4

  class GrowArrowExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Arrow(LEFT,RIGHT),
                  Vector(RIGHT*2).set_color(YELLOW)
              )
          mobjects.scale(3)
          mobjects.arrange(DOWN,buff=2)

          self.play(
              *[GrowArrow(mob)for mob in mobjects]
          )

          self.wait()

SpinInFromNothing
***********************
.. autoclass:: manimlib.animation.growing.SpinInFromNothing
    :members:
    
.. manim-example:: SpinInFromNothingExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/SpinInFromNothingExample.mp4

  class SpinInFromNothingExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Square(),
                  RegularPolygon(fill_opacity=1, color=GREEN),
                  Text("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT,buff=2)

          self.play(
              *[SpinInFromNothing(mob) for mob in mobjects]
          )

          self.wait()

