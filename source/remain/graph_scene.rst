Graph Scene
-------------------
.. admonition:: 声明

   这一页是elteoremadebeethoven写的 `manim_3feb_docs <https://github.com/Elteoremadebeethoven/manim_3feb_docs.github.io/tree/master/source>`_  `online <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/index.html>`_ 我翻译+做笔记，把资料整合编辑成方便的文档格式，以方便查阅使用Manim。
   为了更好地体验，建议看这里 `manim_3feb_docs-mobjects-geometric <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/mobjects/geometric.html>`_  ，Sphinx插件也没问题，不知为何，我的方法和属性没有自动生成^_^# 。

详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>`  。

.. code-block::bash

    .. autoclass:: manimlib.scene.graph_scene.GraphScene
        :members:


报错：\manim\manimlib\scene\graph_scene.py:docstring of manimlib.scene.graph_scene.GraphScene.get_secant_slope_group:7: WARNING: Definition list ends without a blank line; unexpected unindent.





Riemann rectangles
******************

.. raw:: html

    <img src="../_static/manim_3fed/RiemannRectangles.png" alt="Riemann rectangles" style="width:560px;height:315px;">

.. code-block:: python

  class RiemannRectangles(GraphScene):
      CONFIG = {
          "y_max": 8,
          "y_axis_height": 5,
      }
      def construct(self):
          self.setup_axes()
          def func(x):
              return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

          graph=self.get_graph(func,x_min=0.3,x_max=9.2)
          riemann_rectangles=self.get_riemann_rectangles(
                                      graph,
                                      x_min=2,
                                      x_max=8,
                                      dx=0.5
                                      )
          self.add(graph,riemann_rectangles)

Riemann rectangles animation
****************************

.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/manim_3fed/RiemannRectanglesAnimation.mp4" type="video/mp4">
    </video>


.. code-block:: python

  class RiemannRectanglesAnimation(GraphScene):
      CONFIG = {
          "y_max": 8,
          "y_axis_height": 5,
          "init_dx":0.5,
      }
      def construct(self):
          self.setup_axes()
          def func(x):
              return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

          graph=self.get_graph(func,x_min=0.3,x_max=9.2)
          kwargs = {
              "x_min" : 2,
              "x_max" : 8,
              "fill_opacity" : 0.75,
              "stroke_width" : 0.25,
          }
          flat_rectangles = self.get_riemann_rectangles(
                                  self.get_graph(lambda x : 0),
                                  dx=self.init_dx,
                                  start_color=invert_color(PURPLE),
                                  end_color=invert_color(ORANGE),
                                  **kwargs
          )
          riemann_rectangles_list = self.get_riemann_rectangles_list(
                                  graph, 
                                  6,
                                  max_dx=self.init_dx,
                                  power_base=2,
                                  start_color=PURPLE,
                                  end_color=ORANGE,
                                   **kwargs
          )
          self.add(graph)
          # Show Riemann rectangles
          self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list[0]))
          self.wait()
          for r in range(1,len(riemann_rectangles_list)):
              self.transform_between_riemann_rects(
                      riemann_rectangles_list[r-1],
                      riemann_rectangles_list[r],
                      replace_mobject_with_target_in_scene = True,
                  )
          self.wait()
