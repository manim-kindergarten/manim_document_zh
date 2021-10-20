贡献
============

接受你做出任何贡献 :)

- **对 manim 源代码做出贡献**：

请将 `3b1b/manim <https://github.com/3b1b/manim>`_ fork 到自己的 repository 并做出更改后，提出一个 pull request，并按照模版中的指导填写好更改的动机等。
之后Grant或协作者会详细的检查你的 pull request（这通常会花费一段时间，请耐心等待）然后考虑合并。

- **对文档做出贡献**：

  * 英文文档：同样 fork 3b1b/manim，然后在 ``docs/`` 文件夹中进行更改，再交 pull request
  * 中文文档：请 fork `manim-kindergarten/manim <https://github.com/manim-kindergarten/manim>`_，在其中 ``docs/`` 文件夹中进行更改，然后向 manim-kindergarten/manim 中交 pull request

对于其中引用的图片/视频素材，可以放到 ``docs/source/_static/`` 文件夹中，并在文档中正确引用。

- **如果你发现了代码中的 bug 但并不知道如何改正**：

请提出一个 issue，并根据模板填写好发现的问题以及你的运行环境等。
（但请注意，如果你认为这个问题只是你自己配置的问题，而不是源码的问题，
更推荐你在 discussion 中开启一个 `Q&A <https://github.com/3b1b/manim/discussions/categories/q-a>`_）

- **欢迎你分享自己利用 manim 制作的内容**：

发布到 discussion 页面的 `show and tell分类 <https://github.com/3b1b/manim/discussions/categories/show-and-tell>`_ 中。

- **也欢迎你分享自己的一些建议和想法**：

发布到 discussion 页面的 `ideas分类 <https://github.com/3b1b/manim/discussions/categories/ideas>`_ 中。


如何构建本文档
-------------------------

- 克隆 `manim-kindergarten/manim <https://github.com/manim-kindergarten/manim>`_ 存储库

.. code-block:: sh

    git clone https://github.com/manim-kindergarten/manim.git
    # 或者你自己 fork 的 repo
    # git clone https://github.com/<your user name>/manim.git
    cd manim

- 安装 python 包依赖

.. code-block:: sh

    pip install -r docs/requirements.txt

- 进入 ``docs/`` 文件夹并构建

.. code-block:: sh

    cd docs/
    make html

- 输出文档位于 ``docs/build/html/`` 中