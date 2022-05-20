StringMobject
=============

该类由 `凡人忆拾 <https://github.com/YishiMichael>`__ 编写，旨在让用户更加方便地对物件进行切片操作。
该类的实例支持 :class:`~manimlib.animation.transform_matching_parts.TransformMatchingStrings` 动画。

该类为 :class:`~manimlib.mobject.svg.mtex_mobject.MTex` 和 :class:`~manimlib.mobject.svg.text_mobject.MarkupText` 
共同的抽象基类。如果想要在将来通过子字符串进行物件的切片，用户应当在创建实例时指定这些子字符串。可以通过 ``isolate`` 参数指定子串，
派生类的其它参数（包括 :class:`~manimlib.mobject.svg.mtex_mobject.MTex` 的 ``tex_to_color_map`` 字典键，
:class:`~manimlib.mobject.svg.text_mobject.MarkupText` 的 ``t2c`` 字典键等）也可以指定子串，

该文件定义了 ``Selector`` 类型如下：

.. code-block:: python

    Selector = Union[
        str,
        re.Pattern,
        tuple[Union[int, None], Union[int, None]],
        Iterable[Union[
            str,
            re.Pattern,
            tuple[Union[int, None], Union[int, None]]
        ]]
    ]

可以通过以下任意一种或多种方式指定子串（详情请参阅各个子类）：

- ``isolate`` 参数（``Selector`` 类型）；
- 派生类的部分参数；
- 派生类特定的文本内部指定模式。

.. admonition:: 注意

    以以上方式指定的所有子串两两不能“部分重合”（一个完全包含另一个是可以的）。

对于指定了至少一个子串的实例，该类将额外生成一份包含颜色信息的SVG（每种颜色对应一个被指定的子串），并按照位置匹配两个 SVG 的各个物件，
使得原始 SVG 的每个物件对应上该颜色标签，从而完成子串与物件的对应。

StringMobject
*************

.. autoclass:: manimlib.mobject.svg.string_mobject.StringMobject
    :members:
