  class CoorAlias(Scene):
      def construct(self):
          for x in range(-7, 8):
              for y in range(-4, 5):
                  self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))

          aliases = {
              "UP": UP,
              "np.array([0,1,0])": np.array([0, 1, 0]),
              "DOWN": DOWN,
              "np.array([0,-1,0])": np.array([0, -1, 0]),
              "LEFT": LEFT,
              "np.array([-1,0,0])": np.array([-1, 0, 0]),
              "RIGHT": RIGHT,
              "np.array([1,0,0])": np.array([1, 0, 0]),
              "UL": UL,
              "np.array([-1,1,0])": np.array([-1, 1, 0]),
              "DL": DL,
              "np.array([-1,-1,0])": np.array([-1, -1, 0]),
              "UR": UR,
              "np.array([1,1,0])": np.array([1, 1, 0]),
              "DR": DR,
              "np.array([1,-1,0])": np.array([1, -1, 0])}
          circle = Circle(color=RED, radius=0.5)
          self.add(circle)
          self.wait(0.5)

          for text, aliase in aliases.items():
              anno = TexMobject(f"\\texttt{{{text}}}")
              self.play(Write(anno, run_time=0.2))
              self.play(ApplyMethod(circle.shift, aliase))
              self.wait(0.2)
              self.play(FadeOut(anno, run_time=0.2))