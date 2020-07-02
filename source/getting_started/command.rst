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
============================== ====== ===========================================================================================================================================================================


**示例** ：

.. code-block::

  python -m manim example_scenes.py SquareToCircle -ps

``-s`` 可以在images文件夹下看到保存的最后一张图片，比如在一个比较大的项目中，想看自己的某一张图画出来效果，可以使用 ``-s`` 导出最后一帧

.. code-block:: bash

   python -m manim example_scenes.py SquareToCircle -al

``-a`` 把文件中所有scene写成视频。

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -o <file_name>

输出 <file_name>.mp4

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -pl -c WHITE

.. code-block:: bash

  manim example_scenes.py SquareToCircle -pl -c '#FFFFFF' 

.. code-block:: bash

  manim example_scenes.py SquareToCircle -pl -c '#FFFFFF' 
  
白色背景


.. code-block:: bash
   
   self.play(ShowCreation(square))         #0
   self.play(Transform(square, circle))    #1
   self.play(FadeOut(square))              #2


SquareToCircle有3个animations渲染任务，可以：

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -pl -n 2 

这就能直接从第3个（0开始）animations渲染到最后。

.. code-block:: bash

  python -m manim example_scenes.py SquareToCircle -r 1080

获得 1920x1080 分辨率的视频。


**存为gif**

使用 ``python -m manim animation.py name_scene -im`` 渲染中等质量的gif文件，但是选项 ``-i`` 目前被取消了，依旧会生成mp4文件，可以按照常见问题中更改，或者使用 `MK版本的manim <https://github.com/manim-kindergarten/manim>`_

也可以使用ffmpeg手动转换

.. code-block:: bash

   ffmpeg -i SquareToCircle.mp4 SquareToCircle.gif
