from math import factorial
from decimal import Decimal, getcontext

def PiGen():
    getcontext().prec = 10000
    res = Decimal('0')
    k = 0
    numerator = 13591409
    denominator = 1
    const = Decimal(426880) * Decimal(10005).sqrt()

    while True:
        term = Decimal(factorial(6 * k)) * numerator
        term /= (Decimal(factorial(3 * k) * (factorial(k) ** 3) * denominator)) 
        res += term
        ans = const / res
        yield ans
        k += 1
        numerator += 545140134
        denominator *= -262537412640768000
