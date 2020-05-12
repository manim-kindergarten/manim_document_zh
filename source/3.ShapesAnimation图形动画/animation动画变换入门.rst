animation动画变换入门
==========================

.. admonition:: 声明

    这一页是EulerTour写的教程,我只是翻译+学习笔记，github早就有很多教程，但是为了方便查询使用，我才整合这么一份文档。

    **Ps**:chrome加载太多视频的情况下视频播不了，平时卡死人又慢的Edge居然能播放，是我的chrome版本太旧了吗？感觉是安全策略的问题（但是为啥不报错？），因为我Tomcat开个服务器，发现Chrome也可以播放视频。

The simplest of which is ``Scene.add``. The object appears on the first frame
without any animation::

  class NoAnimation(Scene):
      def construct(self):
          square = Square()
          self.add(square))

Animation are used in conjunction with ``scene.Play``

Fade淡出
----------

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeIn.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeIn(Scene):
      def construct(self):
          square = Square()

          anno = TextMobject("Fade In")
          anno.shift(2 * DOWN)
          self.add(anno)
          self.play(FadeIn(square))

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeOut.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeOut(Scene):
      def construct(self):
          square = Square()

          anno = TextMobject("Fade Out")
          anno.shift(2 * DOWN)
          self.add(anno)
          self.add(square)
          self.play(FadeOut(square))



.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeInFrom.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeInFrom(Scene):
      def construct(self):
          square = Square()
          for label, edge in zip(
              ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]
          ):
              anno = TextMobject(f"Fade In from {label}")
              anno.shift(2 * DOWN)
              self.add(anno)

              self.play(FadeInFrom(square, edge))
              self.remove(anno, square)



.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeOutAndShift.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeOutAndShift(Scene):
      def construct(self):
          square = Square()
          for label, edge in zip(
              ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]
          ):
              anno = TextMobject(f"Fade Out and shift {label}")
              anno.shift(2 * DOWN)
              self.add(anno)

              self.play(FadeOutAndShift(square, edge))
              self.remove(anno, square)



.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeInFromLarge.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeInFromLarge(Scene):
      def construct(self):
          square = Square()

          for factor in [0.1, 0.5, 0.8, 1, 2, 5]:
              anno = TextMobject(f"Fade In from large scale\_factor={factor}")
              anno.shift(2 * DOWN)
              self.add(anno)

              self.play(FadeInFromLarge(square, scale_factor=factor))
              self.remove(anno, square)

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeInFromPoint.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeInFromPoint(Scene):
      def construct(self):
          square = Square()
          for i in range(-6, 7, 2):
              anno = TextMobject(f"Fade In from point {i}")
              anno.shift(2 * DOWN)
              self.add(anno)
              self.play(FadeInFromPoint(square, point=i))
              self.remove(anno, square)



Grow生长
----------

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationGrowFromEdge.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationGrowFromEdge(Scene):
      def construct(self):

          for label, edge in zip(
              ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]
          ):
              anno = TextMobject(f"Grow from {label} edge")
              anno.shift(2 * DOWN)
              self.add(anno)
              square = Square()
              self.play(GrowFromEdge(square, edge))
              self.remove(anno, square)



.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationGrowFromCenter.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationGrowFromCenter(Scene):
      def construct(self):
          square = Square()

          anno = TextMobject("Grow from center")
          anno.shift(2 * DOWN)
          self.add(anno)

          self.play(GrowFromCenter(square))




Diagonal Directions对角方向
-------------------------------

You can combine cardinal directions to form diagonal animations

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/Animation/AnimationFadeInFromDiagonal.mp4" type="video/mp4">
    </video>

.. code-block:: python

  class AnimationFadeInFromDiagonal(Scene):
      def construct(self):
          square = Square()
          for diag in [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]:
              self.play(FadeInFrom(square, diag))

.. note::
    You can also use the abbreviated forms like ``UL, UR, DL, DR``.
    See :ref:`ref-directions`.




