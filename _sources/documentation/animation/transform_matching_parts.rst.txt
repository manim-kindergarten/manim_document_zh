Transform Matching Parts
========================

用例详见 **样例学习** :ref:`匹配变换TexTransformExample` 

TransformMatchingParts
**********************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingParts
    :members:


TransformMatchingShapes
***********************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingShapes
    :members:

.. manim-example:: TransformMatchingShapesExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/transform_matching_parts/TransformMatchingShapesExample.mp4

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
********************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingTex
    :members:

.. manim-example:: TransformMatchingTexExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/transform_matching_parts/TransformMatchingTexExample.mp4

  class TransformMatchingTexExample(Scene):
      def construct(self):
          a = Tex("A", "^2", "=", "B^2+C^2")
          b = Tex("A", "=", "\\sqrt{", "B^2+C^2", "}")
          self.add(a)
          self.wait()
          self.play(TransformMatchingTex(a, b, key_map={"^2": "\\sqrt{"}))
          self.wait()

TransformMatchingStrings
************************
.. autoclass:: manimlib.animation.transform_matching_parts.TransformMatchingStrings
    :members:

.. manim-example:: TransformMatchingStringsExample
  :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/transform_matching_parts/TransformMatchingStringsExample.mp4

  class TransformMatchingStringsExample(Scene):
      def construct(self):
          kw = {
              "isolate": [
                  "\\int_{0}^{\\infty} \\mathrm{e}^{- t}",
                  "\\mathrm{d} t",
                  "c_{0}",
                  "c_{1} t",
                  "c_{2} t^{2}",
                  "c_{n} t^{n}"
              ],
              "tex_to_color_map": {
                  "\\mathrm{e}": MAROON_A,
                  "c_{0}": BLUE,
                  "c_{1}": BLUE,
                  "c_{2}": BLUE,
                  "c_{n}": BLUE
              }
          }
          explicit_formula = MTex(
              "\\int_{0}^{\\infty} \\mathrm{e}^{- t}"
              " \\left( c_{0} + c_{1} t + c_{2} t^{2} + \\cdots + c_{n} t^{n} \\right) \\mathrm{d} t",
              **kw
          )
          expanded_formula = MTex(
              "\\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{0} \\mathrm{d} t"
              " + \\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{1} t \\mathrm{d} t"
              " + \\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{2} t^{2} \\mathrm{d} t"
              " + \\cdots"
              " + \\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{n} t^{n} \\mathrm{d} t",
              **kw
          ).scale(0.8)
          self.add(explicit_formula)
          self.wait()
          self.play(TransformMatchingStrings(explicit_formula, expanded_formula), run_time=2)
          self.wait()
