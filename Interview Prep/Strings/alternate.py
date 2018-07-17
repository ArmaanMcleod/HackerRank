#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import groupby

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    sums = 0
    for _, g in groupby(s):
        sums += len(list(g)[1:])

    return sums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
