def fix(num):
    def decorator(f):
        def res(*args, **kwargs):
            new_args = []
            new_kwargs = {}
            for arg in args:
                if isinstance(arg, float):
                    new_args.append(round(arg, num))
                else:
                    new_args.append(arg)
            for kwarg, val in kwargs.items():
                if isinstance(val, float):
                    new_kwargs[kwarg] = round(val, num)
                else:
                    new_kwargs[kwarg] = val
            
            ret = f(*new_args, **kwargs)
            if isinstance(ret, float):
                return round(ret, num)
            else:
                return ret
        return res
    return decorator
