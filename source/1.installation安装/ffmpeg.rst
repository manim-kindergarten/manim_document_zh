
ffmpeg
================

.. code-block:: bash
   :lineno-start: 1

   #视频合并
   ffmpeg -i scene1.mp4 -c copy scene1.ts
   ffmpeg -i scene2.mp4 -c copy scene2.ts
   ffmpeg -i "concat:scene1.ts|scene2.ts" -c copy merge.mp4

   #mp3合并
   ffmpeg -i "concat:bgm1.mp3|bgm2.mp3" -acodec copy merge.mp3

   #修改速度
   ffmpeg -i iname.mp4 -an -filter:v "setpts=0.5*PTS" oname.mp4

   #增加bgm
   ffmpeg -i iname.mp4 -i bgm.mp3 -c copy oname.mp4

   #截取bgm（-ss开始时间，-t持续时间）
   ffmpeg -i bgm.mp3 -vn -acodec copy -ss 00:00:10 -t 00:00:20 output.mp3

   #截取mp4
   ffmpeg -ss 00:00:10 -t 00:00:20 -i iname.mp4 -codec copy oname.mp4

   #mp4转gif
   ffmpeg -i input.mp4 -b:v 2048k output.gif

   #mp4加png水印
   ffmpeg -i input.mp4 -i shuiyin.png -filter_complex "overlay=0:0" output.mp4

ffmpeg文档

- 官方Wiki：http://trac.ffmpeg.org/wiki 
- 官方文档：https://ffmpeg.org/documentation.html
- 2018中文文档：http://itiit.cn/html/ffmpeg.html









