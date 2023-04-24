def No_2Zero(N, K):
    def func(x, k):
        if x == 1:
            return k - 1
        elif x == 2:
            return k ** 2 - k
        else:
            return (k - 1) * (func(x - 1, k) + func(x - 2, k))
    return func(N, K)
