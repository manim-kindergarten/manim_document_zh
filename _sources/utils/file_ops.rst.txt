FILE_ops
==========

``manimlib/utils/file_ops.py`` 这个文件中主要实现了处理文件有关的函数

-----

.. autofunction:: manimlib.utils.file_ops.add_extension_if_not_present

如果file_name没有扩展名extension，则加上扩展名

-----

.. autofunction:: manimlib.utils.file_ops.guarantee_existence

返回path的绝对路径

-  若path不存在，则创建


-----

.. autofunction:: manimlib.utils.file_ops.seek_full_path_from_defaults

从默认值中查找完整路径，默认路径如下

1. 当前目录下file_name文件
2. default_dir下file_name文件和加上扩展名extensions的文件


-----

.. autofunction:: manimlib.utils.file_ops.get_sorted_integer_files

获取根据整数排序的文件(在partial_movie_files的合并中用到)

