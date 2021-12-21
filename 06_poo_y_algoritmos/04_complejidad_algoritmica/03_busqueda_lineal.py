import random


def lineal_search(list, target):
    match = False

    for element in list:
        if element == target:
            match = True
            break
    return match


def main():
    list_size = int(input('Enter list size: '))
    target = int(input('Enter the target number: '))

    list = [random.randint(0, 100) for i in range(list_size)]

    found = lineal_search(list, target)

    print(list)
    print(f'The element {target} {"it was found" if found else "it was not found"}')

if __name__ == "__main__":
    main()
