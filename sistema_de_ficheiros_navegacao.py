"""
Sistema de ficheiros e navegação

Para fazer uso de manipulação de ficheiros do sistema operacional, precisamos importar
e fazer uso dos módulos

os -> Operating system - Sistema Operacional
"""

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd()) # /media/sf_Documents/vm/PyCharmProjects/guppe

# Podemos vericiar se um diretório é absoluto ou relativo

print(os.path.isabs(('C:\Users\carlo\PycharmProjects'))) # True

# Fazer o import
import os
# OBS para utilizadores windows
# Se infelizmente, estiver a utilizar um computador com Windows,
# terá que ter cuidado ao verificar diretórios.z