安装指南
============

Manim运行在Python 3.6或者更高版本上（推荐使用Python 3.8）

另外，不是特别推荐在 WSL 上安装 manimgl，因为 manimgl 在 **预览时** 不可避免地会调用 Pyglet Window 这个库，而这个库需要 GUI。不少用户为此花费大量的心血寻找解决方案，但真正解决的少之又少 qwq

所需的系统依赖有：

- `FFmpeg <https://ffmpeg.org/>`__
- `OpenGL <https://www.opengl.org//>`__ (包含在python包 ``PyOpenGL`` 中)
- `LaTeX <https://www.latex-project.org>`__ (可选，如果需要LaTeX则必需)
- `Pango <https://pango.org>`__ (只有Linux系统需要，可选，如果需要使用manim的 ``Text`` 则必需)

直接安装
----------

.. code-block:: sh

   # 通过pip安装manimgl
   pip install manimgl

   # 测试一下
   manimgl

如果你想要更改manimlib的源码并使用，或者使用最新版本，可以clone下这个存储库（不要下载zip）
然后进入文件夹中执行：

.. code-block:: sh

   # 安装
   pip install -e .

   # 测试
   manimgl example_scenes.py OpeningManimExample
   # 或
   manim-render example_scenes.py OpeningManimExample

如果你运行了上面这条命令，并且没有任何报错信息出现，那么你就已经安装好了manim所需的全部环境。

直接安装 (Windows)
--------------------

1. 安装 `FFmpeg <https://www.wikihow.com/Install-FFmpeg-on-Windows>`_, 并且保证它在 ``PATH`` 环境变量中
2. 安装一个LaTeX发行版，推荐 `TeXLive-full <http://tug.org/texlive/>`__
3. 安装剩余的python依赖包

.. code-block:: sh  

   git clone https://github.com/3b1b/manim.git
   cd manim  
   pip install -e . 
   manimgl example_scenes.py OpeningManimExample

使用Anaconda
---------------

- 同上安装FFmpeg和LaTeX
- 创建一个新的conda环境：

.. code-block:: sh
   
   git clone https://github.com/3b1b/manim.git
   cd manim 
   conda create -n manim python=3.8
   conda activate manim
   pip install -e .
