from functools import reduce
from itertools import tee

def seesaw(sequence):
    seq1, seq2 = tee(sequence)
    for elem1 in seq1:
        if elem1 % 2 == 0:
            yield elem1
            for elem2 in seq2:
                if elem2 % 2 == 1:
                    yield elem2
                    break
    for elem2 in seq2:
        if elem2 % 2 == 1:
            yield elem2   
