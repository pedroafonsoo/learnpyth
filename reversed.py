"""
Reversed

OBS: Não confunda com a função reserve() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

A sua função é inverter o iterável.

A função reversed()retorna um iterável chamado List Reverse Iterator
"""
#
# Exemplos

lista = [1,2,3,4,5]

res = reversed(lista)

print(res)

print(type(res))

# Podemos converter o elemento retornado para uma lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))