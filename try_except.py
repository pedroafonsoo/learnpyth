"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo
assim que o programa pare de funcionar e o utilizador receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    // o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE
tratar de forma específica.

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except NameError:
    print('Voce esta utilizando uma funcao inexistente')
#
"""

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except NameError:
    print('Voce esta utilizando uma funcao inexistente')


