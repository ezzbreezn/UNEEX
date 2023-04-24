import decimal

def f(str_f, x):
    func = eval(str_f)
    return func

str_f = input()
D = int(input())
decimal.getcontext().prec = D + 2
    
lb = decimal.Decimal('-1.5')
lval = f(str_f, lb)
rb = decimal.Decimal('1.5')
rval = f(str_f, rb)
zero = decimal.Decimal('0')
while rval != zero and (rb-lb) > 10 ** (-D):
    mid = (lb + rb) / 2
    midval = f(str_f, mid)
    if (midval > 0 and lval > 0) or (midval < 0 and lval < 0):
        lb = mid
        lval = midval
    else:
        rb = mid
        rval = midval   
print('{:.{precision}f}'.format(rb, precision=D))
    
