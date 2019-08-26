"""
Listas Aninhadas(Nested lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamados de arrays:
    - Unidimensionais (Arrays/Vetores):
    - Multidimensionais (Matrizes):

Em Python nós temos as listas

numeros = [1,'b', 3.234, True, 5]


# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 * 3

print(listas)

print(type(listas))

# Como fazemos para aceder os dados?
print(listas[0][1])  # 2
print(listas[2][1])  # 8

# Iterar com loops numa lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# Utilizando List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# Outros exemplos

# Gerando um tabuleiro / matriz 3*3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
