import inspect
import itertools as it


def get_all_descendent_classes(Class): # 获取所有子类
    awaiting_review = [Class]
    result = []
    while awaiting_review:
        Child = awaiting_review.pop()
        awaiting_review += Child.__subclasses__()
        result.append(Child)
    return result


def filtered_locals(caller_locals): # 过滤self和kwargs
    result = caller_locals.copy()
    ignored_local_args = ["self", "kwargs"]
    for arg in ignored_local_args:
        result.pop(arg, caller_locals)
    return result


def digest_config(obj, kwargs, caller_locals={}):
    """
    Sets init args and CONFIG values as local variables

    The purpose of this function is to ensure that all
    configuration of any object is inheritable, able to
    be easily passed into instantiation, and is attached
    as an attribute of the object.
    """

    # caller_locals指当前局部变量，用法digest_config(self, kwargs, locals())
    # 先使用filtered_locals()过滤掉self和kwargs                      ↑ 当前所有局部变量
    # 然后把局部变量也添加到__dict__中

    # Assemble list of CONFIGs from all super classes
    classes_in_hierarchy = [obj.__class__]
    static_configs = []
    while len(classes_in_hierarchy) > 0:
        Class = classes_in_hierarchy.pop()
        classes_in_hierarchy += Class.__bases__   # 获取父类
        if hasattr(Class, "CONFIG"):              # 获取当前类和所有父类的CONFIG字典
            static_configs.append(Class.CONFIG)

    # Order matters a lot here, first dicts have higher priority
    caller_locals = filtered_locals(caller_locals)
    all_dicts = [kwargs, caller_locals, obj.__dict__]
    all_dicts += static_configs
    obj.__dict__ = merge_dicts_recursively(*reversed(all_dicts))


def merge_dicts_recursively(*dicts):
    """
    Creates a dict whose keyset is the union of all the
    input dictionaries.  The value for each key is based
    on the first dict in the list with that key.

    dicts later in the list have higher priority

    When values are dictionaries, it is applied recursively
    """
    result = dict()
    all_items = it.chain(*[d.items() for d in dicts])
    for key, value in all_items:
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts_recursively(result[key], value)
        else:
            result[key] = value
    return result


def soft_dict_update(d1, d2):
    """
    Adds key values pairs of d2 to d1 only when d1 doesn't
    already have that key
    """
    for key, value in list(d2.items()):
        if key not in d1:
            d1[key] = value


def digest_locals(obj, keys=None): # 把局部变量设为属性
    caller_locals = filtered_locals(
        inspect.currentframe().f_back.f_locals
    )
    if keys is None:
        keys = list(caller_locals.keys())
    for key in keys:
        setattr(obj, key, caller_locals[key])

# Occasionally convenient in order to write dict.x instead of more laborious
# (and less in keeping with all other attr accesses) dict["x"]


class DictAsObject(object):
    def __init__(self, dict):
        self.__dict__ = dict
