Update
======

UpdateFromFunc
*****************
.. autoclass:: manimlib.animation.update.UpdateFromFunc
    :members:
    
.. manim-example:: UpdateFromFuncExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/UpdateFromFuncExample.mp4

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
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/UpdateFromAlphaFuncExample.mp4

  class UpdateFromAlphaFuncExample(Scene):
      def construct(self):
          square = Square().to_edge(UP)
          mobject = Text("Text").scale(2)
          mobject.next_to(square, RIGHT, buff=0.05)
          def update_func(mob, alpha):
              mob.next_to(square, RIGHT, buff=0.05 + alpha)
  
          self.add(square, mobject)
          self.wait()
          self.play(
              square.to_edge, DOWN,
              UpdateFromAlphaFunc(mobject, update_func)
          )
          self.wait()


MaintainPositionRelativeTo
**************************
.. autoclass:: manimlib.animation.update.MaintainPositionRelativeTo
    :members:
    
.. manim-example:: MaintainPositionRelativeToExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/MaintainPositionRelativeToExample.mp4

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

