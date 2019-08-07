import itertools
import json


class Register:
    # lista para gravar os utilizadores
    lista_users=[]

    def _init_(self, nome, pas):
        # newid = itertools.count().next
        # self.id = next(Register.id)
        self.nome = nome
        self.pas = pas
        # or
        # self.id=next(self.id)

    def register_user(self, nome, pas):
        # criar lista vazia
        list = []
        x = 0
        tam = len(list)
        print(tam)
        if nome in list:
            print("Nome ja existe")
        else:
            list.append(nome)
            print("A registar o utilizador com nome  " + nome)
            print(list)
            novo_tam = len(list)
            print("Tamanho da lista atualizado: " + str(novo_tam))

            criaFicheiro("grava_lista.txt", list)
            #cria_ficheiro2()
            """
    for i in len(list):
        if nome in list:
            print("Nome ja existe")
        else:
            list.append(nome)
            print("A registar o utilizador  " + nome + "e password:" + pas)
"""


"""
        while (x < tam):
            print("Conteudo existente na lista:"+list[x]+"\t")
            if (nome in list[x]):
                print("Nome ja existe")
            else:
                list.append(nome)
                print("A registar o utilizador  " + nome + "e password:" + pas)
            x += 1
"""

"""
def criaFicheiro(nome_ficheiro, list2):
    file = open(nome_ficheiro, "w")
    # escreve a lista passada como argumento
    file.write(str(list2))
    file.close()
"""

# para efeito de testes -> JSON


def cria_ficheiro2():
    a = [1, 2, 3]
    with open('test.txt', 'w') as f:
        f.write(json.dumps(a))

    # Now read the file back into a Python list object
    with open('test.txt', 'r') as f:
        a = json.loads(f.read())
        print(a)


def criaFicheiro(nome_ficheiro,list2):
    with open(nome_ficheiro,'a') as f:
        for item in list2:
            f.write("%s\n" % item)
