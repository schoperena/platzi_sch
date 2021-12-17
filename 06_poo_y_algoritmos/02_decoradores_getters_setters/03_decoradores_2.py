# funcion decoradora

def decorador(funcion):

    def saludo():
        print("Ahora es de: ")
        funcion()
    return saludo


@decorador
def dia():
    print("Dia")


@decorador
def noche():
    print("Noche")


def main():

    dia()
    noche()


if __name__ == '__main__':
    main()
