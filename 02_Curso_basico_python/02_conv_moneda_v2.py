menu = int(input("""
1 - Peso colombianos
2 - Peso Argentino
3 - Peso Mexicano

Ingrese una opcion: 
"""))
if menu == 1:
    dolar = 4000
elif menu == 2:
    dolar = 100.76
elif menu == 3:
    dolar = 20.83

peso = int(input("Ingrese el valor a convertir: "))
cambio = peso/dolar
print("Los ${} pesos a dolares es: {} USD".format(peso,cambio))