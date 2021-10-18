场景部分 scene
======================

.. admonition:: 声明

    该部分由 widcardw 整合，由于编者能力和时间有限，所以会有诸多不完善之处。在这里欢迎 **了解视频流、虚拟相机等方面的同学** 加入我们，一起完善文档。 

| :class:`~manimlib.scene.scene.Scene` 是基础的场景类，所有需要渲染出动画的场景都必须以它为超类

:class:`~manimlib.scene.scene_file_writer.SceneFileWriter` 是在任何 ``Scene`` 中都需要调用的，用这个类来实现写入视频片段文件，并在渲染结束后合并为完整视频

.. toctree::
   :maxdepth: 2
   :caption: 目录

   scene
   scene_file_writer
   three_d_scene
   sample_space_scene
   vector_space_scene