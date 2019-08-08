"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

# Iterar sobre dicionários
for chave in receita:
    print(chave)

    for chave in receita:
        print(receita[chave])

# Acedendo a chaves

print(receita.keys())

for chave in receita.keys():
print(receita[chave])

# Acedendo aos valores
print(receita.keys())

for valor in receita.values():
    print(valor)

    # Desempacotamento de dicionários
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
