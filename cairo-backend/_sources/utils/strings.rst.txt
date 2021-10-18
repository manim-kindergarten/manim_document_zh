Strings
=======

``manimlib/utils/strings.py`` 这个文件中主要实现了处理字符串的函数

-----

.. autofunction:: manimlib.utils.strings.to_camel_case

将name转化为驼峰命名（应该会报错）

-----

.. autofunction:: manimlib.utils.strings.initials

获取name中每个单词的首字母

-----

.. autofunction:: manimlib.utils.strings.camel_case_initials

获取name中的大写字母

-----

.. autofunction:: manimlib.utils.strings.complex_string

获取complex_num的每一个字符，括号除外

-----

.. autofunction:: manimlib.utils.strings.split_string_to_isolate_substrings

| 给出一个完整字符串，和一系列可能包含的字符串
| 将完整字符串分割，若出现可能包含的字符串，则将其分离

-  例： ``split_string_to_isolate_substrings("to be or not to be", "to", "be")`` 会返回 ``["to", " ", "be", " or not ", "to", " ", "be"]``


-----

.. autofunction:: manimlib.utils.strings.split_string_list_to_isolate_substrings

对string_list中每个字符串都执行 ``split_string_to_isolate_substrings(full_string, *substrings_to_isolate)``