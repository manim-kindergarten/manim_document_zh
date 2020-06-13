Linux
=====

.. admonition:: 声明

    这一页是EulerTour写的教程,我只是翻译+学习笔记

Linux安装没太多坑，Windows也可以使用WSL,Docker等利用Linux环境

Ubuntu
------

安装系统依赖库::

    # apt install sox ffmpeg libcairo2 libcairo2-dev

安装LaTeX发行版(TeXLive-full)::

    # apt install texlive-full

通过pypi安装manimlib（不推荐）::

    # pip3 install manimlib

或者通过GitHub安装环境（推荐）::

    $ git clone https://github.com/3b1b/manim
    $ cd manim
    $ python3 -m venv ./
    $ source bin/activate
    $ pip3 install -r requirement.txt

若要在虚拟环境中使用manim，您需要通过执行 ``source bin/activate`` 来激活环境，若要退出，请使用 ``deactivate`` 命令。

.. note:: pypi上的manimlib不经常更新，而且GitHub存储库还包括用于生成3b1b视频的项目文件。由于api的更改，一些旧项目可能无法正常工作。


.. note:: 所需要的LaTeX宏包由 ``manimlib/tex_template.tex`` 决定
          安装 ``texlive-full`` 是最保险的，但是下载的文件很大
          如果你想要只安装manim需要的宏包，使用下面的替换 ``texlive-full`` ::

            texlive texlive-latex-extra texlive-fonts-extra
            texlive-latex-recommended texlive-science texlive-fonts-extra tipa

Arch Linux
----------
安装系统依赖库::

    # pacman -S cairo ffmpeg opencv sox

安装LaTeX发行版::

    # pacman -S texlive-most

或者安装 python-manimlib_:sup:`AUR` 包::

    $ git clone https://aur.archlinux.org/python-manimlib.git
    $ cd python-manimlib
    $ makepkg -si

你可以使用AUR助手，例如 yay_:sup:`AUR`::

    $ yay -S python-manimlib

.. _python-manimlib: https://aur.archlinux.org/packages/python-manimlib/
.. _yay: https://aur.archlinux.org/packages/yay/
