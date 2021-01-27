Iterables
=========

``manimlib/utils/iterables.py`` 这个文件中主要实现了和列表字典处理有关的函数


-----

.. autofunction:: manimlib.utils.iterables.remove_list_redundancies

对列表l去重，保留重复元素最后一次出现

-----

.. autofunction:: manimlib.utils.iterables.list_update

从l1中删除l2中重复项，再与l2合并

-----

.. autofunction:: manimlib.utils.iterables.list_difference_update

返回两列表中不同的项的列表

-----

.. autofunction:: manimlib.utils.iterables.all_elements_are_instances

iterable列表中的所有元素是否都为Class类

-----

.. autofunction:: manimlib.utils.iterables.adjacent_n_tuples

objects的相邻n元组（返回zip）

-----

.. autofunction:: manimlib.utils.iterables.adjacent_pairs

objects相邻对

-----

.. autofunction:: manimlib.utils.iterables.batch_by_property

| 输入一个列表，返回一个元组列表（batch，prop）
| 这样一个批中的所有项在放入property_func时都具有相同的输出
| 并且将所有这些批链接在一起将得到原始列表（即保留顺序）

-----

.. autofunction:: manimlib.utils.iterables.tuplify

根据obj返回元组

-  若obj为str类型，返回(obj, )
-  尝试返回tuple(obj)
-  若报错，返回(obj, )

-----

.. autofunction:: manimlib.utils.iterables.stretch_array_to_length

将nparray扩展至length长度

-----

.. autofunction:: manimlib.utils.iterables.make_even

将iterable_1和iterable_2调成一样的长度，不足的伸缩调整

-----

.. autofunction:: manimlib.utils.iterables.make_even_by_cycling

将iterable_1和iterable_2调成一样的长度，不足的循环使用

-----

.. autofunction:: manimlib.utils.iterables.remove_nones

将sequence中的None去除掉，并返回

-----

.. autofunction:: manimlib.utils.iterables.concatenate_lists

串联列表list_of
