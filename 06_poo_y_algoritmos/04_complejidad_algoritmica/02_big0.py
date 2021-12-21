def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) = O(n) //Crecimiento lineal


def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n*n) = O(n+n) = O(n + n^2) = O(n^2) //Crecimiento exponencial


def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2**n) //tiene varias llamadas recursivas y eso hace al algoritmo con un crecimiento exponencial
