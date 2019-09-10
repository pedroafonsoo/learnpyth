"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma:

Se a gente pensar num programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se pensarmos numa função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função
def quadrado(numero):
    return numero * numero


# for i in range(3):
#   retorno = quadrado_de_7(2)
#  print(retorno)

print(quadrado(2))
print(quadrado(3))
print(quadrado(4))

def tipo_operacao(operacao, numero):
    if operacao == 'quadrado':
        retorno = numero * numero
    elif operacao == 'cubo':
        retorno = numero * numero * numero
    print(retorno)
    return retorno

ret = tipo_operacao('quadrado', 2)
#
def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'


print(nome_completo('Angelina', 'Jolie'))

# A diferença entre parametros e argumentos

# Parametros sao variaveis declaradas na definicao de uma funcao;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(nome, sobrenome))
print(nome_completo(nome='Angelina',sobrenome='Jolie'))
"""


# Argumentos nomeados ( Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1,2,3,4,5,6,7]
print(soma_impares(lista))