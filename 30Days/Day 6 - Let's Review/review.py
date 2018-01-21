t = int(input())

lines = []
for i in range(t):
    string = input()
    lines.append(string)

for line in lines:
    even = []
    odd = []
    for i, e in enumerate(line):
        if i % 2 == 0:
            even.append(e)
        else:
            odd.append(e)

    print(''.join(even), ''.join(odd))

