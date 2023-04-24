def statcounter():
    class stat_gen:
        def __init__(self):
            self.d = {}
        def send(self, func):
            if func is None:
                return self.d
            self.d[func] = 0
            def newfunc(*args, **kwargs):
                res = func(*args, **kwargs)
                if func in self.d:
                    self.d[func] += 1
                else:
                    self.d[func] = 1
                return res
            return newfunc
            
        def __next__(self):
            return self.d

    obj = stat_gen()
    return obj
