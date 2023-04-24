def nomore(sequence):
    for elem in sequence:
        for x in sequence:
            if x <= elem:
                yield x
