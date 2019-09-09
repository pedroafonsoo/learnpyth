"""
Zip

zip() -> Cria um iterável (Zip object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.


"""

# Exemplos
lista1 = [1,2,3]
lista2= [4,5,6]

zip1 = zip(lista1,lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla ou dicionario

print(list(zip1))

print(tuple(zip1))

print(dict(zip1))

zip1 = zip(lista1,lista2, 'abc')
print(tuple(zip1))

zip1= zip(lista1,lista2, 'abc')
print(set(zip1))

zip1= zip(lista1,lista2)
print(dict(zip1))


# OBS: O zip() utiliza como parametro o menor tamanho num iteravel. Isso significa que se estiver
# trabalhando com iteraveis de tamanhos diferentes, irá parar quandos os elementos do menor
# itervael acabar

lista3 = [7,8,9,10,11]