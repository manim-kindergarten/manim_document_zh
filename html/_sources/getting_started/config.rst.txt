CONFIG字典用法
=================

什么是CONFIG字典
-----------------

CONFIG字典是manim的一个特性，方便了父子类之间参数的继承和修改

| 对于CONFIG字典的处理，在 ``manimlib/utils/config_ops.py`` 中
| 它可以将CONFIG字典中的键值对转化为类的属性和值

一般在最底层的类( ``Container``, ``Animation``)中的 ``__init__`` 方法第一行会
调用这个函数 ``digest_config(self, kwargs)`` 将CONFIG字典和kwargs都转化为属性，
可以直接通过 ``self.`` 访问，简化了类之间继承的处理

**下面是一个实例**：

``manimlib/mobject/geometry.py`` 中有很多类继承的关系

.. code-block:: python

    # Line 279
    class Circle(Arc):
        CONFIG = {
            "color": RED,
            "close_new_points": True,
            "anchors_span_full_range": False
        }

.. code-block:: python

    # Line 304
    class Dot(Circle):
        CONFIG = {
            "radius": DEFAULT_DOT_RADIUS,
            "stroke_width": 0,
            "fill_opacity": 1.0,
            "color": WHITE
        }

``Circle`` 类通过在CONFIG字典中的键值对 ``"color": BLUE,`` 添加了 ``self.color`` 这个属性，
在父类 ``VMobject`` 中访问 ``self.color`` 对 ``Circle`` 上色

同时 ``Dot`` 类在CONFIG字典中也含有键 ``color``，但值不同，此时会利用优先级将 ``self.color`` 这个属性修改为 ``WHITE``，

CONFIG字典嵌套
------------------

CONFIG字典支持嵌套，即键的值也为一个字典，例如

.. code-block:: python

    class Camera(object):
        CONFIG = {
            # configs
        }

.. code-block:: python

    class Scene(object):
        CONFIG = {
            "window_config": {},
            "camera_class": Camera,
            "camera_config": {},
            "file_writer_config": {},
            # other configs
        }

        def __init__(self, **kwargs):
            digest_config(self, kwargs)
            # some lines
            self.camera = self.camera_class(**self.camera_config)

``Camera`` 类的CONFIG字典含有很多键值对，而且 ``Scene`` 类中需要调用这个类，
为了更方便的控制，``Scene`` 类中有一个特殊的键值对 ``"camera_config": {}`` ，
它的值是一个字典，通过初始化 ``Camera`` 类的时候作为 ``kwargs`` 传入，修改 ``Camera`` 类的属性的值

所以CONFIG字典的嵌套 **本质** 上是将值作为 ``kwargs`` 传入

常见使用方法
--------------

在自己写类的时候，可以通过CONFIG来添加属性或者修改父类的属性

最常用的还是在编写Scene的时候，用来修改camera的属性

.. code:: python

   CONFIG = {
       "camera_config": {
           "background_color": WHITE,
       },
   }

例如添加如上字典，更改背景颜色为白色，等等