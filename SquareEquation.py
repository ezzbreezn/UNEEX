a, b, c = map(float, input().split(','))
if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        print(-c / b)
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print(0)
    elif d == 0:
        print(-b / (2 * a))
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        print(f'{x1} {x2}')
 