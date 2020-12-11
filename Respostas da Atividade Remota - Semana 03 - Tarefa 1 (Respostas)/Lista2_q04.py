"""LISTA02_Q04 Faça um programa que grave uma lista com 15 posições,
calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra."""

lista = []
mai = men = 0
for n in range(0, 15):
    num = int(input("Digite um número: "))
    lista.append(num)
    if n == 0:
        mai = men = num
    else:
        if num > mai:
            mai = num
        if num < men:
            men = num
            
for i, v in enumerate(lista):
    if lista[i] == mai:
        print(f"O maior número da lista {lista} é: {mai}, e está na posição {i}.")
for i, v in enumerate(lista):
    if lista[i] == men:
        print(f"O menor número da lista {lista} é: {men}, e está na posição {i}.")
