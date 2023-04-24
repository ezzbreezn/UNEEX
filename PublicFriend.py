d = {}
M, N = map(int, input().split(', '))
while M != 0 or N != 0:
    if M not in d:
        d[M] = set()
        d[M].add(N)
    else:
        d[M].add(N)
    if N not in d:
        d[N] = set()
        d[N].add(M)
    else:
        d[N].add(M)
    M, N = map(int, input().split(', '))

keys = sorted(d.keys())

for key in keys:
    d[key].add(key)
    if d[key] == set(keys):
        print(key, end=' ')
