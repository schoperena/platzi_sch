import random


def list_generator(n):
    out_list = []
    for _ in range(n):
        out_list.append(random.randint(0, 10))

    return out_list


def remove_duplciates(some_list):
    list_without_duplicates = []

    for element in some_list:
        if element not in list_without_duplicates:
            list_without_duplicates.append(element)

    return list_without_duplicates


if '__main__' == __name__:
    random_list = list_generator(10)
    print(random_list)
    print(remove_duplciates(random_list))

    # con sets en una sola linea lol
    print(list(set(random_list)))
    