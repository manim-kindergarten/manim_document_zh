Mac
===

.. admonition:: 声明

    这一页是EulerTour写的教程,我只是翻译+学习笔记，github早就有很多教程，但是为了方便查询使用，我才整合这么一份文档。




The simplest way to install the system dependencies on Mac OS X is with Homebrew.
Mac come preinstalled with python2, but to use manim, python3 is required.Mac(类unix)安装没太多坑，windows也可以使用WSL,Docker。

1. Install python3 https://docs.python.org/3/using/mac.html
2. Install Cairo: ``brew install cairo``
3. Install Sox: ``brew install sox``
4. Install ffmpeg: ``brew install ffmpeg``
5. Install latex (MacTeX): ``brew cask install mactex``
6. Install manimlib ``pip install manimlib`` (or ``pip install --user manimlib`` to just yourself)
