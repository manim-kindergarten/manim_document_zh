Update
======

UpdateFromFunc
*****************
.. autoclass:: manimlib.animation.update.UpdateFromFunc
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/UpdateFromFuncExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class UpdateFromFuncExample(Scene):
      def construct(self):
          square = Square().to_edge(UP)
          mobject = TextMobject("Text").scale(2).next_to(square, RIGHT)
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/UpdateFromAlphaFuncExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class UpdateFromAlphaFuncExample(Scene):
      def construct(self):
          square = Square().to_edge(UP)
          mobject = TextMobject("Text").scale(2)
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/MaintainPositionRelativeToExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class MaintainPositionRelativeToExample(Scene):
      def construct(self):
          square = Square().to_edge(UP)
          mobject = TextMobject("Text").scale(2)
          mobject.next_to(square, RIGHT)
  
          self.add(square, mobject)
          self.wait()
          self.play(
              square.to_edge, DOWN,
              MaintainPositionRelativeTo(mobject, square)
          )
          self.wait()

