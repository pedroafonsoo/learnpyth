"""
** kwargs

Poderiamos chamar este parametro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
numa tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras num dicionário.


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernando='azul')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))


# Nas nossas funcoes, podemos ter (NESTA ORDEM):
- Parametros obrigatorios:
 - *args
 - Parametros default(nao obrigatorios):
- ** kwargs
"""



