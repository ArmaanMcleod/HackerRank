#!/bin/python3

import math
import os
import random
import re
import sys

from queue import PriorityQueue

# Complete the maximumToys function below.
def maximumToys(prices, k):
    pr_queue = PriorityQueue(len(prices))

    for price in prices:
        if price <= k:
            pr_queue.put(price)

    count = 0
    total = 0
    while not pr_queue.empty():
        price = pr_queue.get()
        if k - total < price:
            break

        total += price
        count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
