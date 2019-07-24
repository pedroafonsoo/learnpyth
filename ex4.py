# ordenar a lista com 3 elementos
lista = [3, 2, 1]

for i in range(len(lista)):
    menor = i
    for j in range(i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

    print(lista)

"""
#CONTROL + SHIFT + ALT+ L PARA REFORMATAR O CODIGO
num1 = int(input("Introduza o 1 numero:\n"))
num2 = int(input("Introduza o 2 numero:\n"))
sinal = input("Introduza o sinal que pretende:\n")
if (sinal == '+'):
    res = num1 + num2
elif (sinal == '-'):
    res = num1 - num2
elif (sinal == '*'):
    res = num1 * num2
elif (sinal == '/'):
    res = num1 / num2
else:
    print("Sinal invalido")

print(res)
"""
