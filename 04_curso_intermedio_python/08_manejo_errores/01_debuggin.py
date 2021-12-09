def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se puede ingresar numeros negativos")   
        divisors = [i for i in range(1, num+1) if num%i == 0] 
        return divisors
    except ValueError as ve:
        return ve   

def main():
    try:
        num = int(input("Ingrese un numero: "))
        print(divisors(num))
        print("termino el programa")
    except ValueError:
        print("Debes ingresa un numero entero")
    

if __name__ == '__main__':
    main()