# python nos permite cambiar el comportamiento
# de la superclase para adaptarlo a la subclase de

class Person:

    def __init__(self, name):
        self.name = name

    def foward(self):
        print('Ando caminando')


class Cyclist(Person):

    def __init__(self, nombre):
        super().__init__(nombre)

    # definimos el metodo avanza tal cual como en la super clase
    # con los mismos argumentos. Notamos que no hay necesidar de
    # declarar el name dentro de la subclase
    def foward(self):
        print('Ando moviendome en bici')


def main():
    persona = Person('Mauricio')
    persona.foward()

    ciclista = Cyclist('Sarah')
    ciclista.foward()


if __name__ == '__main__':
    main()
