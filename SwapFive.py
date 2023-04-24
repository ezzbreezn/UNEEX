x = int(input())
res = x
p = 2
if x == 0 or x == 1:
    print(x)
else:
    while True:
        new = res * x
        res = new * 10 + x
        if res * x == x * 10 ** p + new:
            break
        res %= 10 ** p
        p += 1
    print(res)
