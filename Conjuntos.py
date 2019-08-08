"""
- Conjuntos em qualquer linguagens de programação, estamos a fazer referência à Teoria dos Conjuntos de Matemática.

-Aqui no python, os conjuntos são chamados de Sets

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acedidos via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os Conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem valor;

    # Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos
print(s)
print(type(s))

# NOTA: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))


# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = ['99', '2', '34', '23', '2', '12', '1', '44', '5', '34']
print(f'Lista:{lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 12, 1, 44, 5)
print(f'Tupla:{tupla}')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys(['99, 2, 34, 23, 2, 12, 1, 44, 5,34'], 'dict')
print(f'Dicionario:{dicionario}')

# Conjunttos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto:{conjunto}')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar num set normalmente
for valor in s:
    print(valor)


# Usos interessantes com sets

# Imaginemos que fizemos um formulário de registo de visitantes numa feira ou museu e os visitantes informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade numa lista python, já que numa lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Lisboa', 'Porto', 'Aveiro', 'Coimbra','Coimbra']

print(cidades)
print(f'Quantidades de pessoas: {len(cidades)}')

# Agora precisamos de saber quantas cidades distintas, ou seja, únicas, temos.

# O que fazer? Fazer um loop na lista..?

# Podemos utilizar o set para isso:

print(len(set(cidades)))


# Adicionando elementos num conjunto
s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Remover elementos num conjunto
s = {1, 2, 3}
print(s)
# Forma 1

s.remove(3)  # Não é indice! Informamos o valor a ser removido.

print(s)

# NOTA: Caso o valor não seja encontrado, será gerado o erro KeyError

# Forma 2

s.discard(2)
print(s)

# NOTA: Se o valor não for encontrado, nenhum erro é gerado.


# Remover elementos num conjunto
s = {1, 2, 3}
print(s)
# Forma 1

s.remove(3)  # Não é indice! Informamos o valor a ser removido.

print(s)

# NOTA: Caso o valor não seja encontrado, será gerado o erro KeyError

# Forma 2

s.discard(2)
print(s)

# NOTA: Se o valor não for encontrado, nenhum erro é gerado.


# Copiar um conjunto para outro..

# Forma 2
novo = s
novo.add(4)
print(novo)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes de curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Gui'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana'}

# Repare que alguns alunos que estudam java também estudam python.

# Precisamos de gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caracter pipe
unicos2 = estudantes_python | estudantes_java
print(unicos2)

"""

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes de curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Gui'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana'}

# Repare que alguns alunos que estudam java também estudam python.

# Precisamos de gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caracter pipe
unicos2 = estudantes_python | estudantes_java
print(unicos2)
