#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
# Could use hashing to do this in O(n) instead of O(logn)
def whatFlavors(cost, money):
    sorted_costs = sorted((c, i) for i, c in enumerate(cost, start=1))

    low = 0
    high = len(sorted_costs) - 1
    pair = None

    while (low < high):
        sums = sorted_costs[low][0] + sorted_costs[high][0]
        if sums == money:
            pair = sorted_costs[low][1], sorted_costs[high][1]
            break
        elif sums < money:
            low += 1
        elif sums > money:
            high -= 1

    print(' '.join(map(str, sorted(pair))))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
