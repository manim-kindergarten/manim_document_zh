demo
=========================

其实我觉得代码注释写好，还是能直接看的，但是也许可以有更直观的管理方案：那就是把工程中遇到的需要使用的工具类模板方法等等，直接剥离出来使用“最小可实现用例demo”，写成rst文件，然后在文档中 make html 使用 Sphinx 转换成为html网页文件，随便找个地方托管，就能在线看网页文档。

当然，写工具类分享者已经挺麻烦的，不能苛求文档还要过分精美细致，毕竟代码才是最好的文档，但是好文档对扩展用户群，吸引别人关注你的github仓库有很重大的影响。但是作为文档，也许内容已经太冗长了，也许应该在  `manim-kindergarten-manim_sandbox <https://github.com/manim-kindergarten/manim_sandbox>`_    新建一个Sphinx文档，专门写附加的类和方法。

具体的代码和视频（Up主可以插入视频链接）插入rst语法可以是这样的::

    .. code:: 

        from manimlib.imports import *

    .. code:: 

        class PlotGraph(GraphScene):
            CONFIG = {
                "xxx" : yy,
                "xxxx":yyyy
            }
        
            def construct(self):
                XXXXXXXXXXXXXXXXXXXXXXXX



    .. raw:: html

        <video width="560" height="315" controls>
            <source src="../_static/assets下的子文件夹/视频名称.mp4" type="video/mp4">
        </video>
    
插入代码还能这样::

    .. literalinclude:: ../assets/code/manim-tutorial/graphing.py
   :linenos:


插入文件的第几行到第几行，行号开头数字::

    .. literalinclude:: ./manimlib/constants.py
        :lines: 197-258
        :lineno-start: 197

Sphinx有插件能够自动生成文档，写法是这样的::

    .. autoclass:: manimlib.mobject.geometry.Line
    :members:


    .. autoclass:: manimlib.mobject.svg.tex_mobject.TexMobject
    .. automethod:: manimlib.mobject.svg.tex_mobject.TexMobject.get_tex_string
    .. automethod:: manimlib.mobject.svg.tex_mobject.TexMobject.set_color_by_tex


插图::

    .. figure:: ../assets/image/图片名称.png
    :alt: 



然后Sphinx语法很多教程连国内驰名的史上最垃圾的搜索引擎都能直接搜到（建议用别的搜索引擎），就不赘述了。下面举两个例子说明下对于工具类管理，我的设想方案。
