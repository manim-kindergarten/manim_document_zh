SVG作图
===============

SVG作图,LaTeX也是转换为svg,svg真的很重要！我倒是想讲解生成调用机理（具体怎么调用，然后怎么使用svg利用ffmpeg等辅助软件生成视频）,奈何现在的我实力还不会(~_~，蒟蒻落泪(-…-"

还是先来看看用法吧。

群文件常见问题PDF中提到：

报错 Latex error converting to dvi 先把 manimlib/constants.py 中的 TEX_USE_CTEX 改成 True 再运行


报错 xelatex error converting to xdv 若为 Windows 系统，先把 manimlib/constants.py 的 MEDIA_DIR = "./media"
改成::

    MEDIA_DIR = os.path.join(os.getcwd(), "media")

再进行尝试 


来自群友Cigar666的svg教程,文件夹下还有很多svg可以试试。

.. literalinclude:: ../assets/svg/monsters/SVG_test.py
    :linenos:


.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/svg/monsters/Show_SVG_test.mp4" type="video/mp4">
    </video>



.. raw:: html

    <video width="560" height="315" controls>
        <source src="../_static/svg/monsters/Show_SVG.mp4" type="video/mp4">
    </video>















































































































