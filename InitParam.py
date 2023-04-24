import inspect

def decorator(f):
    def res(*args, **kwargs):
        new_args = list(args)
        params = inspect.getfullargspec(f)
        sig = inspect.signature(f)
        defaults = {k: v.default for k, v in sig.parameters.items() if v.default is not inspect.Parameter.empty}
        pos = params.args
        for i in range(len(args), len(pos)):
            if pos[i] in params.annotations:
                if pos[i] not in defaults:
                    if pos[i] in kwargs:
                        new_args.append(kwargs[pos[i]])
                    else:
                        t = params.annotations[pos[i]]
                        try:
                            dv = t()
                        except:
                            new_args.append(None)
                        else:
                            new_args.append(t())
                elif pos[i] in kwargs:
                    new_args.append(kwargs[pos[i]])
                else:
                    new_args.append(defaults[pos[i]])
        return f(*new_args)
    return res

class init(type):
    def __new__(metaclass, new_class_name, new_class_parents, new_class_attrs):
        new_attrs = {}
        for attr, val in new_class_attrs.items():
            if callable(val):
                new_attrs[attr] = decorator(val)
            else:
                new_attrs[attr] = val
        return type.__new__(metaclass, new_class_name, new_class_parents, new_attrs)
