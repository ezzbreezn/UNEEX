class Nuts:
    def __init__(self, *args):
        pass
    
    def __getitem__(self, idx):
        return idx
    
    def __setitem__(self, idx, val):
        pass
    
    def __delitem__(self, idx):
        pass
    
    def __getattribute__(self, attr):
        return attr
    
    def __setattr__(self, attr, val):
        pass
    
    def __delattr__(self, attr):
        pass
    
    def __str__(self):
        return "Nuts"
    
    def __iter__(self):
        return iter('Nuts')
    
    def __next__(self):
        raise StopIteration
