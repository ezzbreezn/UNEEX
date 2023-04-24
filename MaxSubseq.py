x = int(input())
prev = None
length = 0
max_length = 0
while x != 0:
    if prev is None:
        length = 1
    else:
        if x >= prev:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
    prev = x
    x = int(input())
if length > max_length:
    max_length = length
print(max_length)
