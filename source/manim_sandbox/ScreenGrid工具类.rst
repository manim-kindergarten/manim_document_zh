ScreenGrid工具类
=================


.. admonition:: 前置知识

   前置知识，CONFIG配置变量参数属性和自定义工具类， 这部分主要是学习的这个比较好的 `视频教程  <https://www.bilibili.com/video/BV1W4411Z7Zt>`_   ，因为真的很细，但是不想每次要用一个个视频去翻，我决定mark下来一些有用的方便平时使用。

这里讲工具类安装使用，这里用视频中的例子来举例，还是无敌的elteoremadebeethoven写的，仓库链接前面提过很多次了。

这个工具类是画网格用的，ScreenGrid，同样可以选择像上文建议的方法放在manimlib/extensions文件夹，不常用的话，完全可以直接放在任意地方，手动在文件头import

.. code:: 

    from manimlib.imports import *
    # 工具类，他写的https://github.com/Elteoremadebeethoven/MyAnimations/blob/master/screen_grid/screen_grid.py
    class Grid(VMobject):
        CONFIG = {
            "height": 6.0,
            "width": 6.0,
        }
    
        def __init__(self, rows, columns, **kwargs):
            digest_config(self, kwargs, locals())
            VMobject.__init__(self, **kwargs)
    
        def generate_points(self):
            x_step = self.width / self.columns
            y_step = self.height / self.rows
    
            for x in np.arange(0, self.width + x_step, x_step):
                self.add(Line(
                    [x - self.width / 2., -self.height / 2., 0],
                    [x - self.width / 2., self.height / 2., 0],
                ))
            for y in np.arange(0, self.height + y_step, y_step):
                self.add(Line(
                    [-self.width / 2., y - self.height / 2., 0],
                    [self.width / 2., y - self.height / 2., 0]
                ))

    class ScreenGrid(VGroup):
        CONFIG = {
            "rows": 8,
            "columns": 14,
            "height": FRAME_Y_RADIUS * 2,
            "width": 14,
            "grid_stroke": 0.5,
            "grid_color": WHITE,
            "axis_color": RED,
            "axis_stroke": 2,
            "show_points": False,
            "point_radius": 0,
            "labels_scale": 0.5,
            "labels_buff": 0,
            "number_decimals": 2
        }
    
        def __init__(self, **kwargs):
            VGroup.__init__(self, **kwargs)
            rows = self.rows
            columns = self.columns
            grilla = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
            grilla.set_stroke(self.grid_color, self.grid_stroke)
    
            vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
            vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
            vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))
    
            ejes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
            ejes_y = Line(DOWN * self.height / 2, UP * self.height / 2)
    
            ejes = VGroup(ejes_x, ejes_y).set_stroke(self.axis_color, self.axis_stroke)
    
            divisiones_x = self.width / columns
            divisiones_y = self.height / rows
    
            direcciones_buff_x = [UP, DOWN]
            direcciones_buff_y = [RIGHT, LEFT]
            dd_buff = [direcciones_buff_x, direcciones_buff_y]
            vectores_inicio_x = [vector_ii, vector_si]
            vectores_inicio_y = [vector_si, vector_sd]
            vectores_inicio = [vectores_inicio_x, vectores_inicio_y]
            divisiones = [divisiones_x, divisiones_y]
            orientaciones = [RIGHT, DOWN]
            puntos = VGroup()
            leyendas = VGroup()
            set_changes = zip([columns, rows], divisiones, orientaciones, [0, 1], vectores_inicio, dd_buff)
            for tipo, division, orientacion, coordenada, vi_c, d_buff in set_changes:
                for i in range(1, tipo):
                    for v_i, direcciones_buff in zip(vi_c, d_buff):
                        ubicacion = v_i + orientacion * division * i
                        punto = Dot(ubicacion, radius=self.point_radius)
                        coord = round(punto.get_center()[coordenada], self.number_decimals)
                        leyenda = TextMobject("%s" % coord).scale(self.labels_scale)
                        leyenda.next_to(punto, direcciones_buff, buff=self.labels_buff)
                        puntos.add(punto)
                        leyendas.add(leyenda)
    
            self.add(grilla, ejes, leyendas)
            if self.show_points:
                self.add(puntos)

要如何使用工具类呢？

.. code:: 

    #使用ScreenGrid(row=ROWS,colums=COLUMS)
    class Positions1(Scene): 
        def construct(self): 
            grid = ScreenGrid()
            object=Dot()
            #object.to_edge(RIGHT)
            object.to_corner(UR)
            self.add(grid,object)
            self.wait()

.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/extensions/Positions1.mp4" type="video/mp4">
   </video>

.. code:: 

    #move_to()
    class Positions2(Scene): 
        def construct(self): 
            grid=ScreenGrid()
            object=Dot()
            ReferenceText=TextMobject("Text")
    
            ReferenceText. move_to(3* LEFT+2* UP)
    
            vector=np. array([-3,-2,0])
            #x,y,z object. move_to(UP+RIGHT)
            
            self. add(grid, object)
            self. wait()
            object. shift(RIGHT)
            self. wait()
            object. shift(RIGHT)
            self. wait()


.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/extensions/Positions2.mp4" type="video/mp4">
   </video>



