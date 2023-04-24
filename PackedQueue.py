seq = list(eval(input()))
conv = []

for elem in seq:
    if type(elem) is tuple:
        for obj in elem:
            conv.append(obj)
    elif type(elem) is int:
        if elem > len(conv):
            break
        out = []
        for i in range(elem):
            x = conv.pop(0)
            out.append(x)
        print(tuple(out))   
