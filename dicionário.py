"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são reprsentados por chaves{}
print(type{}))

OBS: Sobre dicionários
    - CHAVE e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


    # Criação de dicionários

# Forma 1 (Mais comum)

# separação entre chave e valor é feito com ":"
    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}


    print(paises)
    print(type(paises))

# Forma 2 (Menos comum)
    paises = dict(br='Brasil', pt='Portugal')
    print(paises)
    print(type(paises))

"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acedendo via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))
