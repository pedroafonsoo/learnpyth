"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos o *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado numa função, coloca os valores extras informados como
entrada numa tupla. Então desde já lembre-se que as tuplas são imutaveis.

# Exemplos

def soma_todos_numeros(num1=1, num2=1, num3=1):
    return num1 + num2 + num3

# Entendendo o args
def soma_todos_numeros(*args):
    return sum(args)

    print(soma_todos_numeros())
    print(soma_todos_numeros(1))
    print(soma_todos_numeros(2, 3))
    print(soma_todos_numeros(2, 3, 4))
    print(soma_todos_numeros(3, 4, 5, 6))
"""


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho a certeza de quem voce é..'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
