arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

sums = []
for i in range(len(arr) - 2):
    row1 = [arr[i][j:j+3] for j in range(len(arr[i]) - 2)]
    row2 = [x for x in arr[i+1][1:-1]]
    row3 = [arr[i+2][j:j+3] for j in range(len(arr[i+2]) - 2)]

    sums.extend([sum(x + [y] + z) for x, y, z in zip(row1, row2, row3)])

print(max(sums))

