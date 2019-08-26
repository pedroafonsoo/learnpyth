"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

print('Geek Univeristy')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

    print(quadrado(3))
    print(quadrado()) # TypeError


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2*2*2 = 8
print(exponencial(3, 2))  # 3*3=9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3,5)) # Eleva à potência informada pelo utilizador

# OBS
# Se o utilizador passar apenas 1 argumento, este será atribuido ao parametro numero e será calculado o quadrado deste numero;
# Se o utilizador passar 2 argumentos, o primeiro será atribuido ao parãmetro numero e o segundo ao parâmetro potencia. Então
# será calculada esta potencia

print(exponencial())


# OBS : Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=5,num2=3):
    return num1+num2

print(soma(4,3))
print(soma(4))
print(soma())



# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá{nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

# Porquê utilizar parametros com valor default?
- Permite-nos ser mais flexiveis nas funções;
- Evita erros com parametros incorretos;
- Permite-nos trabalhar com exemplos mais legiveis de código;


# Quais tipos de dados podemos utilizar como valores default para parametros?
- Qualquer tipo de dados:
- Numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funcoes e etc;


# Exemplos
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...
# Variaveis globais
# Variaveis locais

instrutor = 'Geek' # Variavel global
def diz_oi():
    return f'Oi {instrutor}'

print(diz_oi())

 #OBS: Se tivermos uma variavel local com o mesmo nome de uma variável global, a local tera preferencia(será mais prioritária)

 # ATENCAO COM VARIAVEIS globais ( Se puder evitar, evite!)

total = 0


def incrementa():
    global total # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de escopo de variável

def fora():
    contador=0
    def dentro():
        nonlocal contador
        contador = contador +1
        return contador
    return dentro()


print(fora())