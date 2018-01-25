from itertools import groupby

n = int(input().strip())

binary = bin(n)[2:]

print(max(sum(map(int, g)) for _, g in groupby(binary)))
