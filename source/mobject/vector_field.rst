VectorField
=================

VectorField
******************
.. autoclass:: manimlib.mobject.vector_field.VectorField
    :members:

StreamLines
******************
.. autoclass:: manimlib.mobject.vector_field.StreamLines
    :members:

ShowPassingFlashWithThinningStrokeWidth
****************************************
.. autoclass:: manimlib.mobject.vector_field.ShowPassingFlashWithThinningStrokeWidth
    :members:
    
.. manim-example:: ShowPassingFlashWithThinningStrokeWidthExample
  :media: ../_static/mk/ShowPassingFlashWithThinningStrokeWidthExample.mp4

   class ShowPassingFlashWithThinningStrokeWidthExample(Scene):
       def construct(self):
           sl = StreamLines(
               lambda p: rotate_vector(p / 3, 90 * DEGREES)
           )
           self.add(sl)
           self.wait()
           self.play(ShowPassingFlashWithThinningStrokeWidth(sl))
           self.wait()


AnimatedStreamLines
*******************
.. autoclass:: manimlib.mobject.vector_field.AnimatedStreamLines
    :members: