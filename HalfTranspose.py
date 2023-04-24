a = []
s = list(map(int, input().split(',')))
a.append(s)
length = len(s)
for i in range(1, length):
    s = list(map(int, input().split(',')))
    a.append(s)

for i in range(len(a)):
    out = []
    for j in range(i + 1):
        out.append(a[i][j])
    for j in range(1, i + 1):
        out.append(a[i - j][i])
    print(','.join(map(str, out)))
