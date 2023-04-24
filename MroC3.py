class_dict = {}
order = []
s = input()
last_name = ''

while s:
    if s.find('class') == 0:
        pos1 = s.find(' ')
        pos2 = s.find('(')
        if pos2 == -1:
            class_name = s.split()[1][:-1]
            class_dict[class_name] = []
        else:
            pos3 = s.find(')')
            inherited = s[pos2 + 1: pos3].split(', ')
            class_name = s[:pos2].split()[1]
            class_dict[class_name] = []
            for c in inherited:
                class_dict[class_name].append(c)
        last_name = class_name
        order.append(last_name)
    s = input()

f = True



#def mroc3_check(c):
#    idx = [order.index(x) for x in class_dict[c]]
#    prev = len(order)
#    for i in range(len(idx)):
#        if len(class_dict[class_dict[c][i]]) > 0:
#            if mroc3_check(c):
#                continue
#            else:
#                return False
#        elif idx[i] < order.index(c) and idx[i] < prev:
#            prev = idx[i]
#        else:
#            return False
#    return True

#for c in class_dict[last_name]:
#    if not mroc3_check(c):
#        f = False
#        print('No')
#        break

if f:
    print('Yes')
     
