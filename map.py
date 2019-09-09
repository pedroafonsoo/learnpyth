"""
Map

Com Map, fazemos mapeamento de valores para função.

import math


def area(r):
    """
Calcula
a
área
de
um
circulo
com
raio
'r'.
"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo o iteravél. Retorna um Map Object
# coloca cada um dos dados do iteravel na função area
areas = map(area, raios)
print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resutlado, ele zera/limpa a memória.
"""

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2,... an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde o map irá mapear cada elemento dos "dados" e aplicar à função.

# O Map object: f(a1), f(a2), f(an)
