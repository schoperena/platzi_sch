def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("no se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve: #ve es el alias del value error
        print(ve)
        return False


#si no se ingresa un string nos mostrara un mensaje que se debe ingresar un string
try:
    print(palindrome(""))
except TypeError:
    print("solo puden ingresar strings")
