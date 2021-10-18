Text
============

:class:`~manimlib.mobject.svg.text_mobject.Text` 使用 ``cairo`` 来生成文字的svg，
所以它不需要 ``LaTeX`` 环境，而且可以方便地更改字体，但是不能够书写公式。
需要更改字体，而且要使用公式的，可以尝试cigar666编写的 `MyText <https://github.com/manim-kindergarten/manim_sandbox/blob/master/utils/mobjects/MyText.py>`_

MK 做了一个关于常用 :class:`~manimlib.mobject.svg.text_mobject.Text` 的视频：
`〔manim教程〕第四讲 SVG、图片与文字  <https://www.bilibili.com/video/BV1CC4y1H7kp>`__


由于这个类的作者 XiaoYoung 写了中文的文档，这里就不放出文档字符串了，下方给出原版文档

Text
****
.. autoclass:: manimlib.mobject.svg.text_mobject.Text

.. manim-example:: TextDemo
  :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image1.png

  from manimlib.imports import *
  
  class Demo(Scene): 
      def construct(self): 
          text = Text('Hello, world!')
          self.play(Write(text))

MarkupText
***********
.. autoclass:: manimlib.mobject.svg.text_mobject.MarkupText
    :members:

Code
***********
.. autoclass:: manimlib.mobject.svg.text_mobject.Code
    :members:


**以下为 Text 类的说明**：

-  ``text``:

   -  接收一个\ ``str``\ ，如\ ``'Hello, world!'``
   -  不支持LaTex语法
   -  如果只有一行，字符串前后的空格会被忽略(指不会产生长度，但是这些空格会被计算，可以用下标访问)
   -  ``\t``\ 默认会被替换为4个空格，可以通过调整tab_width改变这一行为

-  ``color``:

   -  接收一个\ ``str``\ ，如\ ``'#FFFFFF'``
   -  或者是定义在\ ``constants.py``\ 里的颜色常量，如\ ``BLUE``
   -  Demo
 
      -  ``text = Text('Hello', color=BLUE)`` |color|

-  ``t2c``:

   -  ``text2color``\ 的缩写
   -  接收一个\ ``dict``\ ，如\ ``{'text': color}``
   -  或者切片模式，如\ ``{'[1:4]': color}``
   -  Demo
 
      -  ``text = Text('Hello, world!', t2c={'world':BLUE})`` |t2c|

-  ``gradient``:

   -  接收一个\ ``tuple``\ ，如\ ``(BLUE, GREEN, '#FFFFFF')``
   -  Demo
 
      -  ``text = Text('Hello', gradient=(BLUE, GREEN))`` |gradient|

-  ``t2g``:

   -  ``text2gradient``\ 的缩写
   -  接收一个\ ``dict``\ ，如\ ``{'text': (BLUE, GREEN, '#FFFFFF')}``
   -  或者切片模式，如\ ``{'[1:4]': (BLUE, GREEN, '#FFFFFF')}``
   -  Demo
 
      -  ``text = Text('Hello, world!', t2g={'world':(BLUE, GREEN)})`` |t2g|

-  ``font``:

   -  接收一个\ ``str``,
          如\ ``'Source Han Sans'``\ ，请确保字体名正确
   -  不支持直接读取给定的字体文件路径，必须先将字体安装到系统中才能使用
   -  Demo
 
      -  ``text = Text('Hello', font='Source Han Sans')`` |font|

-  ``t2f``:

   -  ``text2font``\ 的缩写
   -  接收一个\ ``dict``\ ，如\ ``{'text': 'Source Han Sans'}``
   -  或者切片模式，如\ ``{'[1:4]': 'Source Han Sans'}``
   -  Demo
 
      -  ``text = Text('Hello, world!', t2f={'world':'Forte'})`` |t2f|

-  ``slant``:

   -  斜体选项: ``NORMAL``\ 或者\ ``ITALIC``
   -  其实还有一个\ ``OBLIQUE``\ ，但是貌似效果跟\ ``ITALIC``\ 一样
   -  Demo

      -  ``text = Text('Hello', slant=ITALIC)`` |slant|

-  ``t2s``:

   -  ``text2slant``\ 的缩写
   -  接收一个\ ``dict``\ ，如\ ``{'text': ITALIC}``
   -  或者切片模式，如\ ``{'[1:4]': ITALIC}``
   -  Demo

      -  ``text = Text('Hello, world!', t2s={'world':ITALIC})`` |t2s|

-  ``weight``:

   -  字重(粗细)选项: ``NORMAL``\ 或者\ ``BOLD``
   -  目前只支持调用\ ``NORMAL``\ 和\ ``BOLD``\ 是因为底层的包不支持其它选项
   -  如果想用Light、Condensed等选项可以在调用字体的时候声明，如\ ``'Open Sans Light'``
   -  更多有关Light等选项的问题，可以参考:
          https://github.com/3b1b/manim/issues/884
   -  Demo
 
      -  ``text = Text('Hello', weight=BOLD)`` |weight|

-  ``t2w``:

   -  ``text2weight``\ 的缩写
   -  接收一个\ ``dict``\ ，如\ ``{'text': BOLD}``
   -  或者切片模式，如\ ``{'[1:4]': BOLD}``
   -  Demo
 
      -  ``text = Text('Hello, world!', t2w={'world':BOLD})`` |t2w|

-  ``size``:

   -  不建议使用
   -  接收一个数且该数要大于0.1
   -  不是线性的，因为\ ``SVGMobject``\ 的缩放逻辑有点迷
   -  如果小于0.1可能会出现锯齿
   -  目前与MUnit没有关联，所以玄学调参
   -  如果需要精确控制大小，建议使用\ ``.scale()``
   -  Demo
 
      -  ``text = Text('Hello', size=5)`` |size|

-  ``lsh``:

   -  ``line_spacing_height``\ 的缩写
   -  不建议使用
   -  默认与\ ``size``\ 相等
   -  非线性(存疑)
   -  与MUnit没有关联
   -  Demo
 
      -  ``text = Text('Hello\nWorld', lsh=1.5)`` |lsh|

-  其它:

   -  还有一些从\ ``Mobject``\ 继承来的参数也可以使用
   -  如: ``fill_color``\ 、\ ``fill_opacity``\ 、\ ``stroke_color``\ 、\ ``stroke_width``

**CONFIG中属性**：

-  Mobjcet:

   -  ``color``: 默认为\ ``WHITE``
   -  ``heigth``: 默认为\ ``None``

-  Text:

   -  ``font``: 默认为\ ``''``
   -  ``gradient``: 默认为\ ``None``
   -  ``lsh``: 默认为\ ``-1``
   -  ``size``: 默认为\ ``1``
   -  ``slant``: 默认为\ ``NORMAL``
   -  ``weight``: 默认为\ ``NORMAL``
   -  ``t2c``: 默认为\ ``{}``
   -  ``t2f``: 默认为\ ``{}``
   -  ``t2g``: 默认为\ ``{}``
   -  ``t2s``: 默认为\ ``{}``
   -  ``t2w``: 默认为\ ``{}``
   -  ``tab_width``: 默认为\ ``4``

**方法**：

-  Mobject:

   -  ``set_color(self, color)``:
 
      -  ``text.set_color(BLUE)``
      -  ``text[7:12].set_color(BLUE)``
 
   -  ``set_color_by_gradient(self, gradient)``:
 
      -  ``text.set_color_by_gradient(BLUE, GREEN)``
      -  ``text[7:12].set_color_by_gradient(BLUE, GREEN)``

-  Text:

   -  ``set_color_by_t2c(self, t2c)``:
 
      -  ``text.set_color_by_t2c({'world':BLUE})``
 
   -  ``set_color_by_t2g(self, t2g)``:
 
      -  ``text.set_color_by_t2g({'world':(BLUE, GREEN)})``

**其它**：

-  切片模式:

   .. manim-example:: TextSlice
     :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image14.png
   
     text = Text(
         'Google', 
         t2c={
             '[:1]':'#3174f0', '[1:2]':'#e53125', 
             '[2:3]':'#fbb003', '[3:4]':'#3174f0', 
             '[4:5]':'#269a43', '[5:]':'#e53125',
         }
     )

-  UTF-8:

   .. manim-example:: TextUTF8
     :media: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image15.png
   
     from manimlib.imports import *
     
     script = '''
     Hello
     你好
     こんにちは
     안녕하세요
     '''
     
     class Demo(Scene):
         def construct(self):
             text = Text(script, font='Source Han Sans')
             self.play(Write(text))

-  目前对GBK(中日韩)文字的支持没有太大问题
-  但是对于其它文字，如印度语、阿拉伯语的显示有很大问题

.. |color| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image2.png
.. |t2c| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image3.png
.. |gradient| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image4.png
.. |t2g| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image5.png
.. |font| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image6.png
.. |t2f| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image7.png
.. |slant| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image8.png
.. |t2s| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image9.png
.. |weight| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image10.png
.. |t2w| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image11.png
.. |size| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image12.png
.. |lsh| image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/Text/image13.png
