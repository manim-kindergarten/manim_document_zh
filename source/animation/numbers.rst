Numbers
========

ChangingDecimal
*****************
.. autoclass:: manimlib.animation.numbers.ChangingDecimal
    :members:
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ChangingDecimalExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ChangingDecimalExample(Scene):
      def construct(self):
          number = DecimalNumber(0).scale(2)
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
.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/mk/ChangeDecimalToValueExample.mp4" type="video/mp4">
    </video>
.. code-block:: python

  class ChangeDecimalToValueExample(Scene):
      def construct(self):
          number = DecimalNumber(0).scale(2)
          self.add(number)
          self.wait()
          self.play(ChangeDecimalToValue(number, 20), run_time=3)
          self.wait()
