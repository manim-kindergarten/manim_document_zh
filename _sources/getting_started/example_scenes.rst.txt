样例学习
==============

在了解了前面的知识后，我们可以运行更多的场景了。
``example_scenes.py`` 中给出了许多示例场景，让我们从简单的开始一个一个研究。

交互开发 InteractiveDevlopment
-----------------------------------

.. manim-example:: InteractiveDevelopment
    :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/InteractiveDevelopment.mp4

    from manimlib import *

    class InteractiveDevelopment(Scene):
        def construct(self):
            circle = Circle()
            circle.set_fill(BLUE, opacity=0.5)
            circle.set_stroke(BLUE_E, width=4)
            square = Square()

            self.play(ShowCreation(square))
            self.wait()

            # 这会打开一个iPython终端，你可以在其中继续写你想要执行的代码
            # 在这个例子中，square/circle/self都会成为终端中的实例
            self.embed()

            # 尝试拷贝粘贴下面这些行到交互终端中
            self.play(ReplacementTransform(square, circle))
            self.wait()
            self.play(circle.animate.stretch(4, 0))
            self.play(Rotate(circle, 90 * DEGREES))
            self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

            text = Text("""
                In general, using the interactive shell
                is very helpful when developing new scenes
            """)
            self.play(Write(text))

            # 在交互终端中，你可以使用play, add, remove, clear, wait, save_state
            # 和restore来代替self.play, self.add, self.remove……

            # 这时如果要使用鼠标键盘来与窗口互动，需要输入执行touch()
            # 然后你就可以滚动窗口，或者在按住z时滚动来缩放
            # 按住d时移动鼠标来更改相机视角，按r重置相机位置
            # 按q退出和窗口的交互来继续输入其他代码

            # 特别的，你可以自定一个场景来和鼠标和键盘互动
            always(circle.move_to, self.mouse_point)

这个场景就是我们在 :doc:`quickstart` 中编写的。
这里不再解释。

方法动画 AnimatingMethods
----------------------------

.. manim-example:: AnimatingMethods
    :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/AnimatingMethods.mp4

    class AnimatingMethods(Scene):
        def construct(self):
            grid = Tex(r"\pi").get_grid(10, 10, height=4)
            self.add(grid)

            # 你可以通过.animate语法来动画化物件变换方法
            self.play(grid.animate.shift(LEFT))

            # 或者你可以使用旧的语法，把方法和参数同时传给Scene.play
            self.play(grid.shift, LEFT)

            # 这两种方法都会在mobject的初始状态和应用该方法后的状态间进行插值
            # 在本例中，调用grid.shift(LEFT)会将grid向左移动一个单位

            # 这种用法可以用在任何方法上，包括设置颜色
            self.play(grid.animate.set_color(YELLOW))
            self.wait()
            self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
            self.wait()
            self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
            self.wait()

            # 方法Mobject.apply_complex_function允许应用任意的复函数
            # 将把Mobject的所有点的坐标看作复数

            self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
            self.wait()

            # 更一般地说，你可以应用Mobject.apply方法，它接受从R^3到R^3的一个函数
            self.play(
                grid.animate.apply_function(
                    lambda p: [
                        p[0] + 0.5 * math.sin(p[1]),
                        p[1] + 0.5 * math.sin(p[0]),
                        p[2]
                    ]
                ),
                run_time=5,
            )
            self.wait()

这个场景中新出现的用法是``.get_grid()`` 和 ``self.play(mob.animate.method(args))``:

- ``.get_grid()`` 方法会返回一个由该物体复制得到的阵列
- ``self.play(mob.animate.method(args))`` 动画化方法，详细用法在上面代码注释中说明了

文字示例 TextExample
----------------------

.. manim-example:: TextExample
    :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/TextExample.mp4

    class TextExample(Scene):
        def construct(self):
            # 想要正确运行这个场景，你需要确保你的计算机中安装了Consolas字体
            # 关于Text全部用法，请见https://github.com/3b1b/manim/pull/680
            text = Text("Here is a text", font="Consolas", font_size=90)
            difference = Text(
                """
                The most important difference between Text and TexText is that\n
                you can change the font more easily, but can't use the LaTeX grammar
                """,
                font="Arial", font_size=24,
                # t2c是一个由 文本-颜色 键值对组成的字典
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
            fonts.set_width(FRAME_WIDTH - 1)
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


.. _匹配变换TexTransformExample:

匹配变换 TexTransformExample
-----------------------------

.. manim-example:: TexTransformExample
   :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/TexTransformExample.mp4

    class TexTransformExample(Scene):
        def construct(self):
            to_isolate = ["B", "C", "=", "(", ")"]
            lines = VGroup(
                # 将多个参数传递给Tex，这些参数看起来被连接在一起作为一个表达式
                # 但整个mobject的每个submobject为其中的一个字符串
                # 例如，下面的Tex物件将有5个子物件，对应于表达式[A^2，+，B^2，=，C^2]
                Tex("A^2", "+", "B^2", "=", "C^2"),
                # 这里同理
                Tex("A^2", "=", "C^2", "-", "B^2"),
                # 或者，你可以传入关键字参数isolate，其中包含一个字符串列表
                # 这些字符串应该作为它们自己的子物件存在
                # 因此，下面的一行相当于它下面注释掉的一行
                Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
                # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
                Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
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
            # TransformMatchingTex将源和目标中具有匹配tex字符串的部分对应变换
            # 传入path_arc，使每个部分旋转到它们的最终位置，这种效果对于重新排列一个方程是很好的
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
            # …这看起来很好，但由于在lines[2]中没有匹配"C^2"或"B^2"的tex，这些子物件会淡出
            # 而C和B两个子物件会淡入，如果我们希望C^2转到C，而B^2转到B，我们可以用key_map来指定
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

            # 也许我们想把^2上的指数转换成根号。目前，lines[2]将表达式A^2视为一个单元
            # 因此我们可能会需要创建同一line的新版本，该line仅分隔出A
            # 这样，当TransformMatchingTex将所有匹配的部分对应时，唯一的不匹配将是来自new_line2的"^2"
            # 和来自最终行的"\sqrt"之间的不匹配。通过传入transform_missmatches=True，它会将此"^2"转换为"\sqrt"
            new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
            new_line2.replace(lines[2])
            new_line2.match_style(lines[2])

            self.play(
                TransformMatchingTex(
                    new_line2, lines[3],
                    transform_mismatches=True,
                ),
                **play_kw
            )
            self.wait(3)
            self.play(FadeOut(lines, RIGHT))

            # 或者，如果您不想故意分解tex字符串，您可以使用TransformMatchingShapes
            # 它将尝试将源mobject的所有部分与目标的部分对齐，而不考虑每个部分中的子对象层次结构
            # 根据这些部分是否具有相同的形状（尽其所能）来自动匹配变换
            source = Text("the morse code", height=1)
            target = Text("here come dots", height=1)

            self.play(Write(source))
            self.wait()
            kw = {"run_time": 3, "path_arc": PI / 2}
            self.play(TransformMatchingShapes(source, target, **kw))
            self.wait()
            self.play(TransformMatchingShapes(target, source, **kw))
            self.wait()

这个场景中新出现的类是 ``Tex``，``TexText``，``TransformMatchingTex``
和 ``TransformMatchingShapes``：

- ``Tex`` 利用 LaTeX 来创建数学公式
- ``TexText`` 利用 LaTeX 来创建文字
- ``TransformMatchingTeX`` 根据 ``Tex`` 中 tex 的异同来自动对子物体进行 ``Transform``
- ``TransformMatchingShapes`` 直接根据物体点集的异同来自动对子物体进行 ``Transform``

更新程序 UpdatersExample
--------------------------

.. manim-example:: UpdatersExample
   :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/UpdatersExample.mp4

    class UpdatersExample(Scene):
        def construct(self):
            square = Square()
            square.set_fill(BLUE_E, 1)
        
            brace = always_redraw(Brace, square, UP)
        
            text, number = label = VGroup(
                Text("Width = "),
                DecimalNumber(
                    0,
                    show_ellipsis=True,
                    num_decimal_places=2,
                    include_sign=True,
                )
            )
            label.arrange(RIGHT)
        
            always(label.next_to, brace, UP)
            f_always(number.set_value, square.get_width)
        
            self.add(square, brace, label)
        
            self.play(
                square.animate.scale(2),
                rate_func=there_and_back,
                run_time=2,
            )
            self.wait()
            self.play(
                square.animate.set_width(5, stretch=True),
                run_time=3,
            )
            self.wait()
            self.play(
                square.animate.set_width(2),
                run_time=3
            )
            self.wait()
        
            now = self.time
            w0 = square.get_width()
            square.add_updater(
                lambda m: m.set_width(w0 * math.sin(self.time - now) + w0)
            )
            self.wait(4 * PI)

这个场景中新出现的类和用法是 ``DecimalNumber``，``.to_edge()``，``.center()``，
``always()``，``f_always()``，``.set_y()`` 和 ``.add_updater()``：

- ``DecimalNumber`` 是一个可变数字，通过将其拆成一个个 ``Tex`` 字符来加快速度
- ``.to_edge()`` 表示将该物体放到画面的边位置
- ``.center()`` 表示将该物体置于画面中间
- ``always(f, x)`` 表示每帧都执行 ``f(x)``
- ``f_always(f, g)`` 类似 ``always``，每帧都执行 ``f(g())``
- ``.set_y()`` 表示设置该物体在画面上的的纵坐标
- ``.add_updater()`` 为该物体设置一个更新函数。例如：``mob1.add_updater(lambda mob: mob.next_to(mob2))`` 表示每帧都执行 ``mob1.next_to(mob2)``

坐标系统 CoordinateSystemExample
----------------------------------

.. manim-example:: CoordinateSystemExample
    :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/CoordinateSystemExample.mp4

    class CoordinateSystemExample(Scene):
        def construct(self):
            axes = Axes(
                # x轴的范围从-1到10，步长为1
                x_range=(-1, 10),
                # y轴的范围从-2到2，步长为0.5y-axis ranges from -2 to 10 with a step size of 0.5
                y_range=(-2, 2, 0.5),
                # 坐标系将会伸缩来匹配指定的height和width
                height=6,
                width=10,
                # Axes由两个NumberLine组成，你可以通过axis_config来指定它们的样式
                axis_config={
                    "stroke_color": GREY_A,
                    "stroke_width": 2,
                },
                # 或者，你也可以像这样分别指定各个坐标轴的样式
                y_axis_config={
                    "include_tip": False,
                }
            )
            # add_coordinate_labels方法的关键字参数可以传入DecimalNumber来指定它的样式
            axes.add_coordinate_labels(
                font_size=20,
                num_decimal_places=1,
            )
            self.add(axes)

            # Axes从CoordinateSystem类派生而来，意思是可以调用Axes.coords_to_point
            # （缩写为Axes.c2p）将一组坐标与一个点相关联，如下所示：
            dot = Dot(color=RED)
            dot.move_to(axes.c2p(0, 0))
            self.play(FadeIn(dot, scale=0.5))
            self.play(dot.animate.move_to(axes.c2p(3, 2)))
            self.wait()
            self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
            self.wait()

            # 同样，你可以调用Axes.point_to_coords（缩写Axes.p2c）
            # print(axes.p2c(dot.get_center()))

            # 我们可以从轴上画线，以便更好地标记给定点的坐标在这里
            # always_redraw命令意味着在每一个新帧上重新绘制线来保证线始终跟随着点移动
            h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
            v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

            self.play(
                ShowCreation(h_line),
                ShowCreation(v_line),
            )
            self.play(dot.animate.move_to(axes.c2p(3, -2)))
            self.wait()
            self.play(dot.animate.move_to(axes.c2p(1, 1)))
            self.wait()

            # 如果我们把这个点固定在一个特定的坐标上，当我们移动轴时，它也会跟随坐标系移动
            f_always(dot.move_to, lambda: axes.c2p(1, 1))
            self.play(
                axes.animate.scale(0.75).to_corner(UL),
                run_time=2,
            )
            self.wait()
            self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

            # manim还有一些其它的坐标系统：ThreeDAxes，NumberPlane，ComplexPlane


函数图像 GraphExample
---------------------

.. manim-example:: GraphExample
    :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/GraphExample.mp4

    class GraphExample(Scene):
        def construct(self):
            axes = Axes((-3, 10), (-1, 8))
            axes.add_coordinate_labels()

            self.play(Write(axes, lag_ratio=0.01, run_time=1))

            # Axes.get_graph会返回传入方程的图像
            sin_graph = axes.get_graph(
                lambda x: 2 * math.sin(x),
                color=BLUE,
            )
            # 默认情况下，它在所有采样点(x, f(x))之间稍微平滑地插值
            # 但是，如果图形有棱角，可以将use_smoothing设为False
            relu_graph = axes.get_graph(
                lambda x: max(x, 0),
                use_smoothing=False,
                color=YELLOW,
            )
            # 对于不连续的函数，你可以指定间断点来让它不试图填补不连续的位置
            step_graph = axes.get_graph(
                lambda x: 2.0 if x > 3 else 1.0,
                discontinuities=[3],
                color=GREEN,
            )

            # Axes.get_graph_label可以接受字符串或者mobject。如果传入的是字符串
            # 那么将将其当作LaTeX表达式传入Tex中
            # 默认下，label将生成在图像的右侧，并且匹配图像的颜色
            sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
            relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
            step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

            self.play(
                ShowCreation(sin_graph),
                FadeIn(sin_label, RIGHT),
            )
            self.wait(2)
            self.play(
                ReplacementTransform(sin_graph, relu_graph),
                FadeTransform(sin_label, relu_label),
            )
            self.wait()
            self.play(
                ReplacementTransform(relu_graph, step_graph),
                FadeTransform(relu_label, step_label),
            )
            self.wait()

            parabola = axes.get_graph(lambda x: 0.25 * x**2)
            parabola.set_stroke(BLUE)
            self.play(
                FadeOut(step_graph),
                FadeOut(step_label),
                ShowCreation(parabola)
            )
            self.wait()

            # 你可以使用Axes.input_to_graph_point（缩写Axes.i2gp）来找到图像上的一个点
            dot = Dot(color=RED)
            dot.move_to(axes.i2gp(2, parabola))
            self.play(FadeIn(dot, scale=0.5))

            # ValueTracker存储一个数值，可以帮助我们制作可变参数的动画
            # 通常使用updater或者f_always让其它mobject根据其中的数值来更新
            x_tracker = ValueTracker(2)
            f_always(
                dot.move_to,
                lambda: axes.i2gp(x_tracker.get_value(), parabola)
            )

            self.play(x_tracker.animate.set_value(4), run_time=3)
            self.play(x_tracker.animate.set_value(-2), run_time=3)
            self.wait()


三维示例 SurfaceExample
------------------------

.. manim-example:: SurfaceExample
   :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/SurfaceExample.mp4

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

整体示例 OpeningManimExample
-----------------------------

.. manim-example:: OpeningManimExample
   :media: https://fastly.jsdelivr.net/gh/manim-kindergarten/CDN@master/manimgl_assets/example_scenes/OpeningManimExample.mp4

    class OpeningManimExample(Scene):
        def construct(self):
            intro_words = Text("""
                The original motivation for manim was to
                better illustrate mathematical functions
                as transformations.
            """)
            intro_words.to_edge(UP)

            self.play(Write(intro_words))
            self.wait(2)

            # Linear transform
            grid = NumberPlane((-10, 10), (-5, 5))
            matrix = [[1, 1], [0, 1]]
            linear_transform_words = VGroup(
                Text("This is what the matrix"),
                IntegerMatrix(matrix, include_background_rectangle=True),
                Text("looks like")
            )
            linear_transform_words.arrange(RIGHT)
            linear_transform_words.to_edge(UP)
            linear_transform_words.set_stroke(BLACK, 10, background=True)

            self.play(
                ShowCreation(grid),
                FadeTransform(intro_words, linear_transform_words)
            )
            self.wait()
            self.play(grid.animate.apply_matrix(matrix), run_time=3)
            self.wait()

            # Complex map
            c_grid = ComplexPlane()
            moving_c_grid = c_grid.copy()
            moving_c_grid.prepare_for_nonlinear_transform()
            c_grid.set_stroke(BLUE_E, 1)
            c_grid.add_coordinate_labels(font_size=24)
            complex_map_words = TexText("""
                Or thinking of the plane as $\\mathds{C}$,\\\\
                this is the map $z \\rightarrow z^2$
            """)
            complex_map_words.to_corner(UR)
            complex_map_words.set_stroke(BLACK, 5, background=True)

            self.play(
                FadeOut(grid),
                Write(c_grid, run_time=3),
                FadeIn(moving_c_grid),
                FadeTransform(linear_transform_words, complex_map_words),
            )
            self.wait()
            self.play(
                moving_c_grid.animate.apply_complex_function(lambda z: z**2),
                run_time=6,
            )
            self.wait(2)

这个场景是一个二维场景的综合运用

在看过这些场景后，你就已经了解了 manim 的部分用法了。更多的例子可以看 `3b1b的视频代码 <https://github.com/3b1b/videos>`_。
