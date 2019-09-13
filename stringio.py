"""
StringIO

ATENÇÃO: Para ler ou escrever dados em ficheiros do sistema operacional
o software precisa de ter permissão:
    - Permissão de Leitura -> Para ler o ficheiro.
    - Permissão de escrita -> Para escrever no ficheiro

StringIO -> Utilizado para ler e criar ficheiros em memória.
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este é apenas uma string normal'

# Podemos criar um ficheiro em memória, já com uma string inserida ou mesmo vazio para
# inserirmos texto depois

ficheiro = StringIO(mensagem)  # cria um ficheiro temporário em memória
# ficheiro = open('arquivo.txt','w')

# Agora tendo o ficheiro, podemos utilizar tudo o que já sabemos
print(ficheiro.read())

# Escrevendo outros textos 
ficheiro.write(' Outro texto.')

# Podemos inclusive movimentar o cursor
ficheiro.seek(0)
print(ficheiro.read())