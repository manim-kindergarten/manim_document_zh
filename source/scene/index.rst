场景部分scene(TODO)
======================

| :class:`~manimlib.scene.scene.Scene` 是基础的场景类，所有需要渲染出动画的场景都必须以它为超类
| ``manimlib/scene`` 中还有很多 :class:`~manimlib.scene.scene.Scene` 的子类，用于实现更多功能，支持不同相机

:class:`~manimlib.scene.scene_file_writer.SceneFileWriter` 是在任何 ``Scene`` 中都需要调用的，用这个类来实现写入视频片段文件，并在渲染结束后合并为完整视频

.. toctree::
   :maxdepth: 2
   :caption: 目录

   scene
   scene_file_writer
   moving_camera_scene
   zoomed_scene
   graph_scene
   three_d_scene
   reconfigurable_scene
   vector_space_scene
   sample_space_scene
   scene_from_video
