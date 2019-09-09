"""
Utilizando Lambdas

Conhecidas  por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nomes, ou seja,
funções anónimas.

# Função em Python

def soma(a,b):
    return a+b

# Função em Python
def funcao(x):
    return 3 * x + 1;


print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1
print(calc(4))


# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' '+ sobrenome.strip().title()
print(nome_completo)

#   Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também

amar = lambda: 'Como não amar Python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(1))
print(duas(1,1))
print(tres(3,6,9))
# Outro exemplo

autores = ['Isaac Asimov', ' Ray Bradbury', 'Arthur C. Clarke']

print(autores)
autores.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""

# Função Quadrática
f(x) = a*x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a,b,c):
    """Retorna a função f(x) = a * x ** 2+b *c +c"""
    return lambda x: a * x ** 2 + b * x + c

teste= geradora_funcao_quadratica(2,3,-5)

print(teste(0))
print(teste(1))
print(teste(2))