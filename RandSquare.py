import random
from math import cos, sin, pi, atan2

def randsquare(A, B):
    angle = pi / 4 - atan2(A[1] - B[1], A[0] - B[0])
    shape = ((A[0] - B[0]) * cos(angle) - (A[1] - B[1]) * sin(angle), (A[0] - B[0]) * sin(angle) + (A[1] - B[1]) * cos(angle))
    res = (random.random() * shape[0], random.random() * shape[1])
    res = (res[0] * cos(-angle) - res[1] * sin(-angle), res[0] * sin(-angle) + res[1] * cos(-angle))
    return res[0] + B[0], res[1] + B[1]


