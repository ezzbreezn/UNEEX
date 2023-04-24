s = input()
xmin = None
xmax = None
ymin = None
ymax = None
zmin = None
zmax = None
while s:
    x, y, z = map(float, s.split(','))
    if xmin is None:
        xmin = x
        xmax = x
        ymin = y
        ymax = y
        zmin = z
        zmax = z
    else:
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y
        if z < zmin:
            zmin = z
        elif z > zmax:
            zmax = z
    s = input()
print((xmax - xmin) * (ymax - ymin) * (zmax - zmin))
