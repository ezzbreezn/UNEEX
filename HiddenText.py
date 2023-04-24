s1 = input()
s2 = input()
state = False
if (s2 == ""):
    state = True
if len(s1) == 1 or len(s2) == 1:
    state = s2 in s1
else:
    for i in range(1, len(s1) // (len(s2) - 1) + 1):
        for j in range(i):
            if s2 in s1[j::i]:
                state = True
                break
if state:
    print("YES")
else:
    print("NO")
