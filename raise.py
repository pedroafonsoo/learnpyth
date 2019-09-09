"""
Levantando os próprios erros com raise

raise -> Lança excepções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias excepções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')


raise ValueError('Valor incorreto')



# Exemplo real

def colore(texto, cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisar ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

    colore('Geek', 'preto')


OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""


