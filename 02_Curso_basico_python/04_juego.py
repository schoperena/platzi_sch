import random

def juego(numero):
    random_num = random.randint(1,100)
    while numero != random_num:
        if numero > random_num:
            numero = int(input("Tu numero es menor, ingresa otro: "))
        else:
            numero = int(input("Tu numero es mayor, ingresa otro: "))
    print("Adivinaste!")

juego(int(input("Ingresa un numero del 1 al 100: ")))