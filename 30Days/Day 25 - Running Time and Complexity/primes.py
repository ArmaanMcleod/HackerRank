from math import sqrt

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

def main():
    T = int(input())

    numbers = [int(input()) for i in range(T)]

    for number in numbers:
        if isPrime(number):
            print("Prime")
        else:
            print("Not prime")

if __name__ == '__main__':
    main()

