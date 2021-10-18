CONFIG_ops
==========

``manimlib/utils/config_ops.py`` 这个文件中主要实现了处理CONFIG字典和类的属性有关的函数

-----

.. autofunction:: manimlib.utils.config_ops.get_all_descendent_classes

获取类 Class 的全部子类

-----

.. autofunction:: manimlib.utils.config_ops.filtered_locals

将 caller_locals 字典中去掉 ``self, kwargs`` 两个键值对

-----

.. autofunction:: manimlib.utils.config_ops.digest_config

获取当前类和所有父类的 CONFIG 字典，转换为属性（优先级已经处理好）

- 若要将当前所有局部变量也转化为属性，使用 ``digest_config(self, kwargs, locals())``

-----

.. autofunction:: manimlib.utils.config_ops.merge_dicts_recursively

| 递归合并字典
| 创建一个字典，其键集是所有输入字典的并集，每个键的值都基于列表中带有该键的第一个字典
| 当值为字典时，将递归应用

-----

.. autofunction:: manimlib.utils.config_ops.soft_dict_update

合并字典，仅当 d1 没有该键时，才将 d2 的键值对添加到d1中

-----

.. autofunction:: manimlib.utils.config_ops.digest_locals

把当前局部变量设为属性
