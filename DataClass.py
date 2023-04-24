def sloter(fields, default):
    class res:
        __slots__ = fields
        val = default
        def __init__(self):
            for field in self.__slots__:
                setattr(self, field, self.val)
       
        def __delattr__(self, field):
            setattr(self, field, self.val)

        def __iter__(self):
            for field in self.__slots__:
                yield getattr(self, field)
    return res   
