"""LISTA02_Q05 Faça um programa que leia duas listas de 10 elementos numéricos cada um
e intercale os elementos deste em uma outra lista de 20 elementos."""

from random import randint

lista_A = []
lista_B = []

def intercalar(lista_a, lista_b):
    lista_C = []
    for a, b in zip(lista_a, lista_b):
        lista_C.append(a)
        lista_C.append(b)
    return lista_C

for n in range(0, 20):
    numero = randint(1, 20)
    if n < 10:
        lista_A.append(numero)
    elif n >= 10:
        lista_B.append(numero)
        
C = intercalar(lista_A, lista_B)

print(f"Lista A: {lista_A}.\n")
print(f"Lista B: {lista_B}.\n")
print(f"Unindo as listas A e B e intercalando-as fica: {C}.")


