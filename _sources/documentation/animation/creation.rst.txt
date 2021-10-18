Creation
========

.. admonition:: 声明

   这一页部分翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animations/indication.html>`_ 
   
   后面两个类由鹤翔万里添加


ShowPartial
***************
.. autoclass:: manimlib.animation.creation.ShowPartial
    :members:

ShowCreation
***************
.. autoclass:: manimlib.animation.creation.ShowCreation
    :members:

.. manim-example:: ShowCreationExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/ShowCreationExample.mp4

  class ShowCreationExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[ShowCreation(mob) for mob in mobjects]
          )
  
          self.wait()

Uncreate
*********
.. autoclass:: manimlib.animation.creation.Uncreate
    :members:

.. manim-example:: UncreateExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/UncreateExample.mp4

  class UncreateExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.add(mobjects)
  
          self.wait(0.3)
  
          self.play(
              *[Uncreate(mob) for mob in mobjects]
          )
  
          self.wait()

DrawBorderThenFill
**********************
.. autoclass:: manimlib.animation.creation.DrawBorderThenFill
    
.. manim-example:: DrawBorderThenFillExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/DrawBorderThenFillExample.mp4

  class DrawBorderThenFillExample(Scene):
      def construct(self):
          vmobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          vmobjects.scale(1.5)
          vmobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[DrawBorderThenFill(mob) for mob in vmobjects]
          )
  
          self.wait()

Write
*****************
.. autoclass:: manimlib.animation.creation.Write
    :members:
    
.. manim-example:: WriteExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/manim_3fed/WriteExample.mp4

  class WriteExample(Scene):
      def construct(self):
          mobjects = VGroup(
                  Circle(),
                  Circle(fill_opacity=1),
                  Text("Text").scale(2)
              )
          mobjects.scale(1.5)
          mobjects.arrange_submobjects(RIGHT,buff=2)
  
          self.play(
              *[Write(mob) for mob in mobjects]
          )
  
          self.wait()

ShowIncreasingSubsets
***************************
.. autoclass:: manimlib.animation.creation.ShowIncreasingSubsets
    :members:
    
.. manim-example:: ShowIncreasingSubsetsExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ShowIncreasingSubsetsExample.mp4

  class ShowIncreasingSubsetsExample(Scene):
      def construct(self):
          text = Text("ShowIncreasingSubsets")
          text.set_width(11)
          self.wait()
          self.play(ShowIncreasingSubsets(text[0], run_time=4))
          self.wait()

ShowSubmobjectsOneByOne
***************************
.. autoclass:: manimlib.animation.creation.ShowSubmobjectsOneByOne
    :members:
    
.. manim-example:: ShowSubmobjectsOneByOneExample
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/ShowSubmobjectsOneByOneExample.mp4

  class ShowSubmobjectsOneByOneExample(Scene):
      def construct(self):
          text = Text("ShowSubmobjectsOneByOne")
          text.set_width(11)
          self.wait()
          self.play(ShowSubmobjectsOneByOne(text[0], run_time=4))
          self.wait()


