def palindromo(palabra):
    if palabra[::] == palabra[::-1]:
        print("Es un palindromo")
    else: 
        print("No es un palindromo")

palindromo(input("Ingrese una palabra: ").lower().replace(" ",""))