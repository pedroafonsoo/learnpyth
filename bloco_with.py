"""
O bloco with
Passos para se trabalhar com ficheiros

# 1 - Abrimos o ficheiro
# 2 - Manipulamos o ficheiro
# 3 - Fechamos o ficheiro

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

arquivo = open('texto.txt')

"""

# O bloco with - Forma em Python de manipular ficheiros
# programadores profissionais optam por trabalhor com o with.

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

print(arquivo.closed)




