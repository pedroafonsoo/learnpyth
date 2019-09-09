"""
Debugando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto


# OBS: A utilização do print() para debugar código é uma má prática
def dividir(a, b):
    print(f'a={a},b={b}')
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com o PyCharm

def dividir(a, b):
    print(f'a={a},b={b}')
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4,0))


# Exemplo com o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
nome_completo = nome + ''+ sobrenome
pdb.set_trace()

"""


# Exemplo com o PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variavél)
# c (continua a execução - finaliza o debugging)
#
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo+ 'faz o curso ' + curso
print(final)

# Porquê utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao invés de colocarmos o import do pdb no inicio do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.