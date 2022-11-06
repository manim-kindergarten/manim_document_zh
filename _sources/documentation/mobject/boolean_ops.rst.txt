BooleanOps
====================

.. admonition:: 声明

    该部分从 ManimCommunity 借鉴得来


Union
***********************
.. autoclass:: manimlib.mobject.boolean_ops.Union
    :members:

.. manim-example:: UnionExample
    :media: https://mkcdn.tonycrane.cc/manimgl_assets/mobject/boolean_ops/UnionExample.png

    class UnionExample(Scene):
        def construct(self):
            cir1 = Circle(radius=3).move_to(LEFT * 1.5)
            cir2 = cir1.copy().move_to(RIGHT * 1.5)
            u = Union(cir1, cir2, color=YELLOW, fill_opacity=0.4)

            self.add(cir1, cir2, u)

Difference
***********************
.. autoclass:: manimlib.mobject.boolean_ops.Difference
    :members:

.. manim-example:: DifferenceExample
    :media: https://mkcdn.tonycrane.cc/manimgl_assets/mobject/boolean_ops/DifferenceExample.png

    class DifferenceExample(Scene):
        def construct(self):
            cir1 = Circle(radius=3).move_to(LEFT * 1.5)
            cir2 = cir1.copy().move_to(RIGHT * 1.5)
            d = Difference(cir1, cir2, color=YELLOW, fill_opacity=0.4)

            self.add(cir1, cir2, d)

Intersection
***********************
.. autoclass:: manimlib.mobject.boolean_ops.Intersection
    :members:

.. manim-example:: IntersectionExample
    :media: https://mkcdn.tonycrane.cc/manimgl_assets/mobject/boolean_ops/IntersectionExample.png

    class IntersectionExample(Scene):
        def construct(self):
            cir1 = Circle(radius=3).move_to(LEFT * 1.5)
            cir2 = cir1.copy().move_to(RIGHT * 1.5)
            i = Intersection(cir1, cir2, color=YELLOW, fill_opacity=0.4)

            self.add(cir1, cir2, i)

Exclusion
***********************
.. autoclass:: manimlib.mobject.boolean_ops.Exclusion
    :members:

.. manim-example:: ExclusionExample
    :media: https://mkcdn.tonycrane.cc/manimgl_assets/mobject/boolean_ops/ExclusionExample.png

    class ExclusionExample(Scene):
        def construct(self):
            cirs = VGroup(*[
                Circle(radius=2).move_to(1.5 * np.array([
                    np.cos(i / 3 * TAU), np.sin(i / 3 * TAU), 0
                ])) for i in range(3)
            ])
            e = Exclusion(*cirs, color=YELLOW, fill_opacity=0.4)
            self.add(cirs, e)
