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



    # Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acedendo via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))


# Caso o get não encontra o objeto com a chave informada será retornado o valor None
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Nao encontrei o país')


# Podemos verificar se determinada chave se encontra num dicionário


    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
    print(russia)



# Podemos utilizar qualquer tipo de dado (int, float, string, boolean) , inclusive lista, tupla dicionário, como chaves
# de dicionários.

localidades= {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128,74.0060): 'Escritório em Nova York'

}

print(localidades)



# Adicionar elementos num dicionário
receita = {'jan': 100, 'fev':120,'mar':300}
print(receita)
print(type(receita))

#Forma 1
receita['abr']= 350
print (receita)

# Forma 2
novo_dado={'mai':500}

receita.update(novo_dado)
print(receita)


receita = {'jan': 100, 'fev':120,'mar':300}
print(receita)
# Forma 1 - remove o último elemento da lista
ret = receita.pop('mar')
print(ret)

# após ter sido removido o ultimo elemento da lista
print(receita)

# OBS 1: Aqui precisamos SEMPRE de informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)

#Se a chave não existir , será gerado um KeyError
#OBS: Neste caso o valor removido não é retornado.


# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

# Copiar um dicionário para o outro

# Forma 1
novo= d.copy()
print(novo)

novo['d'] = 4

print(d)
print(novo)


# Métodos de dicionários

d= dict(a=1, b=2, c=3)
print(d)
print(type(d))


# Forma 2 #Shallow Copy
novo = d
print(novo)
novo['d']=4
print(d)
print(novo)


"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# o método fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado
# nao repete o ultimo "t" e o "e" porque não repete a mesma chave
veja = {}.fromkeys('teste', 'valor')
print(veja)
