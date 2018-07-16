#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sums = []

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            top = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            middle = arr[i][j]
            bottom = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            hourglass_sums.append(top + middle + bottom)

    return max(hourglass_sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
