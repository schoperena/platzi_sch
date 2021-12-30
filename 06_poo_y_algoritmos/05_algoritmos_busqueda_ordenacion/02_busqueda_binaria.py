# si la lista esta ordenada: busqueda binaria
# si la lista está desordenada: busqueda lineal_search

import random

def binary_search(list, start, end, target):
    print(f'Searching {target} between {list[start]} and {list[end-1]}')
    
    if start > end:
        return False

    half = (start + end) // 2

    if list[half] == target:
        return True
    elif list[half] < target:
        return binary_search(list, half + 1, end, target)
    else:
        return binary_search(list, start, half - 1, target)

def main():
    list_size = int(input('Enter list size: '))
    target = int(input('Enter the target number: '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(list, 0, len(list), target)

    print(list)
    print(f'The element {target} {"it was found" if found else "it was not found"}')

if __name__ == "__main__":
    main()
