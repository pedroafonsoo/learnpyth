"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
# Para entender melhor o que está a acontecer devemos dividir a expressão em duas partes:

# - A primeira parte: for numero in numeros (para cada número na lista de numeros)
# - A segunda parte: numero * 10

"""

res = [numero / 2 for numero in numeros]
print(f'Res:{res}')


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)
# List Comprehension VS Loop

# Loop
numeros = [1,2,3,4,5]

numeros_dobrados=[]

for numero in numeros:
    numero_dobrados=numero*2
    numeros_dobrados.append(numero_dobrados)

print(numeros_dobrados)


"""

# Outros exemplos

# 1

nome = 'Geek University'
print([letra.upper() for letra in nome])


# 2

def TransformarMaiusculo(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia']

print([TransformarMaiusculo(amigo) for amigo in amigos])
