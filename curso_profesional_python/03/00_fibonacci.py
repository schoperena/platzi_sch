
def fibinacci(n):
    fibonacci = []
    n1 = 0
    n2 = 1

    if n == 0:
        return n1
    elif n == 1:
        return n2
    else:
        for _ in range(n):
            fibonacci.append(n1)
            aux = n1 + n2
            n1, n2 = n2, aux
    return fibonacci


if '__main__' == __name__:
    n = 200
    for x in range(n):
        print(fibinacci(n)[x])
