"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))
print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados recolhidos de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Media:{media}')
# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.
res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)


# filtrar apenas o tamanho do país for superior a 0, coloca na lista esse país
# res = filter(lambda pais: len(pais) > 0, paises) || res= filter(lambda pais: pais!='',paises)
# print(list(res))
# print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo a função.

"""
#
# Exemplo mais complexo

utilizadores = [{"username":"samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
                {"username":"carla", "tweets": ["Eu adoro comer"]},
                {"username":"jeff", "tweets": []},
                {"username":"bob123", "tweets": []},
                {"username":"doggo", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]}
]
print(utilizadores)
# Filtrar os utilizadores que estão inativos no Twitter

inativos = list(filter(lambda u: not u['tweets'],utilizadores))
print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é{nome}',filter(lambda nome: len(nome)<5,nomes)))
print(lista)
