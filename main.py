import aleatorio
import media

lista = aleatorio.geraListaInteiro(10)
print("Minha lista: ")
print(lista)

mediana=media.mediana(lista)
print("Mediana "+str(mediana))

media= media.media(lista)
print("A media da minha lista e "+ str(media))

moda=float(media.moda(lista))
print("A moda e"+ moda)