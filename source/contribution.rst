贡献规则及编写指南
=====================

如果你想要为这个文档做出贡献，可以向 `这个repo <https://github.com/manim-kindergarten/manim_document_zh>`__ 提出Pull Request，我们在review了之后会merge，
并且自动构建并发布到这个网站上。

这里是一些规范和指南

首先，文档需要使用 ``reStructuredText`` 语言来编写，具体语法见 `Sphinx文档 <https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html>`__

目前未完成的部分见 `这个repo的project <https://github.com/manim-kindergarten/manim_document_zh/projects/1>`__

目录结构规范
------------

- 如果是一整个系列的内容，请新建一个文件夹，并且包含 ``index.rst`` 和其他各页的源文件，并写好目录如下::

    .. toctree::
        :maxdepth: 2
        :caption: 目录

        ...
        ...


- 如果是单个页面，请直接在 ``source`` 文件夹中新建一个 ``rst`` 文件，并改好 ``source/index.rst`` 中的目录结构

- 如果为某个系列补充页面，请将文件新建在对应的文件夹中，并改好其对应的 ``index`` 中的目录

页面内部规范
------------

- 目前的目录结构是根据 ``manimlib`` 中文件夹结构排列好的，所以请根据添加内容在 ``manimlib`` 中的位置添加在对应页面中

- 每个页面中每个类需要先使用二级标题，然后再使用 ``.. autoclass:: manimlib.<...>`` 自动生成类名和文档字符串

    - 如果该类中的方法比较重要需要文档字符串，使用::

        .. autoclass:: manimlib.<...>
            :members:

- 每个类需要包含明显示例和对应代码（视频或图片均可）

    - 视频放在 ``source/assets/mk`` 中，使用下面代码引用（需要注意文件所处的层次）::

        .. raw:: html

            <video width="560" height="315" controls>
                <source src="../_static/mk/视频名.mp4" type="video/mp4">
            </video>

    - 图片放在 ``source/assets/image`` 中，使用下面代码引用（需要注意文件所处的层次）::

        .. image:: ../assets/image/Text/image1.png

    - 代码使用（注意缩进使用4个空格，而不是Tab制表符）::
    
        .. code:: python

           class ...(Scene):
               def construct(self):
                   ...
    
    - 示例和代码的类名统一为 ``<当前要示例的类名>Example`` ，并且将代码放在 ``example.py`` 中

以上均可以通过点击 ``animation`` 相关页面及 ``mobject`` 中完成的页面右上角查看源代码来了解

关于文档字符串
---------------

| 这个文档用于生成文档字符串的 ``manimlib`` 在当前repo的 `manim分支下 <https://github.com/manim-kindergarten/manim_document_zh/tree/manim>`__
| 注意文档字符串也需要使用 ``reStructuredText`` 语法编写，并符合 `PEP257 <https://www.python.org/dev/peps/pep-0257/>`__ 中规范

如果所添加的内容需要更改文档字符串，请修改manim分支后另外提交pr
