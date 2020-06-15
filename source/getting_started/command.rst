运行命令
========

.. admonition:: 声明
   这一页来自鹤翔万里在manim_sandbox中的wiki页

   后部分为GZTime添加

在命令行运行manim
-----------------

使用manim运行一个动画，需要进入到与manim.py同级的目录中，并向cmd中输入如下格式的命令

.. code:: shell

   python manim.py <code>.py <Scene(s)> <options>

-  ``<code>.py``
   为你写的python文件，需要与manim.py同级，否则需要使用绝对路径，或写准相对路径
-  ``<Scene(s)>``
   这里填你想要渲染的场景，或者一些场景。如果没有写或者写错，若文件中只有一个Scene，会直接渲染这个类，否则会列出所有让你选择
-  ``<options>`` 传入的选项

**以下是所有manim的选项**：

============================== ====== ===========================================================================================================================================================================
选项                           简写   含义
============================== ====== ===========================================================================================================================================================================
``--preview``                  ``-p`` 渲染之后打开预览
``--write_to_movie``           ``-w`` 使用最高质量渲染(默认1440P60)
``--save_last_frame``          ``-s`` 保存最后一帧图片
``--low_quality``              ``-l`` 使用低质量渲染(默认480P15)
``--medium_quality``           ``-m`` 使用中等质量渲染(默认720P30)
``--high_quality``                    使用高质量渲染(默认1080P60)
``--save_pngs``                ``-g`` 导出每一帧
``--save_as_gif``              ``-i`` 保存为gif(需要按照\ `常见问题 <https://github.com/manim-kindergarten/manim_sandbox/blob/master/documents/manim%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98v2.1.pdf>`__\ 中修改源码)
``--show_file_in_finder``      ``-f`` 渲染完打开文件夹
``--transparent``              ``-t`` 渲染alpha通道，视频为mov格式
``--quiet``                    ``-q``
``--write_all``                ``-a`` 渲染文件中的所有场景
``--file_name``                ``-o`` 视频文件保存的名字，后面接文件名
``-start_at_animation_number`` ``-n`` 后面接两个数(逗号隔开)仅渲染一部分动画
``--resolution``               ``-r`` 渲染视频的画面大小，给出height,width
``--color``                    ``-c`` 背景颜色，后面接颜色(constants中定义或字符串“#FFFFFF”这样)
``--sound``                           运行结束后播放成功或者失败的声音
``--leave_progress_bars``             保持进度条留在终端中
``--video_dir``                       存放视频的目录
``--video_output_dir``                保存视频的目录
``--tex_dir``                         放TeX文件的目录
``--livestream``                      流模式
``--to-twitch``                      
``--with-key``                       
============================== ====== ===========================================================================================================================================================================

使用VSCode的调试功能调试manim
---------------------------------

**假设你的VSCode打开的文件夹恰好是manim的官方库clone下来的根目录，即manim.py所在目录。**

1. 安装好python的官方扩展
2. 编辑lanuch.json为如下

.. code:: text

   {
       // 使用 IntelliSense 了解相关属性。 
       // 悬停以查看现有属性的描述。
       // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Run manim", //渲染manim的480p15预览
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}\\manim.py", //manim.py的路径
               "console": "integratedTerminal",  //使用vscode的终端进行调试
               "args": [
                   "${file}",  //当前文件
                   "-pl",  //480p15预览参数
                   "--media_dir", //输出位置
                   "${workspaceFolder}\\export" //这里定义输出位置
               ]
           },
           {
               "name": "Render manim",//渲染1080p60的manim动画
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}\\manim.py",//manim.py的路径
               "console": "integratedTerminal",//使用vscode的终端进行调试
               "args": [
                   "${file}",//当前文件
                   "--high_quality",//1080p60输出参数
                   "-p",//预览参数
                   "--media_dir",//输出位置
                   "${workspaceFolder}\\export"//这里定义输出位置
               ]
           }
       ]
   }

3. 设置好之后就可以自由使用调试功能进行断点调试等操作了。

