from collections import Counter

symbols = input()
d_1 = Counter()
d_2 = Counter()
prev_end = False
s = input()
while s: 
    words = s.split()
    for i in range(len(words)):
        if words[i][0] == symbols[1] and prev_end:
            d_1.update([words[i]])
        elif words[i][0] == symbols[2] and words[i][-1] == symbols[3]:
            d_2.update([words[i]])
        if words[i][-1] == symbols[0]:
            prev_end = True
        else:
            prev_end = False
    s = input()
           
if len(list(d_1.elements())) == 0:
    print('... 0', end=' ')
else:
    print(d_1.most_common(1)[0][0], end=' ')
    print(d_1.most_common(1)[0][1], end=' ')

print('-', end=' ')

if len(list(d_2.elements())) == 0:
    print('... 0', end=' ')
else:
    print(d_2.most_common(1)[0][0], end=' ')
    print(d_2.most_common(1)[0][1], end=' ')


