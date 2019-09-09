"""
Min e Max

max() -> Retorna o maior valor num iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # 129

tupla = (1,8,4,99,34,129)
print(max(tupla))

conjunto = {1,8,4,99,34,129}
print(max(conjunto))

dicionario = {'a':1, 'b':8, 'c':4, 'd':39,'e':34,'f':129}
print(max(dicionario.values()))



# Faça um programa que receba dois valores do utilizador e mostre o maior
val1 = int(input('Informe o primeiro valor :'))
val2 = int(input('Informe o segundo valor:'))

print(max(val1, val2))
print(max(4, 67, 54))

min() -> Retorna o menor valor num iterável ou o menor de dois ou mais elementos


# Faça um programa que receba dois valores do utilizador e mostre o menor
val1 = int(input('Informe o primeiro valor :'))
val2 = int(input('Informe o segundo valor:'))

print(min(val1, val2))


# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # Tim

print(min(nomes)) # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander

print(min(nomes, key=lambda nome: len(nome)))  # Tim

"""

musicas = [
    {"titulo": "Thunderstuck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too", "tocou": 32},
]

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

        for musica in musicas:
            if musica['tocou'] == max:
                print(musica['titulo'])
#
min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

        for musica in musicas:
            if musica['tocou'] == min:
                print(musica['titulo'])
