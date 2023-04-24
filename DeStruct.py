import base64, sys, io

s = bytes(base64.b85decode(input()))
length = len(s)
pos1 = 0
pos2 = 0
res = 0
c = 0
headers = []
while pos2 < length and s[pos2] != 0:
    c += 1
    pos2 += 1
while c > 0 and pos2 < length:
    header = s[pos1]
    if header > 127:
        header = -(255 - header + 1)
    headers.append(header)
    c -= 1
    pos1 += 1
pos2 += 1
shift = 0
while pos2 < length:
    if headers[shift] < 0:
        r = int.from_bytes(s[pos2:pos2+abs(headers[shift])], byteorder='big', signed=True)
    else:
        r = int.from_bytes(s[pos2:pos2+abs(headers[shift])], byteorder='big', signed=False)
    res += r
    pos2 += abs(headers[shift])
    shift = (shift + 1) % len(headers)

print(res)
