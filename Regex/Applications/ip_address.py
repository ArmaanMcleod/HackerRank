# IP Address Validation Hackerrank

def IPv4(line):
    items = [item.strip() for item in line.split('.')]

    if len(items) == 4:
        valid = 0
        for item in items:
            try:
                item = int(item)
                if 0 <= item <= 255:
                    valid += 1
            except ValueError:
                break

        if valid == 4:
            return True

    return False

def IPv6(line):
    items = [item.strip() for item in line.split(':')]

    if len(items) == 8:
        valid = 0
        for item in items:
            try:
                item = int(item, 16)
                valid += 1
            except ValueError:
                break

        if valid == 8:
            return True

    return False

def main():
    N = int(input())

    for _ in range(N):
        line = input()

        if IPv4(line):
            print('IPv4')
        elif IPv6(line):
            print('IPv6')
        else:
            print('Neither')

if __name__ == '__main__':
    main()