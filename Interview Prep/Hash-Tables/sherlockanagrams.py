#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
from itertools import combinations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    length = len(s)

    groups = defaultdict(list)
    for i in range(length):
        for j in range(i, length):
            string = s[i:j+1]
            groups[''.join(sorted(string))].append(string)

    sums = 0
    for v in groups.values():
        sums += len(list(combinations(v, 2)))

    return sums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
