import tarfile, sys, io

archive = io.BytesIO(bytes.fromhex(sys.stdin.read()))
tar = tarfile.open(fileobj=archive, mode='r')
num = 0
size = 0
for f in tar.getmembers():
    if f.isfile():
        num += 1
        size += f.size

print(size, ' ', num)


