"""
Ganas si al tirar los dados el primero es 6
y el segundo es 4
"""

from art import *
import random
import os


def main():
    os.system("cls")  # limpia la terminal, "clear" en linux
    tprint("DADOS", font="larry3d ")
    print("By @schoperena")

    while True:
        menu = input(
"""
Quieres lanzar los dados?
¿si o no?
"""
        )

        try:
            if menu.lower()[0] != "s":
                break
            else:
                n1 = random.randint(1, 6)
                print("Dado 1: ", n1)
                n2 = random.randint(1, 6)
                print("Dado 2: ", n2)
            if n1 == 6 and n2 == 4:
                print("Ganaste!")
                break
            else:
                print("mala suerte")
                continue
        except:
            print("Debes ingresar si o no, s o n")


if __name__ == "__main__":
    main()
