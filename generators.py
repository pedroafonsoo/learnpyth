"""

Generators

Em aulas anteriores nós estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

    Não vimos:
    - Tuple Comprehension....porque elas se chamam Genearators

nomes = ['Carlos', 'Camila' , 'Carla' , 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes])

# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res=[nome[0]=='C' for nome in nomes]
print(type(res))
print(res)

# Generator
res= (nome[0]=='C' for nome in nomes)
print(type(res))
print(res)

#Qual a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memoria. Quanto maior a string, mais espaço ocupa.

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

"""

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dicionary Comprehension
dict_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension : {list_comp}')
print(f'Set Comprehension : {set_comp}')
print(f'Dict Comprehension : {dict_comp}')
print(f'Generator Expression : {gen}')
