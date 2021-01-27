CONFIG字典用法
=================

CONFIG字典是manim的一个特性，方便了父子类之间参数的继承和修改

| 对于CONFIG字典的处理，在\ ``manimlib/utils/config_ops.py``\ 中
| 它可以将CONFIG字典中的键值对转化为类的属性和值

一般在最底层的类(\ ``Container``,\ ``Animation``)中的\ ``__init__``\ 方法第一行会
调用这个函数\ ``digest_config(self, kwargs)``\ 将CONFIG字典和kwargs都转化为属性，
可以直接通过\ ``self.``\ 访问，简化了类之间继承的处理

**下面是一个实例**：

``manimlib/mobject/geometry.py``\ 中有很多类继承的关系

.. code:: python

   # 711行
   class Polygon(VMobject):
       CONFIG = {
           "color": BLUE,
       }

.. code:: python

   # 813行
   class Rectangle(Polygon):
       CONFIG = {
           "color": WHITE,
           "height": 2.0,
           "width": 4.0,
           "mark_paths_closed": True,
           "close_new_points": True,
       }

Polygon类通过在CONFIG字典中的键值对\ ``"color": BLUE,``\ 添加了\ ``self.color``\ 这个属性，
在父类VMobject中访问\ ``self.color``\ 对Polygon上色

| 同时Rectangle类在CONFIG字典中也含有键color，但值不同，此时会利用优先级将\ ``self.color``\ 这个属性修改为\ ``WHITE``
| 而且还通过键值对\ ``"height": 2.0``\ 等设置了一些特有的属性，方便后面使用

CONFIG字典嵌套
^^^^^^^^^^^^^^

CONFIG字典支持嵌套，即键的值也为一个字典，例如

.. code:: python

   class Camera(object):
       CONFIG = {
           "background_image": None,
           "pixel_height": DEFAULT_PIXEL_HEIGHT,
           "pixel_width": DEFAULT_PIXEL_WIDTH,
           "frame_rate": DEFAULT_FRAME_RATE,
           "frame_height": FRAME_HEIGHT,
           "frame_width": FRAME_WIDTH,
           "frame_center": ORIGIN,
           "background_color": BLACK,
           "background_opacity": 1,
           "max_allowable_norm": FRAME_WIDTH,
           "image_mode": "RGBA",
           "n_channels": 4,
           "pixel_array_dtype": 'uint8',
           "z_buff_func": lambda m: np.round(m.get_center()[2], 2),
           "cairo_line_width_multiple": 0.01,
       }

.. code:: python

   class Scene(Container):
       CONFIG = {
           "camera_class": Camera,
           "camera_config": {},
           "file_writer_config": {},
           "skip_animations": False,
           "always_update_mobjects": False,
           "random_seed": 0,
           "start_at_animation_number": None,
           "end_at_animation_number": None,
           "leave_progress_bars": False,
       }

       def __init__(self, **kwargs):
           Container.__init__(self, **kwargs)
           self.camera = self.camera_class(**self.camera_config)

Camera类的CONFIG字典含有很多键值对，而且Scene类中需要调用这个类，
为了更方便的控制，Scene类中有一个特殊的键值对\ ``"camera_config": {}``\ ，
它的值是一个字典，通过初始化Camera类的时候作为kwargs传入，修改Camera类的属性的值

所以CONFIG字典的嵌套 **本质** 上是将值作为kwargs传入

常见使用方法
^^^^^^^^^^^^

在自己写类的时候，可以通过CONFIG来添加属性或者修改父类的属性

最常用的还是在编写Scene的时候，用来修改camera的属性

.. code:: python

   CONFIG = {
       "camera_config": {
           "background_color": WHITE,
       },
   }

例如添加如上字典，更改背景颜色为白色，等等


