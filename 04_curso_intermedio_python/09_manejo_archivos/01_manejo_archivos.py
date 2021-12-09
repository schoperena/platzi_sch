from typing import Text


def read():
    with open("./archivos/numbers.txt", "r", encoding='utf-8') as f:
        number = [int(i) for i in f]
    print(number)

def write():
    names = ["Sebastian", "Pepe", "Sara"]
    with open("./archivos/names.txt", "w", encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def main():
    read()

if __name__ == '__main__':
    main()