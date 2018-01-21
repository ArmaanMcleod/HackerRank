N = int(input().strip())

if N % 2 != 0:
    print('Weird')
else:
    if 2 <= N <= 5 or N > 20:
        print('Not Weird')
    else:
        print('Weird')