贡献
============

接受你做出任何贡献 :)

- **对manim源代码做出贡献**：

请fork到自己的repository并做出更改后，提出一个pull request，并按照模版中的指导填写好更改的动机等。
之后Grant会详细的检查你的pull request（这通常会花费一段时间，请耐心等待）

- **对文档做出贡献**：

同样提出pull request，并写好主要更改的内容。

- **如果你发现了代码中的bug但并不知道如何改正**：

请提出一个issue，并根据模板填写好发现的问题以及你的运行环境等。
（但请注意，如果你认为这个问题只是你自己配置的问题，而不是源码的问题，
更推荐你在discussion中一个 `Q&A <https://github.com/3b1b/manim/discussions/categories/q-a>`_）

- **欢迎你分享自己利用manim制作的内容**：

发布到discussion页面的 `show and tell分类 <https://github.com/3b1b/manim/discussions/categories/show-and-tell>`_ 中。

- **也欢迎你分享自己的一些建议和想法**：

发布到discussion页面的 `ideas分类 <https://github.com/3b1b/manim/discussions/categories/ideas>`_ 中。


如何构建本文档
-------------------------

- clone 3b1b/manim存储库

.. code-block:: sh

    git clone https://github.com/3b1b/manim.git
    # 或者你自己fork的repo
    # git clone https://github.com/<your user name>/manim.git
    cd manim

- 安装python包依赖

.. code-block:: sh

    pip install -r docs/requirements.txt

- 进入 ``docs/`` 文件夹并构建

.. code-block:: sh

    cd docs/
    make html

- 输出文档位于 ``docs/build/html/`` 中