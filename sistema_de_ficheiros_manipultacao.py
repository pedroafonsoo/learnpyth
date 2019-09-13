"""
Sistema de arquivos - Manipulação

# Ficheiro
# Descobrindo se um ficheiro ou diretório existe
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True


# Diretório

# Pathts relativos
print(os.path.exist('geek')) #True
print(os.path.exist('geek/university')) #True
print(os.path.exist('geek/university/../geek3.py')) #False
print(os.path.exist('outro')) #False


#Criar ficheiros

# Forma 1
open('arquivo.teste.txt','w').close()

# Forma 2
open('arquivo.teste2.txt','a').close()

# Forma 3
with open('arquivo.teste3.txt','w') as arquivo:
    pass




# Criar ficheiros

os.mknod('arquivo-teste4.txt')

os.mknod('C:\\Users\\carlo\\PycharmProjects\\learnpyth')

# OBS: Se estivermos a utilizar o MacOs, pode haver um erro de permisstion Error


import os

# Criar diretórios

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('templates/geek/university')

# OBS: A funçäo mkdir() cria um diretório se näo existir. Caso exista, teremos FileExistsError

os.mkdir('/etc/templates')

# OBS: Se näo tivermos permissäo para criar o diretório teremos um PermissionError

import os
try:
    # Criar multi-diretórios (árvore de diretórios)
    # Se já existir teremos um FileExistsError
    os.makedirs('templates/geek/university')
except FileExistsError as err:
    print(err)

    os.makedirs('templates2/novo2/outro2',exist_ok=True)

    # Renomear ficheiros e diretorias

# os.rename('templates2','geek2')

# OBS: Se a diretoria näo existir teremos um FileNotFoundError

# OBS: Se a diretoria que queremos renomear nao estiver vazio, teremos um OSError


# Ficheiros
os.rename('geek2/novo2/outro2/teste.txt','geek2/novo2/outro2/geek.txt')

os.rename('frutas.txt','cesta.txt')


# ATENÇAO! Tomar cuidado com os comandos de delete. Ao eliminarmos um ficheiro ou diretoria,
# eles nao vao para o lixo.

os.remove('geek')

# OBS: Se estivermos no Windoes e o ficheiro que eliminarmos estiver em uso, teremos um erro.

# OBS: Caso o ficheiro nao exista, teremos o FileNotFoundError

# OBS: Se informarmos uma diretoria ao invés  de um ficheiro, teremos um IsADirectory

# Remover diretorias vazias
os.rmdir('templates')

# OBS: Se a diretoria tiver qualquer conteúdo teremos um OSError

# OBS: Se a diretoria nao existir teremos um FileNotFoundError
"""

import os

# Remover uma árvore de diretorias:
for arquivo in os.scandir('geek2'):
    print(f'-{arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)
