Problems其他问题
====================

.. _Others:



**Q1:**\ 有什么manim教程


1. 群主\ **cigar**\ 666的\ **B**\ 站专栏

-  https://www.bilibili.com/read/readlist/rl82339

1. **pdcxs**\ 大大转载的\ **manim**\ 教程

-  https://www.bilibili.com/video/av64023740

..

   | •源码
   | https://github.com/Elteoremadebeethoven/AnimationsWithManim

1. GitHub上cai-hust的中文教程

-  https://github.com/cai-hust/manim-tutorial-CN


**Q2:**\ 没有manim源码

最好不要使用\ **pip install
manimlib**\ 来装manim,请在GitHub上clone下来manim的全部内容

**Q3:**\ 群友用的\ **manim**\ 都是什么版本

   **manim**\ 不看版本，一般使用的都是最新版\ **code**\ 。\ **release**\ 里面带版本号的都可以看作旧版

**Q4:**\ 如何使用傅里叶级数作图

套用\ **Grant**\ 写好的文件


.. code::

   active\_projects/diffyq/part2/fourier\_series.py

   active\_projects/diffyq/part4/fourier\_series\_scenes.py

   active\_projects/diffyq/part4/long\_fourier\_series.py

   只需要更换\ **svg**\ 素材即可（自己制作，或者使用群里的\ **svg**\ 素材）

**Q5: svg**\ 用什么软件制作

   | Adobe
   | Illustrator(简称AI)或者inkscape(简称ink)。尽量不要使用网页版编辑器

**Q6:** 一些比较复杂，操纵东西比较多的动画怎么做

使用外部剪辑软件，例如\ **Adobe** **Premiere** **Pro**\ 或者达芬奇

**Q7:** 一个self.play里写两个ApplyMethod只对一个起作用怎么办 

去掉 ApplyMethod

**Q8**:动画怎么显示旋转一个物体

使用\ **Ratate**\ 和\ **Rotating**\ ，区别在群文件中有视频

**Q9:**\ 怎么控制物体移动或者\ **Transform**\ 的加速度

使用\ **rate\_func**, ---些**manim**\ 中己经定义的在群文件中有视频

**Q10:**\ 数学符号\ **/**\ 公式用\ **LTEX**\ 怎么打

参见

https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan


**Q11:** 使用一些特殊\ **LTEX**\ 的外部包

如何使用\ **manim**\ 画出音符，或怎么使用这些包？

在\ **manimlib**\ 目录下的\ **ctex**\ \_\ **template**.\ **tex**\ 或者\ **tex**\ \_\ **template**.\ **tex**\ 文件中添加外部包的名称\ 

就拿音符为例，因为是在\ **harmony**\ 包中的，所以在\ **tex**\ 文件中添加\ **\\usepackage{harmony}**

然后新建一个\ **py**\ 文件，写入代码

.. code::

   from manimlib.imports import * 
   class TestHarmony(Scene): 
      def construct(self):
         harmony = TextMobject(
            "\\AAcht \\AAcht \\AAcht \\AAcht \\AAcht",
            color=WHITE,   
            stroke\_width=1,   
            stroke\_opacity=1,
         )
         self.play(ShowCreation(harmony)) 
         self.wait()

运行\ **py**\ 文件即可

**Q12:**\ 使用\ **[LTeX]{.smallcaps}**\ 外部包，编译错误或者无显示

首先，并不是所有外部包都能在\ **manim**\ 中顺利使用，大多都不支持\ **xelatex**\ 编译，所以建议需
要使用外部包时只用\ **latex**\ 编译\ 

至于有些群友常用\ **TiKz**\ 这个外部包，也是使用\ **latex**\ 才能编译，在\ **xelatex**\ 用\ **\\draw**\ 会无法

显示

需要修改tex\_template.tex文件，修改成如下：

   \documentclass[preview, dvisvgm]{standalone}

新建\ **py**\ 文件，写入代码

.. code::

   class TestTikz(Scene): def construct(self):

   text = TextMobject( 
         r"""
         \\begin{tikzpicture}
            \\draw (−1, 0) −− (1, 0);
         \\end{tikzpicture}
         """,
         color=WHITE, 
         stroke_width=1, 
         stroke_opacity=1,
   )
   self.play(ShowCreation(text)) 
   self.wait()

运行\ **py**\ 文件即可

**Q13** :如何解决二维画面中的图层问题

使用\ **z**\ 轴坐标对图层进行区分是无效的

可以使用\ **pdcxs**\ 添加的\ **plot**\ \_\ **depth**\ ，具体更改见下图
 


.. figure:: /assets/image/Problem1.JPG
    :width: 50%
    :align: center


**plot depth** 的值越大，运行出来的物体就越在上面

**Q14** :如何导出gif文件

在新版本中，\ **manim**\ 导出\ **gif**\ 己经失效，可以导出\ **mp**\ 4,后用\ **ffmpeg**\ 转换。也可以按照下图
修改源码

.. figure:: /assets/image/Problem2.JPG
    :width: 50%
    :align: center

..

   改过后，在输入命令时加上-\ **i**\ 选项，就能导出\ **gif** 了

**Q15**:如何导出透明的图片或者视频

在运行命令的时候加上-\ **t**\ 选项

•如果是-\ **s**\ 保存图片，则会存储为背景透明的\ **png**\ 图片

•如果是-\ **l**/-**m**/-**w**\ 保存视频，则会存储为背景透明的\ **mov**\ 视频文件，方便\ **pr**\ 中的剪辑

**Q16**:;宣染视频的画质和巾贞率怎么调整

**manim**\ 的默认画质有四种

-  -1最低画质480**P**\ 15

-  -**m**\ 中等画质720\ **P**\ 30

-  -**high**\ \_\ **qua**\ 1\ **ity**\ `[^10]  [2]_ <#bookmark8>`__
   高画质

      1080\ **P**\ 60

-  -**w**\ 导出（最高）画质1440\ **P**\ 60(2\ **K**)

..

   不加画质选项，默认使用-\ **w**\ 最高画质。可以通过修改\ **constants**.\ **py**\ 中对应的画面长宽和中贞

率来修改

   一般把-\ **w**\ 最高画质修改成1080\ **P**\ 60
   (**B**\ 站支持的最高画质）

**Q17**: 有没有什么好的场景例子供学习

1. **Grant**\ 的代码\ `[^13] <#bookmark11>`__\ 对应3\ **B**\ 1\ **B**\ 的视频，可能会有报错，需要魔改

2. 群文件里"\ **manim**\ 相关的\ **python**\ 代码及视频结果"

3. 群里几个\ **B**\ 站\ **up**\ 主的\ **GitHub**\ 库对应他们的代码

-  cigar666

      | `https://github.\ com/cigar\ 666/\ my\ \_\ manim\_projects <https://github.com/cigar666/my_manim_projects>`__
      | •鹤翔万里
      | `https://github.\ com/Tony\ 031218/\ manim-projects <https://github.com/Tony031218/manim-projects>`__

-  pdcxs

      `https://github.\ com/pdcxs/ManimProjects <https://github.com/pdcxs/ManimProjects>`__

..

   | •有一种悲伤叫额废
   | `https://github.\ com/136108Haumea/my-manim <https://github.com/136108Haumea/my-manim>`__\ `[^14] <#bookmark11>`__

   
