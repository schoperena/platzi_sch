import random
import math
from estadisticas import desviacion_estandar, media


def generar_puntos(numero_puntos):
    dentro_circulo = 0

    for _ in range(numero_puntos):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            dentro_circulo += 1

    return (4*dentro_circulo) / numero_puntos


def estimacion(numero_puntos, intentos):
    estimados = []

    for _ in range(intentos):
        estimacion_pi = generar_puntos(numero_puntos)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados, 5)}, sigma={round(sigma, 5)}, nPuntos={numero_puntos}')
    return (media_estimados, sigma)


def estimar_pi(precision, intentos):

    numero_puntos = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_puntos, intentos)
        numero_puntos *= 2
    

if '__main__' == __name__:
    estimar_pi(0.01, 1000)
