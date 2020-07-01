Notation公式符号
==================


拉丁符号，数学符号，特定符号笔记。

其实我原来的出发点是整出来一个LaTeX符号源文件模板，用什么特殊符号直接复制完事儿，毕竟pdf格式只能看，搜索和查找和复制都不太方便，都只能靠记住位置用的时候去翻细节。

群文件常见问题.pdf中推荐： 数学符号/公式用 LaTeX 怎么打 请见：

https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan



.. literalinclude:: ../assets/code/manim-tutorial/mathEq.py
   :linenos:


.. raw:: html

    <video width="700" height="394" controls>
        <source src="../_static/manim-tutorial/Equations.mp4" type="video/mp4">
    </video>


上面这1个的案例：from `manim-tutorial <https://github.com/malhotra5/Manim-Tutorial>`_  ，下面这几个我忘记哪儿看的了。





.. code-block:: python
   :linenos:

    # 数学公式
    class BasicEquations(Scene):
        #A short script showing how to use Latex commands
        def construct(self):
            for x in range(-7, 8):
                for y in range(-4, 5):
                    self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
            
            eq1_0=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
            eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
            eq1.shift(2*UP)
            eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
            eq2.shift(2*DOWN)
    
            self.play(Write(eq1_0))
            self.play(Write(eq1))
            self.play(Write(eq2))

.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/BasicEquations.mp4" type="video/mp4">
   </video>

.. code-block:: python
   :linenos:

    class ColoringEquations(Scene):
        #Grouping and coloring parts of equations
        def construct(self):
            line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }",r"\text{on object of mass }")
            line1.set_color_by_tex("force", BLUE)
            line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
            line2.set_color_by_tex_to_color_map({
                "m": YELLOW,
                "{a}": RED
            })
            sentence=VGroup(line1,line2)
            sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
            self.play(Write(sentence))
.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/ColoringEquations.mp4" type="video/mp4">
   </video>


.. code-block:: python
   :linenos:

    class UsingBraces(Scene):
        #Using braces to group text together
        def construct(self):
            eq1A = TextMobject("4x + 3y")
            eq1B = TextMobject("=")
            eq1C = TextMobject("0")
            eq2A = TextMobject("5x -2y")
            eq2B = TextMobject("=")
            eq2C = TextMobject("3")
            eq1B.next_to(eq1A,RIGHT)
            eq1C.next_to(eq1B,RIGHT)
            eq2A.shift(DOWN)
            eq2B.shift(DOWN)
            eq2C.shift(DOWN)
            eq2A.align_to(eq1A,LEFT)
            eq2B.align_to(eq1B,LEFT)
            eq2C.align_to(eq1C,LEFT)
    
            eq_group=VGroup(eq1A,eq2A)
            braces=Brace(eq_group,LEFT)
            eq_text = braces.get_text("A pair of equations")
    
            self.add(eq1A, eq1B, eq1C)
            self.add(eq2A, eq2B, eq2C)
            self.play(GrowFromCenter(braces),Write(eq_text))

.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/UsingBraces.mp4" type="video/mp4">
   </video>


.. code-block:: python
   :linenos:

    #eq1_mob=TexMobject(*eq1_text) is identical to eq1_mob=TexMobject("4","x","+","3","y","=","0").
    class UsingBracesConcise(Scene):
        #A more concise block of code with all columns aligned
        def construct(self):
            eq1_text=["4","x","+","3","y","=","0"]
            eq2_text=["5","x","-","2","y","=","3"]
            eq1_mob=TexMobject(*eq1_text)
            eq2_mob=TexMobject(*eq2_text)
            eq1_mob.set_color_by_tex_to_color_map({
                "x":RED_B,
                "y":GREEN_C
                })
            eq2_mob.set_color_by_tex_to_color_map({
                "x":RED_B,
                "y":GREEN_C
                })
            for i,item in enumerate(eq2_mob):
                item.align_to(eq1_mob[i],LEFT)
            eq1=VGroup(*eq1_mob)
            eq2=VGroup(*eq2_mob)
            eq2.shift(DOWN)
            eq_group=VGroup(eq1,eq2)
            braces=Brace(eq_group,LEFT)
            eq_text = braces.get_text("A pair of equations")
    
            self.play(Write(eq1),Write(eq2))
            self.play(GrowFromCenter(braces),Write(eq_text))


.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/UsingBracesConcise.mp4" type="video/mp4">
   </video>




.. code-block:: python
   :linenos:

    class PlotFunctions(GraphScene):
        CONFIG = {
            "x_min" : -10,
            "x_max" : 10.3,
            "y_min" : -1.5,
            "y_max" : 1.5,
            "graph_origin" : ORIGIN ,
            "function_color" : RED ,
            "axes_color" : GREEN,
            "x_labeled_nums" :range(-10,12,2),
    
        }   
        def construct(self):
            self.setup_axes(animate=True)
            func_graph=self.get_graph(self.func_to_graph,self.function_color)
            func_graph2=self.get_graph(self.func_to_graph2)
            vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
            graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
            graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
            two_pi = TexMobject("x = 2 \\pi")
            label_coord = self.input_to_graph_point(TAU,func_graph)
            two_pi.next_to(label_coord,RIGHT+UP)
    
    
    
            self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
            self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))
    
    
        def func_to_graph(self,x):
            return np.cos(x)
    
        def func_to_graph2(self,x):
            return np.sin(x)



.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/PlotFunctions.mp4" type="video/mp4">
   </video>



.. code-block:: python
   :linenos:

    class ExampleApproximation(GraphScene):
        CONFIG = {
            "function" : lambda x : np.cos(x), 
            "function_color" : BLUE,
            "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
            lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
            "center_point" : 0,
            "approximation_color" : GREEN,
            "x_min" : -10,
            "x_max" : 10,
            "y_min" : -1,
            "y_max" : 1,
            "graph_origin" : ORIGIN ,
            "x_labeled_nums" :range(-10,12,2),
    
        }
        def construct(self):
            self.setup_axes(animate=True)
            func_graph = self.get_graph(
                self.function,
                self.function_color,
            )
            approx_graphs = [
                self.get_graph(
                    f,
                    self.approximation_color
                )
                for f in self.taylor
            ]
    
            term_num = [
                TexMobject("n = " + str(n),aligned_edge=TOP)
                for n in range(0,8)]
            #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]
    
    
            #term = TexMobject("")
            #term.to_edge(BOTTOM,buff=SMALL_BUFF)
            term = VectorizedPoint(3*DOWN)
    
            approx_graph = VectorizedPoint(
                self.input_to_graph_point(self.center_point, func_graph)
            )
    
            self.play(
                ShowCreation(func_graph),
            )
            for n,graph in enumerate(approx_graphs):
                self.play(
                    Transform(approx_graph, graph, run_time = 2),
                    Transform(term,term_num[n])
                )
                self.wait()
.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/SquaExampleApproximationreToCircle.mp4" type="video/mp4">
   </video>





.. code-block:: python
   :linenos:

    class DrawAnAxis(Scene):
        CONFIG = { "plane_kwargs" : { 
            "x_line_frequency" : 2,
            "y_line_frequency" :2
            }
        }
    
        def construct(self):
            my_plane = NumberPlane(**self.plane_kwargs)
            my_plane.add(my_plane.get_axis_labels())
            self.add(my_plane)
            #self.wait()
.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/DrawAnAxis.mp4" type="video/mp4">
   </video>





.. code-block:: python
   :linenos:

    class SimpleField(Scene):
        CONFIG = {
        "plane_kwargs" : {
            "color" : RED
            },
        }
        def construct(self):
            plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
            plane.add(plane.get_axis_labels())  #add x and y label
            self.add(plane)  #Place grid on screen
    
            points = [x*RIGHT+y*UP
                for x in np.arange(-5,5,1)
                for y in np.arange(-5,5,1)
                ]     #List of vectors pointing to each grid point
    
            vec_field = []  #Empty list to use in for loop
            for point in points:
                field = 0.5*RIGHT + 0.5*UP   #Constant field up and to right
                result = Vector(field).shift(point)   #Create vector and shift it to grid point
                vec_field.append(result)   #Append to list
    
            draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup
    
    
            self.play(ShowCreation(draw_field))   #Draw VGroup on screen



.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/SimpleField.mp4" type="video/mp4">
   </video>




.. code-block:: python
   :linenos:

    class FieldWithAxes(Scene):
        CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
        }
        def construct(self):
            plane = NumberPlane(**self.plane_kwargs)
            #plane.main_lines.fade(.9)  #doesn't work in most recent commit
            plane.add(plane.get_axis_labels())
            self.add(plane)
    
            field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
                for x in np.arange(-9,9,1)
                for y in np.arange(-5,5,1)
                ])
    
            self.play(ShowCreation(field))
    
    
        def calc_field(self,point):
            #This calculates the field at a single point.
            x,y = point[:2]
            Rx,Ry = self.point_charge_loc[:2]
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
            efield = (point - self.point_charge_loc)/r**3
            #efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)  #Try one of these two fields
            #efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3  #Try one of these two fields
            return Vector(efield).shift(point)


.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/FieldWithAxes.mp4" type="video/mp4">
   </video>



.. code-block:: python
   :linenos:

    class ExampleThreeD(ThreeDScene):
        CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
        }
        def construct(self):
            plane = NumberPlane(**self.plane_kwargs)
            #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
            plane.add(plane.get_axis_labels())
            self.add(plane)
    
            field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
                for x in np.arange(-9,9,1)
                for y in np.arange(-5,5,1)
                ])
    
            self.set_camera_orientation(phi=PI/3,gamma=PI/5)
            self.play(ShowCreation(field2D))
            self.wait()
            #self.move_camera(gamma=0,run_time=1)   #Doesn't work in most recent commit
            #self.move_camera(phi=3/4*PI, theta=-PI/2)   #Doesn't work in most recent commit
            self.begin_ambient_camera_rotation(rate=0.1)
            self.wait(6)
    
        def calc_field2D(self,point):
            x,y = point[:2]
            Rx,Ry = self.point_charge_loc[:2]
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
            efield = (point - self.point_charge_loc)/r**3
            return Vector(efield).shift(point)
.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/ExampleThreeD.mp4" type="video/mp4">
   </video>





.. code-block:: python
   :linenos:

    class EFieldInThreeD(ThreeDScene):
        CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
        }
        def construct(self):
            plane = NumberPlane(**self.plane_kwargs)
            #plane.main_lines.fade(.9)  #Doesn't work in most recent commit
            plane.add(plane.get_axis_labels())
            self.add(plane)
    
            field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
                for x in np.arange(-9,9,1)
                for y in np.arange(-5,5,1)
                ])
    
            field3D = VGroup(*[self.calc_field3D(x*RIGHT+y*UP+z*OUT)
                for x in np.arange(-9,9,1)
                for y in np.arange(-5,5,1)
                for z in np.arange(-5,5,1)])
    
    
    
            self.play(ShowCreation(field3D))
            self.wait()
            #self.move_camera(0.8*np.pi/2, -0.45*np.pi)   #Doesn't work in most recent commit
            self.begin_ambient_camera_rotation()
            self.wait(6)
    
    
        def calc_field2D(self,point):
            x,y = point[:2]
            Rx,Ry = self.point_charge_loc[:2]
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
            efield = (point - self.point_charge_loc)/r**3
            return Vector(efield).shift(point)
    
        def calc_field3D(self,point):
            x,y,z = point
            Rx,Ry,Rz = self.point_charge_loc
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2+(z-Rz)**2)
            efield = (point - self.point_charge_loc)/r**3
            #efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)
            return Vector(efield).shift(point)
.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/EFieldInThreeD.mp4" type="video/mp4">
   </video>





.. code-block:: python
   :linenos:

    class MovingCharges(Scene):
        CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
        }
        def construct(self):
            plane = NumberPlane(**self.plane_kwargs)
            #plane.main_lines.fade(.9)  #Doesn't work in most recent commit
            plane.add(plane.get_axis_labels())
            self.add(plane)
    
            field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
                for x in np.arange(-9,9,1)
                for y in np.arange(-5,5,1)
                ])
            self.field=field
            source_charge = self.Positron().move_to(self.point_charge_loc)
            self.play(FadeIn(source_charge))
            self.play(ShowCreation(field))
            self.moving_charge()
    
        def calc_field(self,point):
            x,y = point[:2]
            Rx,Ry = self.point_charge_loc[:2]
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
            efield = (point - self.point_charge_loc)/r**3
            return Vector(efield).shift(point)
    
        def moving_charge(self):
            numb_charges=4
            possible_points = [v.get_start() for v in self.field]
            points = random.sample(possible_points, numb_charges)
            particles = VGroup(*[
                self.Positron().move_to(point)
                for point in points
            ])
            for particle in particles:
                particle.velocity = np.array((0,0,0))
    
            self.play(FadeIn(particles))
            self.moving_particles = particles
            self.add_foreground_mobjects(self.moving_particles )
            self.always_continually_update = True
            self.wait(10)
    
        def field_at_point(self,point):
            x,y = point[:2]
            Rx,Ry = self.point_charge_loc[:2]
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
            efield = (point - self.point_charge_loc)/r**3
            return efield
    
        def continual_update(self, *args, **kwargs):
            if hasattr(self, "moving_particles"):
                dt = self.frame_duration
                for p in self.moving_particles:
                    accel = self.field_at_point(p.get_center())
                    p.velocity = p.velocity + accel*dt
                    p.shift(p.velocity*dt)
        class Positron(Circle):
            CONFIG = {
            "radius" : 0.2,
            "stroke_width" : 3,
            "color" : RED,
            "fill_color" : RED,
            "fill_opacity" : 0.5,
            }
            def __init__(self, **kwargs):
                Circle.__init__(self, **kwargs)
                plus = TexMobject("+")
                plus.scale(0.7)
                plus.move_to(self)
                self.add(plus)
    .. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/MovingCharges.mp4" type="video/mp4">
   </video>





.. code-block:: python
   :linenos:

    class FieldOfMovingCharge(Scene):
        CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
            },
        "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
        }
        def construct(self):
            plane = NumberPlane(**self.plane_kwargs)
            #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
            plane.add(plane.get_axis_labels())
            self.add(plane)
    
            field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
                for x in np.arange(-9,9,1)
                for y in np.arange(-5,5,1)
                ])
            self.field=field
            self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
            self.source_charge.velocity = np.array((1,0,0))
            self.play(FadeIn(self.source_charge))
            self.play(ShowCreation(field))
            self.moving_charge()
    
        def create_vect_field(self,source_charge,observation_point):
            return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)
    
        def calc_field(self,source_point,observation_point):
            x,y,z = observation_point
            Rx,Ry,Rz = source_point
            r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
            if r<0.0000001:   #Prevent divide by zero
                efield = np.array((0,0,0))  
            else:
                efield = (observation_point - source_point)/r**3
            return efield
    
    
    
        def moving_charge(self):
            numb_charges=3
            possible_points = [v.get_start() for v in self.field]
            points = random.sample(possible_points, numb_charges)
            particles = VGroup(self.source_charge, *[
                self.Positron().move_to(point)
                for point in points
            ])
            for particle in particles[1:]:
                particle.velocity = np.array((0,0,0))
            self.play(FadeIn(particles[1:]))
            self.moving_particles = particles
            self.add_foreground_mobjects(self.moving_particles )
            self.always_continually_update = True
            self.wait(10)
    
    
        def continual_update(self, *args, **kwargs):
            Scene.continual_update(self, *args, **kwargs)
            if hasattr(self, "moving_particles"):
                dt = self.frame_duration
    
                for v in self.field:
                    field_vect=np.zeros(3)
                    for p in self.moving_particles:
                        field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                    v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())
    
                for p in self.moving_particles:
                    accel = np.zeros(3)
                    p.velocity = p.velocity + accel*dt
                    p.shift(p.velocity*dt)
    
    
        class Positron(Circle):
            CONFIG = {
            "radius" : 0.2,
            "stroke_width" : 3,
            "color" : RED,
            "fill_color" : RED,
            "fill_opacity" : 0.5,
            }
            def __init__(self, **kwargs):
                Circle.__init__(self, **kwargs)
                plus = TexMobject("+")
                plus.scale(0.7)
                plus.move_to(self)
                self.add(plus)






.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/Notation/FieldOfMovingCharge.mp4" type="video/mp4">
   </video>






群文件常见问题.pdf中提到，公式怎么对齐 ：

I. 直接在 TexMobject 中使用 & 对齐 

II. 两个 mobject 对齐，使用 obj2.next_to(obj1, DOWN, aligned_edge=LEFT) 使 obj2 在 obj1 下方，并且左对齐 III. VGroup 内对齐，使用 group.arrange(DOWN, aligned_edge=LEFT) 使 VGroup 中的子元素依 次向下排开，并左对齐
写公式的示例： https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/3_text_like_arrays/scenes.md
























































































