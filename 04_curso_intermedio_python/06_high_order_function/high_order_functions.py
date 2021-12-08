# Example

def saludo(func):
    func()

def hola():
    print("Holaaa")

def adios():
    print("Adios")

saludo(hola)
saludo(adios)

# Filter

my_list = [1,4,5,6,9,13,19,21]

""" 
la funcion filter retorna un iterable, por eso está dentro de list
para covertirlo en una lista.
"""
odd = list(filter(lambda x: x%2 !=0, my_list))
print(odd)

# Map

my_list = [1,2,3,4,5]
#squares = [i**2 for i in my_list]
squares = list(map(lambda x: x**2, my_list))
print(squares)

#reduce
from functools import reduce

my_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a*b, my_list)
print(all_multiplied)