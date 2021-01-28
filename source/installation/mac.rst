Mac
===

.. admonition:: 声明

    这一页为Auxence原创编写


安装教程推荐
--------------------

指南的实际操作展示可以见 `视频 <https://www.bilibili.com/video/BV1W4411Z7Zt?p=2>`_。

安装步骤指南
--------------------

1. 安装Homebrew

   类似于Windows和Linux，macOS用来安装系统依赖项的方式就是Homebrew。
   Homebrew下载可以通过打开“终端”app，在终端中输入：
   
   .. code-block:: sh
       
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   按下回车，输入电脑的密码后再按一次回车即可。
   
   .. tip::

      如果因为网络原因下载不成功或者下载的速度太慢的话可以输入：
      
      .. code-block:: sh
      
          cd "$(brew --repo)"
          git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
      
          cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
          git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
      
      使用中科大的镜像替换brew.git和homebrew-core.git

2. 安装MacTeX

   MaxTeX是LaTeX的macOS版本，适用于macOS的文字排版等功能的使用。
   
   可以通过链接 https://mirrors.tuna.tsinghua.edu.cn/ctan/systems/mac/mactex/MacTeX.pkg 下载
   （推荐后台下载不浪费时间，下载完毕后双击安装即可）

3. 安装Python3

   macOS的系统中自带Python2的环境，但是manim使用的环境为Python3，所以需要下载安装Python3（不同的处理器选择对应的安装包）

   - `Python3.8.6 <https://www.python.org/ftp/python/3.8.6/python-3.8.6-macosx10.9.pkg>`_
   - `Python3.8.7 <https://www.python.org/ftp/python/3.8.7/python-3.8.7-macosx10.9.pkg>`_
   - `Python3.9.1（Intel版本） <https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg>`_
   - `Python3.9.1（Apple Silicon M1版本） <https://www.python.org/ftp/python/3.9.1/python-3.9.1-macos11.0.pkg>`_

4. 安装pip

   同样打开终端应用，输入：
   
   .. code-block:: sh
       
       Brew install curl

   然后创建一个存放manim文件的文件夹并进入：

   .. code-block:: sh

       mkdir ManimInstall
       cd ManimInstall

   再下载并安装pip：
   
   .. code-block:: sh
   
       curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
       python3 get-pip.py

5. 下载系统依赖

   安装FFmpeg、sox、cairo、py2cairo、pkg-config，在终端分别输入：
   
   .. code-block:: sh
   
       brew install ffmpeg
       brew install sox
       brew install cairo
       brew install py2cairo
       brew install pkg-config

6. 下载manim主文件

   Manim主文件夹是manim运行的基础，下载方式可以通过文件链接或者GitHub的manim主页下载
   https://github.com/3b1b/manim/archive/master.zip

   下载之后解压缩到刚才创建的位置（可以在文件夹中双指单击页面上方中间的图标，选择房子图标的用户文件夹，找到刚才的位置），
   并且找到 ``requirements.txt``，删除最后的 ``; sys_platform == 'win32'``

   然后继续在刚才的（位于新安装目录的）终端里分别运行：
   
   .. code-block:: sh

       python3 -m pip install -r requirements.txt
       python3 -m pip install pyreadline
       python3 -m pip install pydub

7. 安装完成

   至此我们已经全部安装了manim必需的部件，接下来可以在终端中输入如下命令测试结果：
   
   .. code-block:: sh

       python3 -m manim example_scenes.py OpeningManimExample -pm
   
   其中，所有的输出文件，包括照片、视频等都会保存在manim文件夹下的media文件夹中。
