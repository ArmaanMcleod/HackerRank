#!/bin/python3

import math
import os
import random
import re
import sys

from operator import itemgetter

# Complete the isBalanced function below.
def isBalanced(s):
    # Complete this function
    brackets = [('{', '}'), ('(', ')'), ('[', ']')]
    
    opening = list(map(itemgetter(0), brackets))
    closing = dict(map(reversed, brackets))

    stack = []

    for char in s:

        # opening
        if char in opening:
            stack.append(char)

        # closing
        elif char in closing:
            if not stack or stack.pop() != closing[char]:
                return "NO"

    if not stack:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
