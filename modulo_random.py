"""
Módulo Random e o que são módulos?

- Em Python, módulos são nada mais que outros ficheiros Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.


# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado).

import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponiveis ( Ficarão em memória). Caso saibamos as funções que precisamos de utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2


print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.



# Forma 2 - Importando uma função específica do módulo

from random import random

# No import acima, estamos a falar do módulo random, que importa a função random.

for i in range(10):
    print(random())


# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(5,10)) # 7 não é incluido.
# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai até 60


from random import choice

# choice() -> Mostra um valor aleatório entre um iterável.

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

"""

from random import shuffle

# shuffle () -> Tem a função de emparelhar dados

cartas = ['K','Q','C','A']

print(cartas)

print(cartas.pop())

