# funciones como objetos de primera clase

def presentarse(nombre):
    return f"Me llamo {nombre}"


def estudiemos_juntos(nombre):
    return f"¡Hey {nombre}, aprendamos Python!"


def consume_funciones(funcion_entrante):
    return funcion_entrante("David")


def main():

    print(consume_funciones(estudiemos_juntos))


if __name__ == "__main__":
    main()
