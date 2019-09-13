"""
Escrever em ficheiros


# OBS: Ao abrir um ficheiro para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um ficheiro para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um ficheiro para escrita, o ficheiro é criado no sistema operacional.

Para escrevermos dados num ficheiro, após abrir o ficheiro utilizamos a função write().
Esta função recebe uma string como parâmetro.

Abrindo um ficheiro para escrita com o modo 'w', se o ficheiro não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no ficheiro anterior é perdido

# Exemplo de escrita - modo 'w' - write(escrita)

with open('novo.txt','w') as arquivo:
    arquivo.write('Escrever dados em ficheiro é muito easy.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha')


# Forma tradicional de escrita num ficheiro
arquivo = open('mais.txt','w')
arquivo.write(' Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo .close()
"""

with open('frutas.txt','w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair')
        if fruta != 'sair':
            arquivo.write(fruta)
        else:
            break;

