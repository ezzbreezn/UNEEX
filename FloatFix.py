import types
import numbers
import inspect


def decorator(f, ndigits):
    def res(*args, **kwargs):   
        rv = f(*args, **kwargs)
        if isinstance(rv, numbers.Real):
            return round(rv, ndigits)
        else:
            return rv
    return res

class fixed(type):
    def __new__(metaclass, new_class_name, new_class_parents, new_class_attr, ndigits=3):
        new_attrs = {}
        for attr, val in new_class_attr.items():
            if callable(val):
                new_attrs[attr] = decorator(val, ndigits)
            else:
                new_attrs[attr] = val
        return type(new_class_name, new_class_parents, new_attrs)
