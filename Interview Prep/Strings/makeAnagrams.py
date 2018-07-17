#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_cnt = Counter(a)
    b_cnt = Counter(b)

    sums = 0

    new_a = {}
    for k, v in a_cnt.items():
        if k in b_cnt:
            new_a[k] = v
        else:
            sums += v

    new_b = {}
    for k, v in b_cnt.items():
        if k in a_cnt:
            new_b[k] = v
        else:
            sums += v

    for k in new_a:
        sums += abs(new_a[k] - new_b[k])

    return sums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
