Chinese中文等
====================

相关设置见群文件“manim常见问题.pdf”m,Latex等辅助软件要安装正确，可以LaTeX试试运行ctex模板能否正常使用。

TextMobject 和 TexMobject 使用的都是 LaTeX 语法 其中 TextMobject 文字模式相当于直接在 L ATEX 环境下书写 TexMobject 公式模式使用的是 L ATEX 的 \begin{align*} 环境或者可以看成加了 $$ 的环境 

使用 TextMobject 与 TexMobject 书写公式时

    - TextMobject("文字$公式$")⇐⇒TexMobject("\\text{文字}公式") 


TextMobject和之间的主要区别TexMobject是，文本数学对象假定所有内容都是纯文本，除非指定带有美元符号的方程式；
而Tex数学对象假定所有内容都是方程式，除非使用指定了某些内容是纯文本\text{}。

请注意，如果使用原始字符串，例如，不需要双反斜杠。

常见问题.pdf中提到，TexMobject 中换行是：四个右划线 \\\\，Python 转义右划线，所以涉及到 \ 的均要写成两个 \\，而换行在 L ATEX 中 是两个右划线，所以要写成四个6
 


class TextMobject_TexMoject(Scene),依稀记得下面代码的来源是manim仓库的issuse。

.. code:: 

    class TextMobject_And_TexMoject(Scene): 
        def construct(self): 
            #要先设置CTEX=TRUE再运行这行，调用的是xelatex。text = TextMobject("中文")
            text1 = TextMobject("eng$\lambda$lish","Plus")
            text2 = TexMobject("\lambda\\text{Text English}")
            text3 = TexMobject(r"\lambda\text{Text English .}")
            text=Text('''これは\nmanimのあるアニ\nメーションです''',font='Source Han Sans')
           # text=Text("中文测试",font="Microsoft YaHei",stroke_width=5)
    
            self.play(Write(text))
            self.wait(3)
            self.remove(text)
            self.play(Write(text1))
            self.wait(2)
            self.remove(text1)
            self.play(Write(text2))
            self.wait(2)
            self.remove(text2)
            self.play(Write(text3))
            self.wait(2)


.. code:: 

    #写中文记得修改constants.py
    #文字演示，包括中英文日语韩语大小颜色粗细变换设置梯度颜色渐变
    class Demo_Text(Scene):
        def construct(self):
            #text = Text('Hello, world!')
            #text = Text('Hello, world!', t2f={'world':'Forte'})
            #text = Text('Hello', color=BLUE)
            #text.set_color(BLUE)
            #text[2:3].set_color(BLUE)
            #text = Text('Hello, world!', t2c={'world':BLUE})
            #text = Text('Hello', gradient=(BLUE, GREEN))
            #text.set_color_by_gradient(BLUE, GREEN)
            #text.set_color_by_t2c({'world':BLUE})
            #text[7:12].set_color_by_gradient(BLUE, GREEN)
            #text = Text('Hello, world!', t2g={'world':(BLUE, GREEN)})
            #text.set_color_by_t2g({'world':(BLUE, GREEN)})
            #text = Text('Hello', font='Source Han Sans')
            #text = Text('Hello, world!', t2f={'world':'Forte'})
            #text = Text('Hello', slant=ITALIC)
            #text = Text('Hello, world!', t2s={'world':ITALIC})
            #text = Text('Hello', weight=BOLD)
            #text = Text('Hello, world!', t2w={'world':BOLD})
            #text = Text('Hello', size=5)
            #text = Text('Hello\nWorld', lsh=1.5)
            #text = Text('Google',t2c={'[:1]':'#3174f0', '[1:2]':'#e53125','[2:3]':'#fbb003', '[3:4]':'#3174f0','[4:5]':'#269a43', '[5:]':'#e53125',})
            #script = '''Hello\n你好\nこれわ，\nTridu33センサーです。\n姓名'''
            #text = Text(script, font='Source Han Sans')
            #text=Text("これは\nmanimのあるアニ\nメーションです\n$\lambda$"+"Plusλ",font='Source Han Sans')
            #纯文本，不能解析latex文本的公式，但是可以中文输入λ，A=B+C等字符
            #要输入中文混杂英文难道只能分别Text合并TexMobject吗？为什么旧版TexMobject中英文混合完全没毛病？
           
            text=Text('''これは\nmanimのあるアニ\nメーションです''',font='Source Han Sans')
            self.play(Write(text))


.. code:: 

    # 增添文本
    class AddingText(Scene):
        #Adding text on the screen
        def construct(self):
            my_first_text=Text('''Writing with manim is funny''', font='Source Han Sans')
            second_line=Text('''and easy to do!''', font='Source Han Sans')
            second_line.next_to(my_first_text,DOWN)
            third_line=Text('''for me and you!''', font='Source Han Sans')
            third_line.next_to(my_first_text,DOWN)
    
            self.add(my_first_text, second_line)
            self.wait(2)
            self.play(Transform(second_line,third_line))
            self.wait(2)
            second_line.shift(3*DOWN)
            self.play(ApplyMethod(my_first_text.shift,3*UP))
            ###Try uncommenting the following###
            #self.play(ApplyMethod(second_line.move_to, LEFT_SIDE-2*LEFT))
            #self.play(ApplyMethod(my_first_text.next_to,second_line))

.. code:: 

    #文本动画
    class AddingMoreText(Scene):
        #Playing around with text properties
        def construct(self):
            quote = TextMobject("Imagination is more important than knowledge")
            quote.set_color(RED)
            quote.to_edge(UP)
            quote2 = TextMobject("A person who never made a mistake never tried anything new")
            quote2.set_color(YELLOW)
            author=TextMobject("-Albert Einstein")
            author.scale(0.75)
            author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
    
            self.add(quote)
            self.add(author)
            self.wait(2)
            self.play(Transform(quote,quote2),
              ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
            
            self.play(ApplyMethod(author.scale,1.5))
            author.match_color(quote2)
            self.play(FadeOut(quote))


.. code:: 

    # 旋转高亮
    class RotateAndHighlight(Scene):
        #Rotation of text and highlighting with surrounding geometries
        def construct(self):
            square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
            label=TextMobject("Text at an angle")
            label.bg=BackgroundRectangle(label,fill_opacity=1)
            label_group=VGroup(label.bg,label)  #Order matters
            label_group.rotate(TAU/8)
            label2=TextMobject("Boxed text",color=BLACK)
            label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
            label2_group=VGroup(label2,label2.bg)
            label2_group.next_to(label_group,DOWN)
            label3=TextMobject("Rainbow")
            label3.scale(2)
            label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
            label3.to_edge(DOWN)
    
            self.add(square)
            self.play(FadeIn(label_group))
            self.play(FadeIn(label2_group))
            self.play(FadeIn(label3))















