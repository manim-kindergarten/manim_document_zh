


CONFIG
========


.. admonition:: 前置知识

   前置知识，CONFIG配置变量参数属性和自定义工具类， 这部分主要是学习的这个比较好的 `视频教程这一节 <https://www.bilibili.com/video/BV1W4411Z7Zt?p=14>`_  ，因为真的很细，但是不想每次要用一个个视频去翻，我决定mark下来一些有用的方便平时使用。




这里讲Config设置，config字典变量参数设置  ConfigExample


.. code:: 

    class ConfigExample1(Scene): 
        CONFIG={
            "text_1":"Text 1",#字典中定义的变量可以被类内所有方法使用
            "text_2":"Text 2"
            } 
        def construct(self):
            t1=TextMobject(self.text_1)#t1是construct方法中定义的，只能在内部使用
            self.play(Write(t1))

.. code:: 

    #能运行，等效
    class ConfigExample2(Scene): 
        CONFIG={
            "text_1":"Text 1",#字典中定义的变量可以被类内所有方法使用
            "text_2":"Text 2"
            } 
        def construct(self):
            self.custom_method()
    
        def custom_method(self) :   
            t1=TextMobject(self.text_1)#t1是construct方法中定义的，只能在内部使用
            self.play(Write(t1))

.. code:: 

    '''
    class ConfigExample(Scene): 
        CONFIG={
            "text_1":"Text 1",#字典中定义的变量可以被类内所有方法使用
            "text_2":"Text 2"
            } 
        def construct(self):
            self.custom_method()
            self.play(Write(t1))#t1未定义，因为consruct不能使用custom_method()中定义的私有的t1
    
        def custom_method(self) :   
            t1=TextMobject(self.text_1)#t1是construct方法中定义的，只能在内部使用
            
    '''
    #能运行
    #字典中定义的变量可以被类内所有方法使用
    # 继承自Scene,查看其config字典有"camera_class":=Camera,相机类选用的是Camera类
    # "camera_config" = {}相机类配置默认,而camera 的默认属性config定义在manimlib/camera/camera.py第39行中，查看字典的默认值"background_color": BLACK背景颜色默认是黑色，我们可以修改为"background_color": RED
    # 类似的其他所有属性也是这样设置，或者ctrl点击来查询默认值。3b1b的源码慢慢学习，相信笔记会越来越清晰的。

.. code:: 

    class ConfigExample3(Scene): 
        CONFIG={
            "camera_config" : {"background_color": RED},
            "text_1":"Text 1",#字典中定义的变量可以被类内所有方法使用
            "text_2":"Text 2"
            } 
        def construct(self):
            self.custom_method()
            self.play(Write(t1))#t1可以用
    
        def custom_method(self) :   
            self.t1=TextMobject(self.text_1)#加个self.定义的可以被类内所有方法使用，其实self是指实例化后的类的 实例本身，相当于self.t1属性变量赋值t1
            '''
            和普通数相比，在类中定义函数只有一点不同，就是第一参数永远是类的本身实例变量self，并且调用时，不用传递该参数。
            除此之外，类的方法(函数）和普通函数没啥区别，
            可以用默认参数、可变参数或者关键字参数（*args是可变参数，args接收的是一个tuple，**kw是关键字参数，kw接收的是一个dict）。
            '''














