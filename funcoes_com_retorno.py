"""
Funções com retorno


numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'Retorno de pop:{ret_pop}')
ret_pr = print(numeros)

print(f'Retorno de print:{ret_pr}')

OBS: Em Python, quando uma função não retorna nennhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: Não precsiamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções.


# Exemplo função
def quadrado_de_7():
    output = 7 * 7
    return output


# Criamos uma variàvel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno: {ret}')

# Função que retorna oi
def diz_oi():
    return 'Oi!'


print(diz_oi())

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ela sai da execução da função
2 - Podemos ter numa função, diferentes returns;
3 - Podemos, numa função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplos 1
def diz_oi():
    print('Estou a ser executada antes do retorno')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')
print(diz_oi())

# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

# coloca em cada uma das variaveis o respetivo valor
# num1, num2, num3, num4 = outra_funcao()


# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randómico entre 0 e 1
    valor = random()
    print(f' Valor={valor}')
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'
tipo_retorno= joga_moeda()


def verifica_se_impar(numero):
    if numero % 2 != 0:
        print(f'Impar={numero}')
        return True
    return False

ret=verifica_se_impar(1)
print(ret)
"""

