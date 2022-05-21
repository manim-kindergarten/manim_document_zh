Fading
========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 
   
   部分为鹤翔万里补充

.. admonition:: 注意

   旧版的各种 ``FadeInFrom`` 和 ``FadeOutFrom`` 等方法已经全部整合在 ``FadeIn`` 和 ``FadeOut`` 中，以参数的形式给出，使得类的使用更加简洁

FadeOut
*****************
.. autoclass:: manimlib.animation.fading.FadeOut
    :members:
    
.. manim-example:: FadeOutExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeOutExample.mp4

  class FadeOutExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)
          self.wait(0.3)

          self.play(
              *[FadeOut(mob) for mob in mobjects]
          )

          self.wait()

FadeIn
*****************
.. autoclass:: manimlib.animation.fading.FadeIn
    :members:
    
.. manim-example:: FadeInExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeInExample.mp4

  class FadeInExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.play(
              *[FadeIn(mob) for mob in mobjects]
          )

          self.wait()
    
.. manim-example:: FadeInFromExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeInFromExample.mp4

  class FadeInFromExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          directions = [UP, LEFT, DOWN, RIGHT]

          for direction in directions:
              self.play(
                  *[FadeIn(mob, shift=direction) for mob in mobjects]
              )

          self.wait()

.. manim-example:: FadeOutAndShiftExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeOutAndShiftExample.mp4

  class FadeOutAndShiftExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          directions = [UP, LEFT, DOWN, RIGHT]

          self.add(mobjects)
          self.wait(0.3)

          for direction in directions:
              self.play(
                  *[FadeOut(mob, shift=direction) for mob in mobjects]
              )

          self.wait()

.. manim-example:: FadeInFromLargeExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeInFromLargeExample.mp4

  class FadeInFromLargeExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          scale_factors = [0.3, 0.8, 1, 1.3, 1.8]

          for scale_factor in scale_factors:
              t_scale_factor = Text(
                  f"scale_factor = {scale_factor}", font="monospace")
              t_scale_factor.to_edge(UP)

              self.add(t_scale_factor)

              self.play(
                  *[FadeIn(mob, scale=scale_factor) for mob in mobjects]
              )

              self.remove(t_scale_factor)

          self.wait(0.3)

FadeInFromPoint
*********************
.. autoclass:: manimlib.animation.fading.FadeInFromPoint
    :members:
    
.. manim-example:: FadeInFromPointExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeInFromPointExample.mp4

  class FadeInFromPointExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.wait()
          self.play(
              *[FadeInFromPoint(mob, UP*3) for mob in mobjects]
          )
          self.wait()

FadeOutToPoint
*********************
.. autoclass:: manimlib.animation.fading.FadeOutToPoint
    :members:

.. manim-example:: FadeOutToPointExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeOutToPointExample.mp4

  class FadeOutToPointExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT, buff=2)

          self.add(mobjects)
          self.wait()
          self.play(
              *[FadeOutToPoint(mob, DOWN*3) for mob in mobjects]
          )
          self.wait()

FadeTransform
*********************
.. autoclass:: manimlib.animation.fading.FadeTransform
    :members:

.. manim-example:: FadeTransformExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeTransformExample.mp4

  class FadeTransformExample(Scene):
      def construct(self):
          m_a = Rectangle(width=6, height=2, color=BLUE, fill_opacity=1)
          m_b = Text("Rectangle").scale(3)
          self.add(m_a)
          self.wait()
          self.play(FadeTransform(m_a, m_b))
          self.wait()


FadeTransformPieces
*********************
.. autoclass:: manimlib.animation.fading.FadeTransformPieces
    :members:

.. manim-example:: FadeTransformPiecesExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/fade/FadeTransformPiecesExample.mp4


  class FadeTransformPiecesExample(Scene):
      def construct(self):
          m_a = VGroup(*[
              Circle(radius=0.4)
              .move_to((np.random.random(3)-0.5) * 3)
              for i in range(6)
          ])
          m_b = Text("Circle").scale(3)
          self.add(m_a)
          self.wait()
          self.play(FadeTransformPieces(m_a, m_b))
          self.wait()

VFadeIn
*****************
.. autoclass:: manimlib.animation.fading.VFadeIn
    :members:

VFadeOut
*****************
.. autoclass:: manimlib.animation.fading.VFadeOut
    :members:


VFadeInThenOut
*****************
.. autoclass:: manimlib.animation.fading.VFadeInThenOut
    :members:

**Fade和VFade的区别**：

.. raw:: html

    <video class="manim-video" controls loop autoplay src="https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/FadeAndVFade.mp4"></video>

``FadeIn`` 的边从细变粗，从暗变亮。 ``VFadeIn`` 的边始终是正常粗细，从暗变亮。

``FadeOut`` 和 ``VFadeOut`` 无区别
