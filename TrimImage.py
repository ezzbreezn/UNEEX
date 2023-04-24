symb = [['.' for i in range(1000)] for j in range(1000)]
shift = 100
s = input()
x_min = None
x_max = None
y_min = None
y_max = None
while s:
    x, y, l, w, c = s.split()
    x = int(x)
    y = int(y)
    l = int(l)
    w = int(w)
    if l < 0:
        x_s = -1
        x -= 1
    else:
        x_s = 1
    if x_s < 0 and l != 0 and w != 0:
        if x_min is None or x + l + 1 < x_min:
            x_min = x + l + 1
        if x_max is None or x > x_max:
            x_max = x
    elif x_s > 0 and l != 0 and w != 0:
        if x_min is None or x < x_min:
            x_min = x
        if x_max is None or x + l - 1 > x_max:
            x_max = x + l - 1
    if w < 0:
        y_s = -1
        y -= 1
    else:
        y_s = 1
    if y_s < 0 and w != 0 and l != 0:
        if y_min is None or y + w + 1 < y_min:
            y_min = y + w + 1
        if y_max is None or y > y_max:
            y_max = y
    elif y_s > 0 and w != 0 and l != 0:
        if y_min is None or y < y_min:
            y_min = y
        if y_max is None or y + w - 1 > y_max:
            y_max = y + w - 1

    
    for i in range(x, x + l, x_s):
        for j in range(y, y + w, y_s):
            symb[j + shift][i + shift] = c
    s = input()

for y in range(y_min, y_max + 1):
    for x in range(x_min, x_max + 1):
        print(symb[y + shift][x + shift], end='')       
    print()
