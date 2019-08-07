"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla

"""

# CUIDADO 1: As tuplas são representadas por (), mas veja:
from builtins import type

"""
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type((tupla1)))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

tupla3 = 3,
print(tupla3)
print(type(tupla3))

# Soma*, Valor Máximo*, Valor Minimo* e Tamanho
tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)
    
    # contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e','a','b')

print(tupla.count('b'))
    
"""

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos numa coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro')

print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# iterar com o while
i = 0

while i < len(meses):
    print(meses)
    i = i + 1

    # verificamos qual o indice de um elemento que está na tupla
    print(meses.index('Julho'))
    # OBS: Caso o elemento não exista, será gerado ValueError.

    # Slicing

    # tupla[inicio:fim:passo]

    print(meses[5:9:1])

# Razão para utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam o nosso código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz segurança para o código


#Para copiar uma tupla para outra

tupla=(1,2,3)
print(tupla)

nova=tupla
print(nova)
print(tupla)

outra=(4,5,6)

nova=nova+outra

print(nova)
print(tupla)