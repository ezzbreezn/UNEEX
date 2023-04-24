class NegExt():
    def __neg__(self):
        MRO = type(self).mro()
        self.next_class = MRO[MRO.index(NegExt) + 1]
        if hasattr(self.next_class, '__neg__'):
            return MRO[0](self.next_class.__neg__(self))
        try:
            res = MRO[0](self[1:-1])
        except (Exception, RuntimeError, TypeError, NameError):
            return MRO[0](self)
        else:
            return res
