from itertools import product

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None

    def computeDifference(self):
        pairs = product(self.__elements, repeat = 2)

        self.maximumDifference = max(abs(x - y) for x, y in pairs)

def main():
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)


if __name__ == '__main__':
    main()