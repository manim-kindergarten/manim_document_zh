Update
======

UpdateFromFunc
*****************
.. autoclass:: manimlib.animation.update.UpdateFromFunc
    :members:
    
.. manim-example:: UpdateFromFuncExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/update/UpdateFromFuncExample.mp4

  class UpdateFromFuncExample(Scene):
      def construct(self):
          square = Square().to_edge(UP)
          mobject = Text("Text").scale(2).next_to(square, RIGHT)
          def update_func(mob):
              mob.next_to(square, RIGHT)
  
          self.add(square, mobject)
          self.wait()
          self.play(
              square.to_edge, DOWN,
              UpdateFromFunc(mobject, update_func)
          )
          self.wait()


UpdateFromAlphaFunc
********************
.. autoclass:: manimlib.animation.update.UpdateFromAlphaFunc
    :members:
    
.. manim-example:: UpdateFromAlphaFuncExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/update/UpdateFromAlphaFuncExample.mp4

  class UpdateFromAlphaFuncExample(Scene):
      def construct(self):
          circle = Circle(radius=2).to_edge(UP)
          mobject = Text("Text")
          mobject.move_to(circle.get_start())
          mobject.save_state()

          def update_func(mob, alpha):
              mob.restore()
              mob.move_to(circle.point_from_proportion(alpha))
              mob.rotate(TAU * alpha)

          self.add(circle, mobject)
          self.wait()
          self.play(
              circle.animate.to_edge(DOWN),
              UpdateFromAlphaFunc(mobject, update_func),
              run_time=3
          )
          self.wait()


MaintainPositionRelativeTo
**************************
.. autoclass:: manimlib.animation.update.MaintainPositionRelativeTo
    :members:
    
.. manim-example:: MaintainPositionRelativeToExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/update/MaintainPositionRelativeToExample.mp4

  class MaintainPositionRelativeToExample(Scene):
      def construct(self):
          square = Square().to_edge(UP)
          mobject = Text("Text").scale(2)
          mobject.next_to(square, RIGHT)
  
          self.add(square, mobject)
          self.wait()
          self.play(
              square.to_edge, DOWN,
              MaintainPositionRelativeTo(mobject, square)
          )
          self.wait()

