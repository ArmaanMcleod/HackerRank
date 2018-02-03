n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0
for i in range(n):
    currSwaps = 0
    for j in range(n - 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] a[j+1]
            a[j+1] = temp
            currSwaps += 1

    if currSwaps == 0:
        break

    numSwaps += currSwaps

print('Array is sorted in %d swaps' % numSwaps)
print('First Element: %d' % a[0])
print('Last Element: %d' % a[-1])

