"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

""""
nome = 'Geek Univeristy'

print(nome)
print(type(nome))

nome = "'Gina's Bar"
print(nome)
print(type(nome))

nome = "Angelina Jolie"
print(nome)
print(type(nome))


print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(nome)
print(type(nome))

# lower tudo minusculo, upper tudo maiusculo
nome = 'Geek Univeristy'
print(nome.lower())

# split -> Transforma cada palavra numa lista de strings
nome = 'Geek University'
print(nome.split())
# print a primeira parte da palavra
print(nome[0:4])
# print a segunda parte da palavra
print(nome[5:15])

# acesso a primeira palavra da lista
# [ 0, 1]
# ['Geek', 'University']
print(nome.split()[0])

# acesso a segunda palavra da lista
print(nome.split()[1])


"""

"""
Escopo de variàveis:

Dois casos de escopo:

1-Variavéis globais:
    - Variavéis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
    
2-Variaveis locais:
    -Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo 
    está limitado ao bloco onde foi declarada.
    
    Para declarar variaveis em Python fazemos:
    
    nome_da_variavel= valor_da_variavel

"""

"""
    Estruturas lógicas: and(e), or (ou), not(não), is(é)
    
Operadores unários:
    -not, is
Operadores binários:
    -and, or
    
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True -> false, se for false -> True
"""
ativo = True
logado = True
"""
if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, verifique o seu e-mail')
"""
if not ativo:
    print('Você precisa ativar sua conta. Por favor verifique o seu e-mail')
else:
    print('Bem-vindo usuário')

    nome = "Geek University"
    for i, v in enumerate(nome):
        print(nome[i])

    # Quando não precisamos de um valor, podemos descartà-lo utilizando um unerline(_)
    # enumerate traz dois valores (0,'G') ..
    for _, letra in enumerate(nome):
        print(letra)

        for valor in enumerate(nome):
            print(valor)


