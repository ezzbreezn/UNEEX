class Pushpull:
    __pos = 0
    def __init__(self, p=0):
        Pushpull.__pos = p

    def push(self, n=1):
        Pushpull.__pos += n

    def pull(self, n=1):
        Pushpull.__pos -= n

    def __str__(self):
        if Pushpull.__pos < 0:
            return '<' + str(abs(Pushpull.__pos)) + '<'
        elif Pushpull.__pos > 0:
            return '>' + str(abs(Pushpull.__pos)) + '>'
        else:
            return '<0>'

    def __iter__(self):
        if Pushpull.__pos >= 0:
            return iter(range(Pushpull.__pos))
        else:
            return iter(range(0, Pushpull.__pos, -1))
