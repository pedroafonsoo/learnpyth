"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo ficheiro.

arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para a movimentação do cursor pelo ficheiro.
# Ela recebe um parâmetro que indica onde queremos colocar o cursor.
# Movimentando o cursor pelo ficheiro com a função seek()
arquivo.seek(0)

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())

arquivo = open('texto.txt')

# readLine() -> Função que lê o ficheiro linha a linha

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))

# readlines()

arquivo = open('texto.txt')

# readLine() -> Função que lê o ficheiro linha a linha

linhas = arquivo.readlines()

print(f'Numero de linhas do ficheiro: {len(linhas)}')

# OBS: Quando abrimos um ficheiro com a funcão open() é criada uma conexão entre o ficheiro
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o ficheiro devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um ficheiro:

1 - Abrir o ficheiro;

2 - Trabalhar o ficheiro;

3 - Fechar o ficheiro;


# 1 - Abrir o ficheiro:
arquivo = open('texto.txt')

# 2 - Trabalhar o ficheiro:
print(arquivo.read())

print(arquivo.closed) # False Verifica se o ficheiro está aberto ou fechado

# 3 - Fechar o ficheiro:
arquivo.close()

print(arquivo.closed) # True - Verifica se o ficheiro está aberto ou fechado

print(arquivo.read())

# OBS: Se tentarmos manipular o ficheiro após ter sido fechado, teremos um ValueError
# sendo necessário voltar a abrir o ficheiro ,para podermos trabalhar novamente com ele.
"""

arquivo = open('texto.txt')

# Com a funcao read() podemos limitar a quantidade de caracteres a serem lidos no ficheiro
print(arquivo.read(50)) # lê os primeiros 50 caracteres do ficheiro