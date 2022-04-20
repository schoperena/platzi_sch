
def decorador(func):
    def wrapper():
        print("Esto se añade a la funcion original")
        func()
    return wrapper

@decorador
def saludo():
    print("Hola")


if '__main__' == __name__:
    #saludo = decorador(saludo)
    saludo()
 