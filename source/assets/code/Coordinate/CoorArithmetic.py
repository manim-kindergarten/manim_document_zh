  class CoorArithmetic(Scene):
      def construct(self):
          for x in range(-7, 8):
              for y in range(-4, 5):
                  self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))

          circle = Circle(color=RED, radius=0.5)
          self.add(circle)
          self.wait(0.5)

          aliases = {
              "LEFT * 3": LEFT * 3,
              "UP + RIGHT / 2": UP + RIGHT / 2,
              "DOWN + LEFT * 2": DOWN + LEFT * 2,
              "RIGHT * 3.75 * DOWN": RIGHT * 3.75 * DOWN,
              # certain arithmetic won't work as you expected
              # In [4]: RIGHT * 3.75 * DOWN
              # Out[4]: array([ 0., -0.,  0.])
              "RIGHT * 3.75 + DOWN": RIGHT * 3.75 + DOWN}

          for text, aliase in aliases.items():
              anno = TexMobject(f"\\texttt{{{text}}}")
              self.play(Write(anno, run_time=0.2))
              self.play(ApplyMethod(circle.shift, aliase))
              self.wait(0.2)
              self.play(FadeOut(anno, run_time=0.2))