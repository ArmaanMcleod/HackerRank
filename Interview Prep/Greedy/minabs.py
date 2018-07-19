#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)

    min_abs = sys.maxsize
    for x, y in zip(sorted_arr, sorted_arr[1:]):
        abs_pair = abs(x - y)

        if abs_pair < min_abs:
            min_abs = abs_pair

    return min_abs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
