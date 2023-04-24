import math
ans = set()
n = int(input())
sq = math.ceil(n ** 0.5)
for x in range(math.ceil(sq / 2), sq + 1):
    x_sq = x * x
    for y in range(x + 1):
        y_sq = y * y
        for z in range(y + 1):
            z_sq = z * z
            t_sq = n - x_sq - y_sq - z_sq
            if t_sq >= 0:
                t = t_sq ** 0.5
                if x_sq + y_sq + z_sq + math.floor(t) * math.floor(t) == n:
                    ans.add(tuple(sorted([x, y, z, math.floor(t)], reverse=True)))
                elif x_sq + y_sq + z_sq + math.ceil(t) * math.ceil(t) == n:
                    ans.add(tuple(sorted([x, y, z, math.ceil(t)], reverse=True)))
            else:
                break
                    
for seq in sorted(ans):
    print(' '.join(map(str, seq)))

