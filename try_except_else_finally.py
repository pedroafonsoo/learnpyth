"""
Try / Except / Else /Finally

Dica de quando e onde tratar código:

TODA ENTRADA  DEVE SER TRATADA!

OBS: A função do utilizador é DESTRUIR o sistema.
# Else -> É executado só se não ocorrer o erro (except)
num = 0
try:
    num = int(input("Introduza um numero:"))
except ValueError:
    print('valor incorreto')
else:
    print(f'Voce digitou {num}')

    # Finally
try:
    num = int(input('Introduza um numero:'))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Voce digitou {num}')
finally:
    print('Depois do bloco try/except')

# OBS: O bloco finally é SEMPRE executado. Independentemente se houver excepção ou não.

# O finally, geralmente é utilizado para fechar ou desalocar recursos.

num1 = int(input('Informe o primeiro numero'))

try:
    num2 = int(input('Informe o segundo numero:'))
except ValueError:
    print(f'O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

    # Exemplo mais complexo - Genérico
# OBS: Você é responsavel pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'


num1 = input('Informe o primeiro número:')
num2 = input('Informe o segundo numero:')
"""


# Exemplo mais complexo - Semi-Genérico
# OBS: Você é responsavel pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número:')
num2 = input('Informe o segundo numero:')

print(dividir(num1, num2))
