n = int(input())

d = {}
for _ in range(n):
    info = input().split()
    name, number = info[0], info[1]
    d[name] = number

to_lookup = []
while True:
    try:
        lookup = input()
        to_lookup.append(lookup)
    except EOFError:
        break

for name in to_lookup:
    if name in d:
        print('%s=%s' % (name, d[name]))
    else:
        print('Not found')

