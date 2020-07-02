Windows
======================


.. admonition:: 声明

  这一页是一些中文manim安装教程的推荐

安装教程推荐
--------------------

知乎用户李狗嗨的安装教程 manimInstallation_ 写的很明白

同时推荐一视数学卷毛杨的两个教程 https://www.bilibili.com/video/av38126904 https://www.bilibili.com/read/cv4139851，
pdcxs的安装实况 https://www.bilibili.com/video/BV14i4y1G7Yr

有什么安装上的问题可以在 `manim-kindergarten的任意repo <https://github.com/manim-kindergarten>`_ 中提出issue，或者B站私信manim相关up主，或者加入QQ群

简要安装指南
---------------
不要把manim的安装看得很复杂，其本质上就是安装几个依赖的软件

- **python** ，这个是必须的，版本应该在 ``3.6`` 以上（需要支持 ``f-string`` ）。推荐直接安装 ``anaconda`` 方便管理环境
- 一些python的 **依赖模块** ，在 ``requirements.txt`` 中

  1. 直接使用pip安装，执行：``pip install -r requirements.txt`` ，注意pip的版本应该和python相匹配（或者使用 ``python -m pip`` 代替pip）
  2. 使用anaconda，执行：``conda env create -f environment.yml`` 和 ``pip install pyreadline`` 即可
  3. 附：pip临时换源： ``-i https://pypi.tuna.tsinghua.edu.cn/simple``
  4. 附：`pycairo的whl文件下载地址 <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo>`__ ，注意匹配python与系统版本

- **ffmpeg** ，用于处理生成视频，注意，不要使用anaconda或pip安装ffmpeg，要手动单独安装
- **LaTeX** ，用于生成文字和公式，推荐直接安装TeXLive-full版，详见官网
- **sox** ，可以不安装，只是用于播放渲染完成/失败的提示音（一般不用）

将这些依赖都解决后，manim就可以使用了

VSCode调试manim
-----------------

**假设你的VSCode打开的文件夹恰好是manim的官方库clone下来的根目录，即manim.py所在目录。**

1. 安装好python的官方扩展
2. 编辑lanuch.json为如下

.. code-block:: json

   {
       // 使用 IntelliSense 了解相关属性。 
       // 悬停以查看现有属性的描述。
       // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Run manim", // 渲染manim的480p15预览
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}\\manim.py", // manim.py的路径
               "console": "integratedTerminal",           // 使用vscode的终端进行调试
               "args": [
                   "${file}",                   // 当前文件
                   "-pl",                       // 480p15预览参数
                   "--media_dir",               // 输出位置
                   "${workspaceFolder}\\export" // 这里定义输出位置
               ]
           },
           {
               "name": "Render manim",                   // 渲染1080p60的manim动画
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}\\manim.py",// manim.py的路径
               "console": "integratedTerminal",          // 使用vscode的终端进行调试
               "args": [
                   "${file}",                   // 当前文件
                   "--high_quality",            // 1080p60输出参数
                   "-p",                        // 预览参数
                   "--media_dir",               // 输出位置
                   "${workspaceFolder}\\export" // 这里定义输出位置
               ]
           }
       ]
   }

3. 设置好之后就可以自由使用调试功能进行断点调试等操作了。


.. _manimInstallation: https://zhuanlan.zhihu.com/p/70243739
