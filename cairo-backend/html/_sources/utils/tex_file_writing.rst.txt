Tex_file_writing
================


``manimlib/utils/tex_file_writing.py`` 这个文件中主要包含了将tex字符串使用LaTeX编译成svg的函数


-----

.. autofunction:: manimlib.utils.tex_file_writing.tex_hash

返回将 ``expression`` 和 ``template_tex_file_body`` 合并后sha256后的哈希值

-----

.. autofunction:: manimlib.utils.tex_file_writing.tex_to_svg_file

| 将tex表达式转换为svg文件
| (先写入.tex文件，再编译为.dvi/.xdv文件，后转换为.svg文件)

-----

.. autofunction:: manimlib.utils.tex_file_writing.generate_tex_file

| 将 ``expression`` 写入tex文件，并返回tex文件
| 使用 ``expression`` 替换掉 ``template_tex_file_body`` 文件中的 ``TEX_TEXT_TO_REPLACE``
| tex文件名为hash值

-----

.. autofunction:: manimlib.utils.tex_file_writing.tex_to_dvi

将tex文件编译为dvi/xdv文件，并返回dvi/xdv文件

-  若 ``TEX_USE_CTEX=False`` ，则使用latex将tex编译为dvi
-  若 ``TEX_USE_CTEX=True`` ，则使用xelatex将tex编译为xdv


-----

.. autofunction:: manimlib.utils.tex_file_writing.dvi_to_svg

使用dvisvgm将dvi/xdv文件转换为svg文件，并返回svg文件


