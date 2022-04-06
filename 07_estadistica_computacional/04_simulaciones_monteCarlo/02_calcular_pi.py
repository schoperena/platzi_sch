import random
import math

def generar_puntos(numero_puntos):
    dentro_circulo = 0
    
    for _ in range(numero_puntos):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)
        
        if distancia_desde_el_centro <= 1:
            dentro_circulo += 1

    return (4*dentro_circulo) / numero_puntos

if '__main__' == __name__:
    main()