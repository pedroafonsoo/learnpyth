"""
Leitura de ficheiros

Para o conteúdo de um ficheiro em Python, utilizamos a função integrada open(),
que literalmente significa ' abrir'

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o ficheiro a ser lido. Essa função retorna
um _io_.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

#OBS: Por padrão, a função open() abre o ficheiro para leitura.Este ficheiro
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>

mode r -> Modo de Leitura. r -> read() -> ler
"""
# -*- coding: utf-8 -*-
# Exemplo

arquivo = open('texto.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um ficheiro, após a sua abertura, devemos utilizar a função read()

ret = arquivo.read()
print(ret)
print(type(ret))

print(arquivo.read())


# OBS: O Python, utiliza um recurso para trabalhar com ficheiros chamado cursor. Esse cursor,
# funciona como o cursor quando estamos a escrever.

# print(arquivo.read())

# OBS: A função read() lê todo o conteúdo de um ficheiro.
