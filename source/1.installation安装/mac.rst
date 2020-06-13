Mac
===

.. admonition:: 声明

    这一页是EulerTour写的教程,我只是翻译+学习笔记


在Mac OS X上安装系统依赖项的最简单方法是使用 ``brew``

Mac预装了python2，但要使用manim必须安装python3

1. 安装python3 https://docs.python.org/3/using/mac.html
2. 安装cairo: ``brew install cairo``
3. 安装Sox: ``brew install sox``
4. 安装ffmpeg: ``brew install ffmpeg``
5. 安装LaTeX发行版 (MacTeX): ``brew cask install mactex``
6. 安装manimlib ``pip install manimlib`` (或者 ``pip install --user manimlib`` 只为你自己安装)，或者clone下来GitHub上的存储库并安装requirements.txt中的依赖包
