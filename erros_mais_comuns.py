"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:
1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que
o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError
 a)

 def funcao():
    print('Geek University')


b)
    def = 1

c)
 return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
 print(geek)

 b)
 geek()

 c)
a = 18

if a < 10:
    msg = 'É maior que 10'

    print(msg)

3 - TypeError -> Ocorre quando uma função / operação / ação é aplicada a um tipo errado.

Exemplos TypeError

a)
 print(len(5))

b) print('Geek' + [])

4 . IndexError -> Ocorre quando tentamos aceder a um elemento numa lista ou outro tipo de dado indexado utilizando
um indice inválido.

Exemplos IndexError

a)
 lista= ['Geek']
 print(lista[2])

b)
 lista = ['Geek']
 print(lista[0][10])

c)
 tupla = ('Geek')
 print(tupla[0][10])

"""



# Exemplos IndexError
lista=('Geek',)
print(lista[0][0])
