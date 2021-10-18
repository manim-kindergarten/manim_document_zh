Simple_functions
================

``manimlib/utils/simple_functions.py`` 这个文件中包含了一些常用的简单函数


-----

.. autofunction:: manimlib.utils.simple_functions.sigmoid

sigmoid 函数， ``1/(1+e^(-x))``

-----

.. autofunction:: manimlib.utils.simple_functions.choose_using_cache

计算 :math:`C^k_n` ，并使用缓存

-----

.. autofunction:: manimlib.utils.simple_functions.choose

计算 :math:`C^k_n` ， 若 ``use_cache=True`` 则使用缓存，否则直接计算

-----

.. autofunction:: manimlib.utils.simple_functions.get_num_args

获取 function 的参数个数

-----

.. autofunction:: manimlib.utils.simple_functions.get_parameters

获取 function 的参数

-----

.. autofunction:: manimlib.utils.simple_functions.clip_in_place

将 ndarray 中小于 min 的值全设为 min，大于 max 的值全设为 max，并返回

-----

.. autofunction:: manimlib.utils.simple_functions.fdiv

计算 a/b，若 0/0 则返回 ``zero_over_zero_value``

-----

.. autofunction:: manimlib.utils.simple_functions.binary_search

二分查找
