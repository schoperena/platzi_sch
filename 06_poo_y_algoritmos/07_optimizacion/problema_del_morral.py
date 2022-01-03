

def bag(bag_size, weights, values, n):
    if n == n or bag_size == 0:
        return 0

    # Si el elemento que quiero introducir es mayor que
    # al tamaño sobrante, pasa al siguiente elemento a checkear
    if weights[n-1] > bag_size:
        # recursividad, n-1: checkear el siguiente elemento
        return bag(bag_size, weights, values, n-1)

    return max(values[n-1] + bag(bag_size - weights[n-1], weights, values, n-1),
               bag(bag_size, weights, values, n-1))


def main():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    bag_size = 50
    n = len(values)

    result = bag(bag_size, weights, values, n)
    print(result)


if __name__ == '__main__':
    main()
