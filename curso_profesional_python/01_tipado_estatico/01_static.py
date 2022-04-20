# Declaracion de varibales estaticas

#var: type = value

from typing import List, Dict, Tuple
a: int = 5
print(a)
b: str = 'Hola'
print(b)
c: bool = True
print(c)

# funciones

# -> para definir el tipo de valor retornado


def suma(a: int, b: int) -> int:
    return a + b


print(suma(1, 2))

# Para listas y diccionarios:

positives: List[int] = [1, 2, 3, 4, 5, 6]

users: Dict[str, int] = {
    'argentina': 1,
    'colombia': 2,
    'mexico': 3,
}

# Tulpes
# Las tuplas al ser inmutables se pueden definir el tipo de cada uno de sus elementos
numbers: Tuple[int, float, int] = (1, 0.5, 1)
