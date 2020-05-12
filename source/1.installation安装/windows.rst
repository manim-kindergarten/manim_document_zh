Windows安装Manim
======================

Install System Libraries
---------------------------------------

.. admonition:: 声明

  这一页是EulerTour写的教程,我只是翻译+学习笔记，github早就有很多教程，但是为了方便查询使用，我才整合这么一份文档。

下面是一些需要安装的软件，知乎用户李狗嗨的安装教程 manimInstallation_ 已经写很明白,Q群友推荐一视数学卷毛杨的两个教程https://www.bilibili.com/video/av38126904 https://www.bilibili.com/read/cv4139851


Make sure you have *Python 3* for Windows installed first:

https://www.python.org/downloads/windows/

Install ffmpeg:

https://ffmpeg.org/download.html#build-windows

Install sox:

http://sox.sourceforge.net/Main/HomePage

Install a latex distribution. On Windows MikTex is commonly used:

https://miktex.org/howto/install-miktex

Path configuration
------------------

建议看知乎相关安装教程，B站专栏也有很多，新版本坑越来越少，nice!
To invoke commandline without supplying path to the binary
the PATH environment配置环境变量 needs to be configured. Below are template examples, please change
the path according to your username and specific python version. Assuming all the
softwares are installed with no alteration to the installation paths::

  C:\Users\$username\AppData\local\Programs\Python\Python$version\
  C:\Users\$username\AppData\local\Programs\Python\Python$version\Scripts\
  C:\MikTex\miktex\bin\x64\
  C:\ffmpeg\bin\

The path entries should be separated by semicolon.

Installing python packages and manim需要的库
-------------------------------------------------------------------------

Make sure you can start pip using ``pip`` in your commandline. Then do
``pip install pyreadline`` for the ``readline`` package.

Grab the pycairo wheel binary ``pycairo‑1.18.0‑cp37‑cp37m‑win32.whl`` from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo
and install it via ``python -m pip install C:\absolute\path\to\the\whl\file``

clone the manim repository if you have git ``git clone https://github.com/3b1b/manim`` or download the zip file from
the repository page with ``Clone or download`` button and unzip it.

Open the commandline within the manim directory with ``Shift + Right click`` on an empty space in the folder and select ``open command window here``

Install manim python dependencies with ``pip install -r requirements.txt``

Test the installation测试安装
------------------------------------

Type in ``python -m manim -h`` and if nothing went wrong during the installation process you should see the help text.

Use ``python -m manim example_scenes.py SquareToCircle -pl`` to render the example scene and the file should play after rendering. The movie file should be
in ``media/videos/example_scenes/480p15``

By the way总想对Win用户说点啥
------------------------------
Visual Studio Code真心好用，ctrl+shift+p打开命令,Preferences:Open Keyboard Shortcuts搜索进入keybings.json,添加代码：

::

     {
       "key": "ctrl+shift+c ctrl+shift+d",
       "command": "terminalHere.create"
     }

ctrl+shift+c， ctrl+shift+d就能快速打开当前文件目录所在的终端（相当于文件浏览器地址栏输入cmd回车），一般默认cmd也能设置成powershell,wsl等你想要的终端，好处在于不用cd路径，直接快捷键打开路径下的终端。

如果使用miniConda的话，想要cmd终端使用Conda的CommandPrompt，需要先随便一个路径下新建MyBatFilesPath文件夹（然后添加到环境变量path,好处是很多有用的自定义bat脚本全都放这儿，省心），新建txt重命名 ``hereConda.bat``,文本内容如下：

.. code-block:: bash

  %windir%\System32\cmd.exe "/K" C:\ProgramData\Miniconda3\Scripts\activate.bat C:\ProgramData\Miniconda3


然后文件浏览器任何manim文件的目录下，地址栏输入hereConda回车，就能打开当前目录Conda的CommandPrompt，输入manim相关命令（我最常使用的方式）。

最简单双击打开当前目录的Anaconda Powershell Prompt (Miniconda3)直接运行manim方法是：复制Anaconda Powershell Prompt (Miniconda3)到manim目录，右键属性：

.. code-block:: bash

  %windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\Miniconda3' ;"

.. code-block:: bash

  %windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\Miniconda3' ;cd 'C:\Users\admin\Documents\Tridu33\(Py\!3b1b-video';"


ps:有一点我没搞懂，visual studio code不能直接使用manim命令，不知道原因是什么，我已经设置了管理员权限，文件夹权限也取消仅读，因为影响不大就没继续折腾，其实我还是很想知道的。ipython，jupyter,python使用Tensorflow等等只要在conda命令能用的都能用，就是执行manim.py的命令会跳转编辑，即manim相关命令vsc的终端中不能直接使用。



我一般在Visual Studio Code打开终端后输入hereConda，就能使用Conda的相关命令，如果是使用Jupyter的小伙伴，可以试试这个hereJupyter.bat代码：

.. code-block:: bash

  %windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\Miniconda3' ;jupyter notebook"


Jupyter中，!+命令 执行conda中命令，比如：

.. code:: ipython3

  %lsmagic


.. parsed-literal::

    Available line magics:
    %alias  %alias_magic  %autoawait  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %cls  %colors  %conda  %config  %connect_info  %copy  %ddir  %debug  %dhist  %dirs  %doctest_mode  %echo  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %macro  %magic  %matplotlib  %mkdir  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %ren  %rep  %rerun  %reset  %reset_selective  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
    
    Available cell magics:
    %%!  %%HTML  %%SVG  %%bash  %%capture  %%cmd  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
    
    Automagic is ON, % prefix IS NOT needed for line magics.



.. code:: ipython3

    %clear
    %cls
    !python -m manim example_scenes.py SquareToCircle -pl


就会自动播放预览低分辨率的视频，如果想内嵌进去ipython需要安装写东西，但是windows坑不少，我放弃了安装那个视频内嵌ipynb的功能，文件读写就挺好，vsCode可以用wsl，bash等，但是每次切换，我嫌麻烦就没继续用。



.. _manimInstallation: https://zhuanlan.zhihu.com/p/70243739
