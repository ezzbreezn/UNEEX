import time

def sort_key(record):
    return (record[0], record[1][1], record[1][0], record[1][2])

record = input().split()
records = []
while record:
    records.append([time.strptime(record[-1], "%H:%M:%S"), [record[0], record[1], ' '.join(record[2 : len(record) - 1]), record[-1]]])
    record = input().split()
records.sort(reverse=False, key=sort_key)
    
output = [records[0][1]]
num = 0
idx = 0
while idx < (len(records) - 1) and num < 3:
    idx += 1
    if records[idx][0] != records[idx - 1][0]:
        num += 1
    if num < 3:
        output.append(records[idx][1])
            
lengths = [0] * len(output[0])
for row in output:
    for i in range(len(row)):
        if len(row[i]) > lengths[i]:
            lengths[i] = len(row[i])
for row in output:
    for i in range(len(row)):
        print('{:<{width}}'.format(row[i], width=lengths[i]), end=' ')
    print()
