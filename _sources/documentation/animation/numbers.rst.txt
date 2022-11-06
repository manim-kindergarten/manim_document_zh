Numbers
========

ChangingDecimal
*****************
.. autoclass:: manimlib.animation.numbers.ChangingDecimal
    :members:
    
.. manim-example:: ChangingDecimalExample
  :media: https://mkcdn.tonycrane.cc/manimgl_assets/animations/numbers/ChangingDecimalExample.mp4

  class ChangingDecimalExample(Scene):
      def construct(self):
          number = DecimalNumber(0, text_config={"font": "monospace"}).scale(2)

          def update_func(t):
              return t * 10
          self.add(number)
          self.wait()
          self.play(ChangingDecimal(number, update_func), run_time=3)
          self.wait()

    
ChangeDecimalToValue
**********************
.. autoclass:: manimlib.animation.numbers.ChangeDecimalToValue
    :members:
    
.. manim-example:: ChangeDecimalToValueExample
  :media: https://mkcdn.tonycrane.cc/manimgl_assets/animations/numbers/ChangeDecimalToValueExample.mp4

  class ChangeDecimalToValueExample(Scene):
      def construct(self):
          number = DecimalNumber(0, text_config={"font": "monospace"}).scale(2)
          self.add(number)
          self.wait()
          self.play(ChangeDecimalToValue(number, 20), run_time=3)
          self.wait()


CountInFrom
**********************
.. autoclass:: manimlib.animation.numbers.CountInFrom
    :members:

.. manim-example:: ChangeDecimalToValueExample
  :media: https://mkcdn.tonycrane.cc/manimgl_assets/animations/numbers/CountInFromExample.mp4

  class CountInFromExample(Scene):
      def construct(self):
          number = DecimalNumber(10, text_config={"font": "monospace"}).scale(2)
          self.add(number)
          self.play(CountInFrom(number, 0))
          self.wait()