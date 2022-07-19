Movement
======================

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/movement.html>`_ 



Homotopy
***********************
.. autoclass:: manimlib.animation.movement.Homotopy
    :members:
    
.. manim-example:: HomotopyExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/movement/HomotopyExample.mp4

  class HomotopyExample(Scene):
      def construct(self):
          def homotopy_fun(x, y, z, t):
              return [x * t, y * t, z]

          mob = Square()
          self.add(mob)
          self.play(Homotopy(homotopy_fun, mob))
          self.wait()


ComplexHomotopy
***********************
.. autoclass:: manimlib.animation.movement.ComplexHomotopy
    :members:

.. manim-example:: ComplexHomotopyExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/movement/ComplexHomotopyExample.mp4

  class ComplexHomotopyExample(Scene):
      def construct(self):
          def complex_func(z: complex, t: float) -> complex:
              return interpolate(z, z**3, t)

          mobjects = VGroup(
              Text("Text"),
              Square(side_length=1),
          ).arrange(RIGHT, buff=2)

          self.add(mobjects)
          self.play(
              *[ComplexHomotopy(
                  complex_func,
                  mob
              ) for mob in mobjects]
          )
          self.wait(0.3)

PhaseFlow
***********************
.. autoclass:: manimlib.animation.movement.PhaseFlow
    :members:
    
.. manim-example:: PhaseFlowExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/movement/PhaseFlowExample.mp4

  class PhaseFlowExample(Scene):
      def construct(self):
          def func(t):
              return t*0.5*RIGHT

          mobjects=VGroup(
              Text("Text").scale(3),
              Square(),
          ).arrange(RIGHT,buff=2)

          self.play(
              *[PhaseFlow(
                  func, mob,
                  run_time = 2,
              )for mob in mobjects]
          )

          self.wait()

MoveAlongPath
***********************
.. autoclass:: manimlib.animation.movement.MoveAlongPath
    :members:
    
.. manim-example:: MoveAlongPathExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/movement/MoveAlongPathExample.mp4

  class MoveAlongPathExample(Scene):
      def construct(self):
          line=Line(ORIGIN,RIGHT*FRAME_WIDTH,buff=1)
          line.move_to(ORIGIN)
          dot=Dot()
          dot.move_to(line.get_start())

          self.add(line,dot)
          self.play(
              MoveAlongPath(dot,line)
          )
          self.wait(0.3)

