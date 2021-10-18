Rotation
=========

.. admonition:: 声明

   这一页翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/movement.html>`_ 
   
   由鹤翔万里补充


Rotating
***********************
.. autoclass:: manimlib.animation.rotation.Rotating
    :members:
    
.. manim-example:: RotatingExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/RotatingExample.mp4

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
    
.. manim-example:: RotateExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/RotateExample.mp4

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


请不要尝试直接使用 ``ApplyMethod`` 或 ``self.play(mob.rotate, ...)`` 来旋转，
因为这只是在当前和结果之间进行 ``Transform`` ，并无旋转效果