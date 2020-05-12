ManimLibrary库
=========================

计划中下面几个章节标题为“XXX类的属性和方法”是准备介绍manimlib的代码的，但是太多，似乎elteoremadebeethoven都感觉太无聊肝不下去导致TODO一年都没动静（不过基本每个人都有自己要忙的事情 -_-#）,用的是Sphinx插件sphinx.ext.autodo，具体怎么使用他这部分文档看 `这集 <https://www.bilibili.com/video/BV1W4411Z7Zt?p=13>`_  ,主要形式是:

.. code::
    
    文件位置
    参数
    类的类型
    参数类型
    名字（类型）--描述
    CONFIG参数


之所以把elteoremadebeethoven大神这几个没写完的常用源码类库解析章节复制到这里，我的想法是，万一以后闲着没事儿研究源码或者manim做的旧项目的代码研究出什么新的可以写这里？最吸引人的地方在于这种方式直接用 manimlib源码生成sphinx.ext.autodo文档，然后每个后续都有demo代码+视频用法！真正小白能懂，但是可能有点太多啦。



实际上我更喜欢用PyDoc，因为可以动态查询，PyDoc自动生成,详情可以看这里PyDoc生成的结果 :ref:`manim类属性方法 <manimlibClassesPropertiesMethods>` 。


其实最开始文档分类是打算根据manimlib的分类（animation、camera、container、mobject、scene、utils）进行的，但是索引查询+搜索查询才是好用的文档，manimlib也是类似地根据功能集群进行分类。

其实我更想做的是减法，想把manim文档写厚写详细，再写薄从原理讲解如何从零组装manim+开发工具模板类（可惜我太菜了）。不过幸亏，虽然一个人的时间精力和兴趣点持续时间是有限的，但是开源社区可以前赴后继共同编辑维护一份文档，毕竟只要维护更新好一份完整统一的文档对社区用户推广很有意义。

 Copyright - This document has been placed in the public domain.


.. toctree::
    :caption: Contents
    :maxdepth: 2

    manim_packages包
    manim_类属性方法
    ManimLibrary库
    
