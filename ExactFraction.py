import fractions
import decimal
import re

def process(num):
    return 'fractions.Fraction("' + str(num[0]) + '")'

s = input()

s = re.sub(r'(\.)*(\d+)(\.)*(\d+)*', process, s)

val = eval(s)
print(val)
