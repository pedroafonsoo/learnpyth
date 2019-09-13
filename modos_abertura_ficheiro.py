"""
Modos de Abertura de Ficheiro

r -> Abre para leitura - padrão
w -> Abre para escrita -  Sobrescreve caso o ficheiro já exista
x -> Abre para escrita só se o ficheiro não existir.
+ -> Abre para o modo de atualização: Leitura e Escrita.
a -> Abre para escrita, adicionando o conteudo ao final do ficheiro.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controlo do cursor)

#OBS: Abrindo no modo 'a' -> append, se o ficheiro não existir, será criado. Caso exista, o novo conteúdo
será adicionado ao final.

https://docs.python.org/3/library/functions.html#open


#Exemplo x
try:
    with open('university.txt','x') as ficheiro:
        ficheiro.write('Teste de conteudo.\n')
except FileExistsError:
        print('Arquivo ja existe')

# Exemplo a ( No modo a , caso o ficheiro exista o novo conteudo sera adicionado
sempre no final do ficheiro. Como este tipo de modo, não conseguimos controlar o cursor.
with open('frutas.txt', 'x') as ficheiro:
    while True:
        fruta = input('Informe uma fruta ou sair')
        if fruta != 'sair':
            ficheiro.write(fruta)
            ficheiro.write('\n')
        else:
            break


# Exemplo r+
with open('outro.txt','r+') as arquivo:
    arquivo.seek(0) # move o cursor para o inicio do ficheiro
    arquivo.write('Noix\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')
"""

