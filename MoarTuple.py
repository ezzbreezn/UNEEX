def moar(a, b, n):
    a_count = len([x for x in a if x % n == 0])
    b_count = len([x for x in b if x % n == 0])
    return a_count > b_count
