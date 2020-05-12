About关于
===============

Animating technical concepts is traditionally pretty tedious, since it can be
difficult to make the animations precise enough to convey them accurately.
``Manim`` uses Python to generate animations programmatically, which makes it
possible to specify exactly how each one should run.

动画技术概念在传统上非常乏味，因为很难使动画足够精确以准确地传达它们。 
``Manim`` 使用 ``Python`` 以编程方式生成动画，这使得可以准确指定每个动画的运行方式。

This project is still very much a work in progress, but I hope that the
information here will make it easier for newcomers to get started using
``Manim``.

这个项目仍在进行中，EulerTour希望这里的信息将使新手更容易上手使用Grant Sanderson的 ``Manim`` ,我想翻译EulerTour教程+笔记整合，同时在此之上，整合出方便 \-_\-#查阅使用的文档。
其实manim的版本不断在变动，所以elteoremadebeethoven出教程比较早，版本比较旧，会出现 ``AttributeError: module 'manimlib.animation.transform' has no attribute 'ComplexFunction'`` 之类的manim变动的问题，但是issues很多大神出没。

本来就是python胶水语言调用ffmpeg、LaTeX、sox等多种软件+python无敌生态类库的协同合作，很难一开始就想好尽善尽美的抽象工程结构，manimlib改动很正常，所以，manimlib/once_useful_constructs中用到的一次性工具类Grant Sanderson也很严谨地声明：

    This folder contains a collection of various things that were built for a video at some point, but were really one-off and should be given more careful consideration before being brought into the main library.  In particular, there is really no guarantee of these being fully functional.

而清晰维护及时的文档，有助于用户使用和添砖加瓦的社区发展，这就引发我产生一个想法：extensions插件商城。

extensions脚本商城
-------------------

想法很简单，一句话总结就是每个开发者自己做的工具类github保存仓库x，在汇总wiki仓库README.md中粘贴x仓库的链接和一个简短简介Demo用例。

还需要写个安装插件批处理脚本（一开始也许勉强将就点），bat或者python怎么都行，功能需求是：

一些帮助信息，传参x仓库的url时就git clone url、解压到特定的子目录下，比如manimlib//extensions， 然后文件读写，在manimlib/imports.py追加形式写入一行  `` from manimlib.extensions.x import * ``  ,或者不常用的就不追加等需要用的时候手动import。


软件，在我的看来就是封装好的批处理函数，一般我的电脑有个文件夹叫做"MyEnvPath",里面写着我常用的很多bat批处理等执行文件，然后我会给那些bat写上中文名称，比如:清理垃圾.bat,任意位置命令行输入“清理垃圾”，就能清理系统缓冲区垃圾。（手动狗头，这莫非是传说中的中文编程？）。

联想到这个是因为，前面说的安装插件的脚本批处理文件完全可以移动到MyEnvPath中，到时候安装工具类只要命令行输入：“manim安装插件”命令+x的url。其实，Cmake就是这样的简单朴素的想法，只是当考虑的问题变复杂，跨平台等等挑战导致晦涩难懂罢了。

我只是提个想法，抛砖引玉。感觉，其实各种软件社区套路都类似，只有火起来社区生态才能上去，插件市场和扩展工具类才能欣欣向荣。


不过如果想远一点的话，工具类贵精不贵多，要有Grant Sanderson般的严谨态度，插件管理要有规范约束（我是不是想太远了？）。

提起包管理软件，我不禁想，如果有大量不太完善的函数命令充斥，甚至出现令人深恶痛疾的全局污染的问题呢？nodejs那样的工程类库独占一个文件夹实在是太稳定部署方便，stack也这么整，来个局部或整体安装，虽然sandbox隔离还是很重要的，但是开发者面对内存和下载部署的耐心挑战，还有不同版本依赖性交叉等问题，恕我直言，太操蛋了。有时候，会感觉好多设计思路都好像，比如Docker分层-镜像-容器、统一管理jar包需要的时候再加、Spring的依赖注入等设计，感觉目的都是为了实现统一的资源管理和分配，降低耦合度，减少资源双方的依赖。我其实觉得这两者的关系，很像是windows下文件管理策略(比如很多软件安装目录下都有很多份mingw，gcc)和linux下的文件管理策略（统一的目录资源管理结构）的区别。这也是规范设计，制定通用标准的意义所在吧。

如果真有人要发布工具类插件什么的，最起码需要写好 " __doc__ ",python中每个modul，每个class，每个def都是留有写doc的地方的，写没写是另一回事，可以用 “对象名称.__doc__” 查看。这是一个字符串，所以内容只能是字符串允许的内容。如果字符不足以满足说明需求，可能会加上web链接，或者专门的说明函数。当然，一个好的Demo胜过千言万语。Theorem of Beethoven写的工具类真心牛逼，文档Demo都也很详尽。

我觉得，工具开发这玩意儿就是越多人用，越火，开发热情越高，极客精神就是看不爽了手撸一个，很多软件都是社区不断开发新功能，倒逼官方合并扩展功能。

而只要这个东西火了，就会有商业或者相关人员封装改良更好，做更好的优化。我真心感觉python慢，用manim的时候，满屏滚动等大半天，频繁的io读写容易降低程序的效率，长期以往甚至对磁头有不好的影响（不过那得多肝才能损害磁头？），反正我感觉现在manim就像是一个胶水代码散装“钢铁侠”，需要更底层支持的优化相关人才支持，动态一时爽重构火葬场，或者可以试试pybind11生成c/C++等调用？或者，频繁读写文件操作优化成内存缓冲区变大？自动垃圾删除辅助文件？......

但是那是软件成熟之后考虑的事情了，适当地封装a higher level of abstraction是为了更好地开发使用，比如c/java等打包整理好方便调用函数的Matlab可以mex出来C/C++，特别是一些仿真包暂时可以说是睥睨天下没对手,唉，可惜背靠大树（matlab成熟算法包很多）好乘凉的开源版Octave路漫漫其修远兮呀。

Linux设计哲学有时候越看越有意思，构建稳健的软件工程结构，真的很需要这种软件工程的知识。


1. 一切皆文件。几乎把所有的资源系统抽象为文件形式：包括硬件设备，甚至通信接口等。作用：提高资源管理效率。
 

2. 由众多功能单一的程序组成：一个程序只做一件事，并且做好;组合小程序完成复杂任务。作用：程序分工明确，运行后方便进程管理。程序代码也轻量化，高效，容易修复错误。
小程序易于理解，维护，消耗系统资源较少，易于与其他工具结合实现更多的功能。


3. 尽量避免跟用户交互。使用命令行接口执行效率更高，易于以编程的方式实现自动化任务。

 

4. 使用文本文件保存配置信息，文本文件易于阅读和编辑。

 

5. 提供机制而非策略。机制，是实现某个功能需要的原语操作和结构；策略，是某功能的具体实现；提供机制，而非策略，指的就是要给用户充分的自主可调配性。


越扯越远了，反正有源文件，可以make html之前自己改动。

最后，我准备喊一声“Grant Sanderson牛逼！3b1b牛逼!”。

然后，群友果然牛逼的大神不少，已经在整了 `manim-kindergarten-manim_sandbox <https://github.com/manim-kindergarten/manim_sandbox>`_  。

于是我已搜索，我发现，很多人在整这事儿了，Elteoremadebeethoven果然是大佬，  `Elteoremadebeethoven-MyAnimations <https://github.com/Elteoremadebeethoven/MyAnimations>`_   中，他已经写了很多的工具类，而且都有效果gif+markdown说明文件，很强很规范，超级牛逼！

Copyright - This document has been placed in the public domain.








