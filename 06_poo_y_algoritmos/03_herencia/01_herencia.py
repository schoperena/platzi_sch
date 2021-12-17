
class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height * self.base

# Definimos la superclase de donde se hereda


class Square(Rectangle):

    def __init__(self, lado):
        # Con super accedemos a la superclase y llamamos al constructor de la misma
        super().__init__(lado, lado)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle.area())

    square = Square(5)
    print(square.area())


if __name__ == '__main__':
    main()
