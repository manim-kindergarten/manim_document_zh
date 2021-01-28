安装指南
============

Manim运行在Python 3.8上.

所需的系统依赖有：

- `FFmpeg <https://ffmpeg.org/>`__
- `OpenGL <https://www.opengl.org//>`__ (包含在python包 ``PyOpenGL`` 中)
- `LaTeX <https://www.latex-project.org>`__ (可选，如果需要LaTeX则必需)
- `cairo <https://www.cairographics.org/>`_ (包含在python包 ``pycairo`` 中. 可选，如果需要使用manim的 ``Text`` 则必需)

直接安装
----------

clone这个存储库，然后进入文件夹中执行：

.. code-block:: sh

   # 安装python依赖包
   pip install -r requirements.txt

   # 尝试运行
   python -m manim example_scenes.py OpeningManimExample

如果你运行了上面这条命令，并且没有任何报错信息出现，那么你就已经安装好了manim所需的全部环境。

直接安装 (Windows)
--------------------

1. 安装`FFmpeg <https://www.wikihow.com/Install-FFmpeg-on-Windows>`_, 并且保证它在 ``PATH`` 环境变量中
2. 安装一个LaTeX发行版，推荐 `TeXLive-full <http://tug.org/texlive/>`__
3. 安装剩余的python依赖包

.. code-block:: sh  

   git clone https://github.com/3b1b/manim.git
   cd manim  
   pip install -r requirements.txt  
   python manim.py example_scenes.py OpeningManimExample

使用Anaconda
---------------

- 同上安装FFmpeg和LaTeX
- 创建一个新的conda环境：

.. code-block:: sh
   
   git clone https://github.com/3b1b/manim.git
   cd manim 
   conda env create -f environment.yml

使用virtualenv和virtualenvwrapper
--------------------------------------

在安装了 ``virtualenv`` 和 ``virtualenvwrapper`` 后，执行：

.. code-block:: sh

   git clone https://github.com/3b1b/manim.git
   mkvirtualenv -a manim -r requirements.txt manim
   python -m manim example_scenes.py OpeningManimExample