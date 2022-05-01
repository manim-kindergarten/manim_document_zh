Specialized
=============

.. admonition:: 声明

    这一页由 widcardw 编辑

Broadcast
**********
.. autoclass:: manimlib.animation.specialized.Broadcast
    :members:

.. manim-example:: BroadcastExample
    :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/animations/BroadcastExample.mp4

    class BroadcastExample(Scene):
        def construct(self):
            dot = Dot()
            self.add(dot)
            anim_kwargs = {
                'big_radius': 5,
                'n_circles': 8,
                'lag_ratio': 0.1,
                'color': YELLOW
            }
            self.play(Broadcast(dot, **anim_kwargs))
            self.wait()