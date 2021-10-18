FILE_ops
==========

``manimlib/utils/file_ops.py`` 这个文件中主要实现了处理文件有关的函数

-----

.. autofunction:: manimlib.utils.file_ops.add_extension_if_not_present

如果 file_name 没有扩展名 extension，则加上扩展名

-----

.. autofunction:: manimlib.utils.file_ops.guarantee_existence

返回 path 的绝对路径

-  若 path 不存在，则创建


-----

.. autofunction:: manimlib.utils.file_ops.find_file

从默认值中查找完整路径，默认路径如下

1. 当前目录下 file_name 文件
2. default_dir 下 file_name 文件和加上扩展名 extensions 的文件


-----

.. autofunction:: manimlib.utils.file_ops.get_sorted_integer_files

获取根据整数排序的文件 (在 partial_movie_files 的合并中用到)

