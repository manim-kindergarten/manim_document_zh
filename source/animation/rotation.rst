Rotation
=========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/movement.html>`_ 
   
   由鹤翔万里补充


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


**Rotate和Rotating的区别**：

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/RotateAndRotating.mp4" type="video/mp4">
    </video>

``Rotate`` 目前是 ``Transform`` 的子类，即带有 ``path_arc`` 的 ``Transform`` ，所有会有扭曲

``Rotating`` 直接继承自 ``Animation`` ，根据角度插值，比较顺滑，推荐使用

另外，请不要尝试直接使用 ``ApplyMethod`` 或 ``self.play(mob.rotate, ...)`` 来旋转，
因为这只是在当前和结果之间进行 ``Transform`` ，并无旋转效果