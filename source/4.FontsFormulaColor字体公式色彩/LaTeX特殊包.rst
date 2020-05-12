
LaTeX特殊包
~~~~~~~~~~~~

群文件常见问题.pdf中提到：

在 manimlib 目录下的 ctex_template.tex 或者 tex_template.tex 文件中添加外部包的名称。

拿音符为例，因为是在 harmony 包中的，所以在 tex 文件中添加 ``\usepackage{harmony}``

然后新建一个 py 文件，写入代码 ::

    from manimlib.imports import * 
    class TestHarmony(Scene): 
        def construct(self): 
            harmony = TextMobject( 
            "\\AAcht \\AAcht \\AAcht \\AAcht \\AAcht", 
            color=WHITE, 
            stroke_width=1, 
            stroke_opacity=1, 
            )
            self.play(ShowCreation(harmony)) 
            self.wait() 

运行 py 文件即可。


Q12: 使用 L ATEX 外部包，编译错误或者无显示 首先，并不是所有外部包都能在 manim 中顺利使用, 大多都不支持 xelatex 编译，
所以建议需要使用外部包时只用 latex 编译 9 至于有些群友常用 TiKz 这个外部包，也是使用 latex 才能编译，
在 xelatex 用 \draw 会无法 显示 需要修改 tex_template.tex 文件，修改成如下::

    \documentclass[preview, dvisvgm]{standalone} 

新建 py 文件，

写入代码 ::

    class TestTikz(Scene): 
        def construct(self): 
            text = TextMobject( 
                r""" 
                \begin{tikzpicture}
                \draw (−1, 0) −− (1, 0); 
                \end{tikzpicture} 
                """, 
                color=WHITE, 
                stroke_width=1, 
                stroke_opacity=1,
            ) 
            self.play(ShowCreation(text)) 
            self.wait()


建议看这个教程，https://www.bilibili.com/video/BV1W4411Z7Zt?p=23