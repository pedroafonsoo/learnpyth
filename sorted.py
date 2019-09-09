"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o projeto nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados
# Exemplo

numeros = [6,1,8,2]
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)


numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

"""

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]
#
print(usuarios)
# print(sorted(usuarios,key=len))

print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando por username, Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
