Iterables
=========

``manimlib/utils/iterables.py`` 这个文件中主要实现了和列表字典处理有关的函数


-----

.. autofunction:: manimlib.utils.iterables.remove_list_redundancies

对列表 l 去重，保留重复元素最后一次出现

-----

.. autofunction:: manimlib.utils.iterables.list_update

从 l1 中删除 l2 中重复项，再与 l2 合并

-----

.. autofunction:: manimlib.utils.iterables.list_difference_update

返回两列表中不同的项的列表

-----

.. autofunction:: manimlib.utils.iterables.adjacent_n_tuples

objects 的相邻 n 元组（返回zip）

-----

.. autofunction:: manimlib.utils.iterables.adjacent_pairs

objects 相邻对

-----

.. autofunction:: manimlib.utils.iterables.batch_by_property

| 输入一个列表，返回一个元组列表（batch，prop）
| 这样一个批中的所有项在放入 property_func 时都具有相同的输出
| 并且将所有这些批链接在一起将得到原始列表（即保留顺序）

-----

.. autofunction:: manimlib.utils.iterables.listify

根据 obj 返回列表

-  若 obj 为 str 类型，返回 [obj]
-  尝试返回 list(obj)
-  若报错，返回 [obj]

-----

.. autofunction:: manimlib.utils.iterables.resize_array

重置数组长度

- 若长度变短，则截断为前半部分元素
- 若长度不变，则直接返回
- 若长度变长，则循环拷贝

-----

.. autofunction:: manimlib.utils.iterables.resize_preserving_order

重置数组长度，但保留原有的序列

- 若长度为 0，则返回 0 数组
- 若长度变短，则截断为前半部分元素
- 若长度不变，则直接返回
- 若长度变长，则类似 [1,2,3] 变为 [1,1,2,2,3,3]

-----

.. autofunction:: manimlib.utils.iterables.resize_with_interpolation

重置数组长度，并对中间元素进行线性插值，插值起止点分别为数组的首尾元素

-----

.. autofunction:: manimlib.utils.iterables.make_even

将 iterable_1 和 iterable_2 调成一样的长度，不足的伸缩调整

-----

.. autofunction:: manimlib.utils.iterables.hash_obj

获取 object 的哈希值