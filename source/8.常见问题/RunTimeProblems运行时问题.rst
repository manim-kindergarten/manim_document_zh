RunTimeProblems运行时问题
============================


.. _runtimeProblem:





1. **import** 问题

**Q** 1:没有模块 big\_ol\_pile\_of\_ manim\_imports

   将文件中的

   from big\_ol\_pile\_of\_manim\_imports import \*

   改成

   from manimlib.imports import *

**Q** 1. **LATEX** 问题

Q1:报错 Latex error converting to dvi

   先不要管错误在哪，先把manimlib/constants.py中的\ **TEX**\ \_\ **USE**\ \_\ **CTEX**\ 改成True再运行

**Q** 2:报错 xelatex error converting to xdv

   | 若为 Windows 系统，先把 manimlib/constants.py 的第 29 行
   | **MEDIA\_DIR** = "./\ **media**"

   改成

   MEDIA\_DIR = os.path.join(os.getcwd()， "media")

   再进行尝试

   I.若安装的\ **[TeX]{.smallcaps}**\ 发行版为MiKTEX

   1. **MiKTEX**\ 的有关路径是否添加到环境变量中

   2. 是否有包没有装全

   | 对于\ **2.**\ ，可以正常运行一遍\ **WriteStuff**\ 场景，看是否又框弹出提示\ **install**\ 什么东西，如
   | 果有，则\ **install**\ ，并重复运行安装运行安装...直到不报错为止。或者使用\ **tex**\ 编辑器
   | (**TEXStudio**)并使用\ **xelatex**\ 手动编译\ **media/Tex**\ 文件夹中的\ **.tex**\ 文件，查看是否有包
   | 没有安装

   II.若安装的TEX发行版为TXLive

   1. **TXLive**\ 有关路径是否添加到环境变量中

   2. 安装的是否为\ **full**\ 版本

   **Ill.**\ 若安装的LaTeX发行版不为以上两款

      建议换成\ **TXLive-full**\ 版或者\ **MiKTX**,并且在重新安装前请删除旧版

**Q3:**\ 报错在文件夹内找不到\ **svg**\ 文件

   | 清空\ **media/Tex**\ 文件夹内全部内容，再次运行带文字的场景，查看\ **Tex**\ 文件夹中的内容
   | **I.**\ 若仅有\ **tex**\ 文件和\ **log**\ 文件，按照\ `2.2 <#bookmark19>`__\ 中方法处理
   | **II.**\ 若含有\ **xdv**\ 文件但没有\ **svg**\ 文件

1. divsvgm是否添加到环境变量，可以使用dvisvgm

      --version观察是否由报错来检查

2. dvisvgm版本是否过低，若dvisvgm

      | --verison的输出版本号为1开头，请更换新版dvisvgm`[^4] <#bookmark3>`__
      | 并注意将含有dvisvgm的文件夹添加到环境变量中

2.3中文显示问题

**Q** 1:含有中文的 TextMobject 编译报错 Latex error converting to dvi

   将 manimlib/constants.py 中的 TEX\_USE\_CTEX 改成 True 再尝试

**Q2:**\ 英文可以正常显示，中文不报错，但不显示

   考虑使用的是否为TextMobject而不是TexMobject

2.4文字问题

**Q** 1: TextMobject 和 TexMobject 有什么区别

   | TextMobject 和 TexMobject 使用的都是 LTEX 语法
   | 其中TextMobject文字模式相当于直接在LTEX环境下书写

   | TexMobject公式模式使用的是LTEX的\\begin{align\*}环境或者可以看成加了
   | $$的环境 使用TextMobject与TexMobject书写公式时

   TextMobject("文字$公式$")令今 TexMobject("\\\\text{文字}公式■'）

**Q** 2: TextMobject中怎么改字体

   **TextMobject**\ 中只能使用\ **LTEX**\ 的内置字体族和字体形状，包括：

   •罗马字体 \\textrm{textrm}

   •无衬线字体 \\textsf{textsf}

   •打字机字体 \\texttt{texttt}

   •直立形状 \\textup{textup}

   •意大利形状\\textit〇eo:\^}

   •倾斜形状 \\textsl{texts1}

   •小型大写 \\textsc{**TEXTSC**}

**Q3:**\ 想自定义字体怎么办

| 使用新版\ **manim**\ 特有的\ **Text**\ 〇类，方法如下\ **Text("**\ 文字\ **"**\ ，\ **font="**\ 字体"），其中字体要填
| 写在计算机内存储的格式\ `[^5] <#bookmark24>`__,但是不能使用\ **LTX**\ 语法书写公式

**Q4:**\ 想用自定义字体写公式怎么办

可以使用群文件里\ **cigar**\ 666编写的\ **MyText**\ ()类

   Cigar牛逼

Q5: TexMobject中换行是什么

| 四个右划线\ **\\\\\\\\**\ ，\ **Python**\ 转义右划线，所以涉及到\ **\\**\ 的均要写成两个\ **\\\\**\ ，而换行在\ **LTX**\ 中
| 是两个右划线，所以要写成四个\。

**Q6:**\ 公式怎么对齐

   I.直接在TexMobject中使用&对齐

   | II. 两个 mobject 对齐，使用
   | > obj2.next\_to(obj1，DOWN，aligned\_edge=LEFT)使 obj2 在 objl

   下方，并且左对齐

   | III. VGroup 内对齐，使用 group.arrange(DOWN，aligned\_edge=LEFT)使
   | VGroup 中的子兀素依次向下排开，并左对齐

   写公式的示例：

   `https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/ <https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/3_text_like_arrays/scenes.md>`__

   `3\_text\_like\_arrays/scenes.md <https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/3_text_like_arrays/scenes.md>`__

**Q** 7: TexMobject上色问题的处理办法

   I.将上色的字符分开，使用text[i].set\_color(color)来上色

   II.
   将上色的字符分开，使用text.set\_color\_by\_tex\_to\_color\_map(t2c)传入t2c字典来对相

   同的字符串上色

   III.
   只传入一个字符串，但同时传入\ **tex\_to\_color\_map=t2c**\ 来自动拆分上色（容易出问题）

   IV.
   只传入一个字符串，使用\ **text[0][i]**\ 来对细小的路径上色（一般是一个字符一个下标）

**Q** 8: TexMobject的下标怎么分析

   创建函数

   def debugTeX(self, texm):

   for i, j in zip(range(100), texm):

      tex\_id = TextMobject(str(i)).scale(0.3).set\_color(PURPLE)

      tex\_id.move\_to(j)

      self.add(tex\_id)

   | 在使用时先self.add(tex)然后再debugTeX(self,
   | tex),导出最后一帧

   观察每段字符上的标号，即为下标{.underline}

**Q** 9: TexMobject使用\\frac拆分时出错

   | 这个是\ **Grant**\ 写\ **tex\_file\_writing.py**\ 的一个\ **bug**,建议使用{分子\\\ **over**\ 分母}来代替
   | \\\ **frac**\ {分子}{分母}

2.5素材引用问题

**Q** 1:使用SVGMobject找不到svg文件

   | **I**.直接使用绝对路径引用\ **svg**\ 文件
   | **II**.将\ **svg**\ 文件放到\ **assets/svg\_images/**\ 文件夹中

**Q** 2:如何使用jpg或者png文件

   | **I**.直接使用绝对路径引用，并使用ImageMobject **II**.将
     **jpg/png**
   | 文件放到 assets/raster\_images/ 文件夹中


