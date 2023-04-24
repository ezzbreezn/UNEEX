def maxfun(*args):
    vals = args[0]
    i = 1
    num = len(args)
    max_sum = None
    for j in range(1, num):
        temp_sum = 0
        for val in vals:
            temp_sum += args[j](val)
        if max_sum is None or temp_sum >= max_sum:
            max_sum = temp_sum
            i = j
    return args[i]
