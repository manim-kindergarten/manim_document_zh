Composition
===========

AnimationGroup
*****************
.. autoclass:: manimlib.animation.composition.AnimationGroup
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/AnimationGroupExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class AnimationGroupExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              TextMobject("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/SuccessionExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class SuccessionExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              TextMobject("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/LaggedStartExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class LaggedStartExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              TextMobject("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/LaggedStartMapExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class LaggedStartMapExample(Scene):
      def construct(self):
          mobjects = VGroup(
              Circle(),
              Circle(fill_opacity=1),
              TextMobject("Text").scale(2)
          )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
          self.wait()
          anims = LaggedStartMap(
              FadeOut, mobjects
          )
          self.play(anims)
          self.wait()
