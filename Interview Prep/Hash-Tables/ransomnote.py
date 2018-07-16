#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_counts = Counter(magazine)

    valid = True
    for word in note:
        check_word = magazine_counts.get(word)
        if not check_word:
            valid = False
            break
        magazine_counts[word] -= 1

    if valid:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()
