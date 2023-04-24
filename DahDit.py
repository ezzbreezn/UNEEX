class morse:
    def __init__(self, string='di dit dah'):
        self.dot = 'di'
        self.ddot = 'dit'
        self.dash = 'dah'
        self.elsep = ' '
        self.sep = ', '
        self.end = '.'
        self.res = ''
        self.start = True
        if ' ' in string:
            if string[-1] == ' ':
                self.end = ''
            words = string.split()
            if len(words) == 2:
                self.dot = words[0]
                self.ddot = words[0]
                self.dash = words[1]
            elif len(words) == 3:
                self.dot = words[0]
                self.ddot = words[1]
                self.dash = words[2]
            elif len(words) == 4:
                self.dot = words[0]
                self.ddot = words[1]
                self.dash = words[2]
                self.end = words[3]
        else:
            self.sep = ' '
            self.elsep = ''
            self.end = ''
            if len(string) == 2:
                self.dot = string[0]
                self.ddot = string[0]
                self.dash = string[1]
            elif len(string) == 3:
                self.dot = string[0]
                self.ddot = string[1]
                self.dash = string[2]
            elif len(string) == 4:
                self.dot = string[0]
                self.ddot = string[1]
                self.dash = string[2]
                self.end = string[3]
    
    def __str__(self):
        return self.res + self.end

    def __pos__ (self):
        if self.start:
            obj = self.ddot
            elsep = ''
        else:
            obj = self.dot
            elsep = self.elsep
        if self.res == '':
            self.res = obj + self.res
        else:
            self.res = obj + elsep + self.res
        self.start = False
        return self

    def __neg__(self):
        if self.start:
            elsep = ''
        else:
            elsep = self.elsep
        if self.res == '':
            self.res = self.dash + self.res
        else:
            self.res = self.dash + elsep + self.res
        self.start = False
        return self

    def __invert__(self):
        self.res = self.sep + self.res
        self.start = True
        return self
