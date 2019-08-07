"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de ser Dinâmico e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
 -Possuem tamanho e tipo de dado fixo:
 Ou seja, nestas linguagens se criarmos um array do tipo int e com tamanho 5, este array
 será SEMPRE do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:

-Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

 As listas em Python são representadas por concatenação:[]

 # podemos inserir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial.O mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo valor')
print(lista1)

# inverter a lista

Forma 1:
    lista1.reverse()
    lista2.reverse()
     ou
     print(lista1[::-1])
     print(lista2[::-1])

# antes de ter o valor 42 incluido na lista
print(lista1)
lista1.append(42)
# depois de termos feito o append
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12,34,56) # Erro

# adiciona á lista 1 outra lista
lista1.append([8, 3, 1])  # coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrada a lista")
else:
    print("Não foi encontrada")

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)


#Podemos contar quantos elementos existem dentro da lista
print(len(lista5))


# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento , mas também o retorna.
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
 # OBS: Os elementos à direita deste índice serão deslocados para a esquerda.
 # OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)


#Podemos remover todos os elementos(zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos numa lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente verificar se um determinado valor existe na lista
num = 8
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print('Nao encontrei o numero 8')

# Ordenar uma lista
lista1.sort()
print(lista1)

# Contar o número de ocorrências de um valor numa lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append
"""

# Podemos converter uma string para uma lista
# OBS: Por defeito , o split separa os elementos da lista pelo espaço entre elas.
# Exemplo 1
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)
