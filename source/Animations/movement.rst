Movement and Rotations
======================

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/movement.html>`_ 



Homotopy
***********************
.. autoclass:: manimlib.animation.movement.Homotopy
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/HomotopyExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class HomotopyExample(Scene):
      def construct(self):
          def plane_wave_homotopy(x, y, z, t):
              norm = get_norm([x, y])
              tau = interpolate(5, -5, t) + norm/FRAME_X_RADIUS
              alpha = sigmoid(tau)
              return [x, y + 0.5*np.sin(2*np.pi*alpha)-t*SMALL_BUFF/2, z]
  
          mobjects=VGroup(
              TextMobject("Text").scale(3),
              Square(),
          ).arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
          self.play(
              *[Homotopy(
                  plane_wave_homotopy, 
                  mob
              ) for mob in mobjects]
          )
          self.wait(0.3)

ComplexHomotopy
***********************
.. autoclass:: manimlib.animation.movement.ComplexHomotopy
    :members:

PhaseFlow
***********************
.. autoclass:: manimlib.animation.movement.PhaseFlow
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/PhaseFlowExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class PhaseFlowExample(Scene):
      def construct(self):
          def func(t):
              return t*0.5*RIGHT
  
          mobjects=VGroup(
              TextMobject("Text").scale(3),
              Square(),
          ).arrange_submobjects(RIGHT,buff=2)
  
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/MoveAlongPathExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

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

Rotating
***********************
.. autoclass:: manimlib.animation.rotation.Rotating
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/RotatingExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class RotatingExample(Scene):
      def construct(self):
          square=Square().scale(2)
          self.add(square)
  
          self.play(
              Rotating(
                  square,
                  radians=PI/4,
                  run_time=2
              )
          )
          self.wait(0.3)
          self.play(
              Rotating(
                  square,
                  radians=PI,
                  run_time=2,
                  axis=RIGHT
              )
          )
          self.wait(0.3)

Rotate
***********************
.. autoclass:: manimlib.animation.rotation.Rotate
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/RotateExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class RotateExample(Scene):
      def construct(self):
          square=Square().scale(2)
          self.add(square)
  
          self.play(
              Rotate(
                  square,
                  PI/4,
                  run_time=2
              )
          )
          self.wait(0.3)
          self.play(
              Rotate(
                  square,
                  PI,
                  run_time=2,
                  axis=RIGHT
              )
          )
          self.wait(0.3)

