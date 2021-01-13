"""LISTA02_Q15 Ler uma lista D de 10 elementos.
Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja,
o último elemento passará a ser o primeiro,
o penúltimo será o segundo e assim por diante.
Escrever todo a lista D e todo a lista E."""


from random import randint

lista_D = []
lista_E = []

def inverso_E():
    i = 10
    for j,v  in enumerate(lista_D):
        i -= 1
        lista_E.append(lista_D[i])
    print(f"Lista normal: {lista_D}\nLista invertida: {lista_E}")

for n in range(0,10):
    D = randint(1, 50)
    lista_D.append(D)
  
inverso_E()

