# Funciones anidadas

def funcion_mayor():

    print("Esta es una función mayor y su mensaje de salida.")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

    def frameworks():
        print("Algunos frameworks de Python son: Django, Dash y Flask.")

    # Las funciones anidadas deben ser llamadas desde la funcion principal
    librerias()
    frameworks()


def main():
    funcion_mayor()


if __name__ == '__main__':
    main()
