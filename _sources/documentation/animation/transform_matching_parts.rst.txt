Transform Matching Parts
===========================

用例详见 **样例学习** :ref:`匹配变换TexTransformExample` 

TransformMatchingParts
***************************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingParts
    :members:


TransformMatchingShapes
***************************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingShapes
    :members:

.. manim-example:: TransformMatchingShapesExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/TransformMatchingShapesExample.mp4

  class TransformMatchingShapesExample(Scene):
      def construct(self):
          a = Text("the morse code").scale(2)
          b = Text("here some dots").scale(2)
          self.add(a)
          self.wait()
          self.play(TransformMatchingShapes(a, b, path_arc=PI/2))
          self.wait()
          self.play(TransformMatchingShapes(b, a, path_arc=PI/2))
          self.wait()

TransformMatchingTex
***************************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingTex
    :members:

.. manim-example:: TransformMatchingTexExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/TransformMatchingTexExample.mp4

  class TransformMatchingTexExample(Scene):
      def construct(self):
          a = Tex("A", "^2", "=", "B^2+C^2")
          b = Tex("A", "=", "\\sqrt{", "B^2+C^2", "}")
          self.add(a)
          self.wait()
          self.play(TransformMatchingTex(a, b, key_map={"^2": "\\sqrt{"}))
          self.wait()

