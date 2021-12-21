import time
import sys


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


def main():

    sys.setrecursionlimit(1500)

    n = 1000

    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
