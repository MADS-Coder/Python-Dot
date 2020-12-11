"""LISTA02_Q07 Dada uma lista contendo 10 elementos numéricos,
elabore um programa que verifique se um outro valor dado pertence ou não à lista."""

from random import randint


lista_numerica = []

def validacao(N):
    if N in lista_numerica:
        return "Pertence"
    else:
        return "Não pertence"
    
for i in range(0, 10):
    numeros = randint(1, 10)
    lista_numerica.append(numeros)

while True:
    try:
        num = int(input("\nDigite um número para saber se está na lista: "))
        resp = str(input("Quer continuar?[S/N]: ")).upper().strip()[0]
        lista = validacao(num)
        if resp == "N":
            print(f"\nO número {num} {lista} a lista.")
            break
        else:
            print(f"\nO número {num} {lista} a lista.")
        
    except:
        print("Número inválido. Digite novamente!")
