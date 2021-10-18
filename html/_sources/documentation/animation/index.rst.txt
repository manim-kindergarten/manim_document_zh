动画部分 animation
==================

.. admonition:: 声明

   这一部分有些翻译自elteoremadebeethoven的 `manim_3feb_docs <https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/animation.html>`_ 

   还有一部分是鹤翔万里原创编写的（这一部分未标明的页均为鹤翔万里编写）


.. toctree::
   :maxdepth: 2
   :caption: 目录

   creation
   fading
   growing
   indication
   movement
   numbers
   rotation
   transform
   transform_matching_parts
   update
   composition
   specialized

动画基类Animation
-------------------

.. autoclass:: manimlib.animation.animation.Animation

通用参数：

run_time
^^^^^^^^^^

表示一个动画运行的总时间（单位为秒）

rate_func
^^^^^^^^^^

一个动画运行的速率参数，是一个定义域为[0,1]的函数，自带的如下

.. image:: https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/image/rate_functions.png

效果如下：

.. raw:: html

    <video class="manim-video" controls loop autoplay src="https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/RateFunctions.mp4"></video>

.. raw:: html

    <video class="manim-video" controls loop autoplay src="https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/mk/RateFunctions2.mp4"></video>


lag_ratio
^^^^^^^^^^^

对于每个子物体执行动画，两个子物体之间延迟的半分比(0~1之间)，默认为0，即对所有子物体同时执行动画
