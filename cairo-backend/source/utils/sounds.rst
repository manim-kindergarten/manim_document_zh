Sounds
======

``manimlib/utils/sounds.py`` 这个文件中主要实现了和音频有关的函数


-----

.. autofunction:: manimlib.utils.sounds.play_chord

play和弦

-----

.. autofunction:: manimlib.utils.sounds.play_error_sound

播放编译失败声音

-----

.. autofunction:: manimlib.utils.sounds.play_finish_sound

播放编译成功声音

-----

.. autofunction:: manimlib.utils.sounds.get_full_sound_file_path

使用 ``seek_full_path_from_defaults`` 获取音频位置

-  默认文件夹\ ``assets/sounds/``
-  扩展名:\ ``[.wav, .mp3]``

-  **注意:** 播放编译成功/失败音频的方法

   - 在输入命令时加上 ``--sound`` 选项

     -  Linux系统安装sox后直接可以使用
     -  Windows系统需要下载sox-14-4-1安装包(新版可能会报错)，并将其中的sox.exe复制，重命名为play.exe，填好环境变量就可以使用了

