Composition
===========

AnimationGroup
*****************
.. autoclass:: manimlib.animation.composition.AnimationGroup
    :members:

.. manim-example:: AnimationGroupExample
    :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/AnimationGroupExample.mp4

    class AnimationGroupExample(Scene):
        def construct(self):
            mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
            mobjects.scale(1.5)
            mobjects.arrange(RIGHT,buff=2)
    
            self.wait()
            anims = AnimationGroup(
                *[GrowFromCenter(mob) for mob in mobjects]
            )
            self.play(anims)
            self.wait()


Succession
*****************
.. autoclass:: manimlib.animation.composition.Succession
    :members:

.. manim-example:: SuccessionExample
    :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/SuccessionExample.mp4

    class SuccessionExample(Scene):
        def construct(self):
            mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
            mobjects.scale(1.5)
            mobjects.arrange(RIGHT,buff=2)
    
            self.add(mobjects)
            self.wait()
            anims = Succession(
                *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
            )
            self.play(anims)
            self.wait()

LaggedStart
*****************
.. autoclass:: manimlib.animation.composition.LaggedStart
    :members:

.. manim-example:: LaggedStartExample
    :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/LaggedStartExample.mp4

    class LaggedStartExample(Scene):
        def construct(self):
            mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
            mobjects.scale(1.5)
            mobjects.arrange(RIGHT,buff=2)
    
            self.add(mobjects)
            self.wait()
            anims = LaggedStart(
                *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
            )
            self.play(anims)
            self.wait()


LaggedStartMap
*****************
.. autoclass:: manimlib.animation.composition.LaggedStartMap
    :members:

.. manim-example:: LaggedStartMapExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/LaggedStartMapExample.mp4

  class LaggedStartMapExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              Text("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange(RIGHT,buff=2)
  
          self.add(mobjects)
          self.wait()
          anims = LaggedStartMap(
              FadeOut, mobjects
          )
          self.play(anims)
          self.wait()
