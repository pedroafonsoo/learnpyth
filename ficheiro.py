# -*- coding: utf-8 -*-
"""w = open("arquivo2.txt","a")

w.write("Esse é o meu arquivo")

w.close()
"""
"""
listas
minha_lista=["abacaxi","melancia","abacate"]
minha_lista2=[1,2,3,4,5]
minha_lista3=["abacaxi",2,9.89,True]
#verificar tamanho da lista
tamanho=len(minha_lista)
print(tamanho)
#adicionar o valor ao final da minha lista
minha_lista.append("limao")
print(minha_lista)

#verificar se um elemento pertence a uma lista
if 3 in minha_lista2:
    print("3 esta na lista")
else:
    print("esta fora da lista")

#removendo elementos
#remover do dois até ao final
del(minha_lista[2:])
# remover lista inteira -> del(minha_lista[:])
print(minha_lista)

"""

"""
lista=[124,345,5,72,46,6]
lista.sort()
lista.reverse()
print(lista)

lista2=["bola","abacate","dinheiro"]

lista2.sort()
print(lista2)
"""

"""
import random
random.seed(1) # forca o valor do rand a ser o mesmo
numero= random.randint(0,10)
print(numero)

lista=[6,45,9]
numero=random.choice(lista)
print(numero)
"""
"""
a=2
b=0
try:
    print(a/b)
except:
    print("Nao e permitida a divisao por 0")
    print(a/a)
"""

