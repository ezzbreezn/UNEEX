from collections import OrderedDict, defaultdict

class Spiral:    
    def __init__(self, string):
        self.string = string
        self.coord = defaultdict(lambda: defaultdict(lambda: " "))
        self.left_bound = 0
        self.upper_bound = 0
        self.right_bound = 0
        self.lower_bound = 0
        x = 0
        y = 0
        counter = 0
        bound = 1
        direction = 0
        l = len(string)
        for i in range(l - 1):
            self.coord[x][y] = string[i]
            if direction == 0:
                x += 1
                self.right_bound = max(self.right_bound, x)
            elif direction == 1:
                y += 1
                self.upper_bound = max(self.upper_bound, y)
            elif direction == 2:
                x -= 1
                self.left_bound = min(self.left_bound, x)
            else:
                y -= 1
                self.lower_bound = min(self.lower_bound, y)
            counter += 1
            if counter == bound:
                counter = 0
                bound += 1
                direction = (direction + 1) % 4
        if l > 0:
            self.coord[x][y] = string[l - 1]
        
    def __str__(self):
        res = ""
        for y in range(self.upper_bound, self.lower_bound - 1, -1):
            for x in range(self.left_bound, self.right_bound + 1):
                res += self.coord[x][y]
            res += '\n'
        return res[:-1]
    
    def __add__(self, other):
        res_dict = OrderedDict()
        for elem in self.string:
            res_dict[elem] = res_dict.get(elem, 0) + 1        
        for elem in other.string:
            res_dict[elem] = res_dict.get(elem, 0) + 1
        res_string = ""
        for key, value in res_dict.items():
            res_string += key * value
        return Spiral(res_string)
    
    def __sub__(self, other):
        res_dict = OrderedDict()
        for elem in self.string:
            res_dict[elem] = res_dict.get(elem, 0) + 1
        for elem in other.string:
            if elem in res_dict:
                res_dict[elem] -= 1
        res_string = ""
        for key, value in res_dict.items():
            res_string += key * value
        return Spiral(res_string)
    
    def __mul__(self, n):
        res_string = []
        for elem in self.string:
            res_string.extend([elem] * n)
        return Spiral(''.join(res_string))
    
    def __iter__(self):
        return iter(self.string)
