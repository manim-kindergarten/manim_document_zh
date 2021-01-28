样例学习
==============

在了解了前面的知识后，我们可以运行更多的场景了。
``example_scenes.py`` 中给出了许多示例场景，让我们从简单的开始一个一个研究。

由方变圆SquareToCircle
------------------------

.. manim-example:: SquareToCircle
    :media: ../_static/example_scenes/SquareToCircle.mp4

    from manimlib.imports import *

    class SquareToCircle(Scene):
        def construct(self):
            circle = Circle()
            circle.set_fill(BLUE, opacity=0.5)
            circle.set_stroke(BLUE_E, width=4)
            square = Square()
    
            self.play(ShowCreation(square))
            self.wait()
            self.play(ReplacementTransform(square, circle))
            self.wait()

这个场景就是我们在 :doc:`quickstart` 中编写的。
这里不再解释。

扭曲方形WarpSquare
--------------------

.. manim-example:: WarpSquare
   :media: ../_static/example_scenes/WarpSquare.mp4

   class WarpSquare(Scene):
       def construct(self):
           square = Square()
           self.play(square.apply_complex_function, np.exp)
           self.wait()

这个场景中新出现的用法是 ``self.play(square.apply_complex_function, np.exp)``，
这展示了对正方形施加 :math:`f(z)=e^z` 的复数函数的动画。
其相当于将原正方形变换为施加函数后的图形。

文字示例TextExample
----------------------

.. manim-example:: TextExample
   :media: ../_static/example_scenes/TextExample.mp4

    class TextExample(Scene):
        def construct(self):
            text = Text("Here is a text", font="Consolas", font_size=90)
            difference = Text(
                """
                The most important difference between Text and TexText is that\n
                you can change the font more easily, but can't use the LaTeX grammar
                """,
                font="Arial", font_size=24,
                t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
            )
            VGroup(text, difference).arrange(DOWN, buff=1)
            self.play(Write(text))
            self.play(FadeIn(difference, UP))
            self.wait(3)

            fonts = Text(
                "And you can also set the font according to different words",
                font="Arial",
                t2f={"font": "Consolas", "words": "Consolas"},
                t2c={"font": BLUE, "words": GREEN}
            )
            slant = Text(
                "And the same as slant and weight",
                font="Consolas",
                t2s={"slant": ITALIC},
                t2w={"weight": BOLD},
                t2c={"slant": ORANGE, "weight": RED}
            )
            VGroup(fonts, slant).arrange(DOWN, buff=0.8)
            self.play(FadeOut(text), FadeOut(difference, shift=DOWN))
            self.play(Write(fonts))
            self.wait()
            self.play(Write(slant))
            self.wait()

这个场景中新出现的类是 ``Text``，``VGroup``，``Write``，``FadeIn`` 和 ``FadeOut``：

- ``Text`` 可以创建文字，定义字体等。相关特性在上述例子中已经清晰体现。
- ``VGroup`` 可以将多个 ``VMobject`` 放在一起看做一个整体。例子中调用了 ``arrange()`` 方法来将其中子物体依次向下排列（``DOWN``），且间距为 ``buff``
- ``Write`` 是显示类似书写效果的动画
- ``FadeIn`` 将物体淡入，第二个参数表示淡入的方向
- ``FadeOut`` 将物体淡出，第二个参数表示淡出的方向

匹配变换TexTransformExample
-----------------------------

.. manim-example:: TexTransformExample
   :media: ../_static/example_scenes/TexTransformExample.mp4

    class TexTransformExample(Scene):
        def construct(self):
            kw = {
                "isolate": ["B", "C", "=", "(", ")"]
            }
            lines = VGroup(
                Tex("{{A^2}} + {{B^2}} = {{C^2}}"),
                Tex("{{A^2}} = {{C^2}} - {{B^2}}"),
                Tex("{{A^2}} = (C + B)(C - B)", **kw),
                Tex("A = \\sqrt{(C + B)(C - B)}", **kw)
            )
            lines.arrange(DOWN, buff=LARGE_BUFF)
            for line in lines:
                line.set_color_by_tex_to_color_map({
                    "A": BLUE,
                    "B": TEAL,
                    "C": GREEN,
                })

            play_kw = {"run_time": 2}
            self.add(lines[0])
            self.play(
                TransformMatchingTex(
                    lines[0].copy(), lines[1],
                    path_arc=90 * DEGREES,
                ),
                **play_kw
            )
            self.wait()

            self.play(
                TransformMatchingTex(lines[1].copy(), lines[2]),
                **play_kw
            )
            self.wait()
            self.play(FadeOut(lines[2]))
            self.play(
                TransformMatchingTex(
                    lines[1].copy(), lines[2],
                    key_map={
                        "C^2": "C",
                        "B^2": "B",
                    }
                ),
                **play_kw
            )
            self.wait()

            self.play(
                TransformMatchingTex(
                    lines[2].copy(), lines[3],
                    fade_transform_mismatches=True,
                ),
                **play_kw
            )
            self.wait(3)
            self.play(FadeOut(lines, RIGHT))

            source = TexText("the morse code")
            target = TexText("here come dots")

            self.play(Write(source))
            self.wait()
            kw = {"run_time": 3, "path_arc": PI / 2}
            self.play(TransformMatchingShapes(source, target, **kw))
            self.wait()
            self.play(TransformMatchingShapes(target, source, **kw))
            self.wait()

这个场景中新出现的类是 ``Tex``，``TexText``，``TransformMatchingTex``
和 ``TransformMatchingShapes``：

- ``Tex`` 利用LaTeX来创建数学公式
- ``TexText`` 利用LaTeX来创建文字
- ``TransformMatchingTeX`` 根据 ``Tex`` 中tex的异同来自动对子物体进行 ``Transform``
- ``TransformMatchingShapes`` 直接根据物体点集的异同来自动对子物体进行 ``Transform``

更新程序UpdatersExample
--------------------------

.. manim-example:: UpdatersExample
   :media: ../_static/example_scenes/UpdatersExample.mp4

    class UpdatersExample(Scene):
        def construct(self):
            decimal = DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=3,
                include_sign=True,
            )
            square = Square()
            square.to_edge(UP)

            always(decimal.next_to, square)
            f_always(decimal.set_value, square.get_y)

            self.add(square, decimal)
            self.play(
                square.to_edge, DOWN,
                run_time=3,
            )
            self.play(square.center)
            self.wait()

            now = self.time
            square.add_updater(
                lambda m: m.set_y(math.sin(self.time - now))
            )
            self.wait(10)

这个场景中新出现的类和用法是 ``DecimalNumber``，``.to_edge()``，``.center()``，
``always()``，``f_always()``，``.set_y()`` 和 ``.add_updater()``：

- ``DecimalNumber`` 是一个可变数字，通过将其拆成一个个 ``Tex`` 字符来加快速度
- ``.to_edge()`` 表示将该物体放到画面的边位置
- ``.center()`` 表示将该物体置于画面中间
- ``always(f, x)`` 表示每帧都执行 ``f(x)``
- ``f_always(f, g)`` 类似 ``always``，每帧都执行 ``f(g())``
- ``.set_y()`` 表示设置该物体在画面上的的纵坐标
- ``.add_updater()`` 为该物体设置一个更新函数。例如：``mob1.add_updater(lambda mob: mob.next_to(mob2))`` 表示每帧都执行 ``mob1.next_to(mob2)``

三维示例SurfaceExample
------------------------

.. manim-example:: SurfaceExample
   :media: ../_static/example_scenes/SurfaceExample.mp4

    class SurfaceExample(Scene):
        CONFIG = {
            "camera_class": ThreeDCamera,
        }

        def construct(self):
            surface_text = Text("For 3d scenes, try using surfaces")
            surface_text.fix_in_frame()
            surface_text.to_edge(UP)
            self.add(surface_text)
            self.wait(0.1)

            torus1 = Torus(r1=1, r2=1)
            torus2 = Torus(r1=3, r2=1)
            sphere = Sphere(radius=3, resolution=torus1.resolution)
            
            # 你可以使用最多两个图像对曲面进行纹理处理，
            # 这两个图像将被解释为朝向灯光的一侧和远离灯光的一侧。
            # 这些可以是URL，也可以是指向本地文件的路径
            # day_texture = "EarthTextureMap"
            # night_texture = "NightEarthTextureMap"
            day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
            night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

            surfaces = [
                TexturedSurface(surface, day_texture, night_texture)
                for surface in [sphere, torus1, torus2]
            ]

            for mob in surfaces:
                mob.shift(IN)
                mob.mesh = SurfaceMesh(mob)
                mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

            # 设置视角
            frame = self.camera.frame
            frame.set_euler_angles(
                theta=-30 * DEGREES,
                phi=70 * DEGREES,
            )

            surface = surfaces[0]

            self.play(
                FadeIn(surface),
                ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
            )
            for mob in surfaces:
                mob.add(mob.mesh)
            surface.save_state()
            self.play(Rotate(surface, PI / 2), run_time=2)
            for mob in surfaces[1:]:
                mob.rotate(PI / 2)

            self.play(
                Transform(surface, surfaces[1]),
                run_time=3
            )

            self.play(
                Transform(surface, surfaces[2]),
                # 在过渡期间移动相机帧
                frame.increment_phi, -10 * DEGREES,
                frame.increment_theta, -20 * DEGREES,
                run_time=3
            )
            # 添加自动旋转相机帧
            frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

            # 移动光源
            light_text = Text("You can move around the light source")
            light_text.move_to(surface_text)
            light_text.fix_in_frame()

            self.play(FadeTransform(surface_text, light_text))
            light = self.camera.light_source
            self.add(light)
            light.save_state()
            self.play(light.move_to, 3 * IN, run_time=5)
            self.play(light.shift, 10 * OUT, run_time=5)

            drag_text = Text("Try moving the mouse while pressing d or s")
            drag_text.move_to(light_text)
            drag_text.fix_in_frame()

            self.play(FadeTransform(light_text, drag_text))
            self.wait()

这个场景展示了使用三维面的例子，相关用法已经在注释中简要叙述。

- ``.fix_in_frame()`` 使该物体不随画面视角变化而变化，一直显示在画面上的固定位置

整体示例OpeningManimExample
-----------------------------

.. manim-example:: OpeningManimExample
   :media: ../_static/example_scenes/OpeningManimExample.mp4

    class OpeningManimExample(Scene):
        def construct(self):
            title = TexText("This is some \\LaTeX")
            basel = Tex(
                "\\sum_{n=1}^\\infty "
                "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
            )
            VGroup(title, basel).arrange(DOWN)
            self.play(
                Write(title),
                FadeIn(basel, UP),
            )
            self.wait()

            transform_title = Text("That was a transform")
            transform_title.to_corner(UL)
            self.play(
                Transform(title, transform_title),
                LaggedStartMap(FadeOut, basel, shift=DOWN),
            )
            self.wait()

            fade_comment = Text(
                """
                You probably don't want to overuse
                Transforms, though, a simple fade often
                looks nicer.
                """,
                font_size=36,
                color=GREY_B,
            )
            fade_comment.next_to(
                transform_title, DOWN,
                buff=LARGE_BUFF,
                aligned_edge=LEFT
            )
            self.play(FadeIn(fade_comment, shift=DOWN))
            self.wait(3)

            grid = NumberPlane((-10, 10), (-5, 5))
            grid_title = Text(
                "But manim is for illustrating math, not text",
            )
            grid_title.to_edge(UP)
            grid_title.add_background_rectangle()

            self.add(grid, grid_title)  # Make sure title is on top of grid
            self.play(
                FadeOut(title, shift=LEFT),
                FadeOut(fade_comment, shift=LEFT),
                FadeIn(grid_title),
                ShowCreation(grid, run_time=3, lag_ratio=0.1),
            )
            self.wait()

            matrix = [[1, 1], [0, 1]]
            linear_transform_title = VGroup(
                Text("This is what the matrix"),
                IntegerMatrix(matrix, include_background_rectangle=True),
                Text("looks like")
            )
            linear_transform_title.arrange(RIGHT)
            linear_transform_title.to_edge(UP)

            self.play(
                FadeOut(grid_title),
                FadeIn(linear_transform_title),
            )
            self.play(grid.apply_matrix, matrix, run_time=3)
            self.wait()

            grid_transform_title = Text(
                "And this is a nonlinear transformation"
            )
            grid_transform_title.set_stroke(BLACK, 5, background=True)
            grid_transform_title.to_edge(UP)
            grid.prepare_for_nonlinear_transform(100)
            self.play(
                ApplyPointwiseFunction(
                    lambda p: p + np.array([np.sin(p[1]), np.sin(p[0]), 0]),
                    grid,
                    run_time=5,
                ),
                FadeOut(linear_transform_title),
                FadeIn(grid_transform_title),
            )
            self.wait()

这个场景是一个二维场景的综合运用

在看过这些场景后，你就已经了解了manim的部分用法了。更多的例子可以看 `3b1b的视频代码 <https://github.com/3b1b/videos>`_。
