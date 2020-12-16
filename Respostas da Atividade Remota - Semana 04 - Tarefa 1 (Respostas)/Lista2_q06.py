"""LISTA2_Q06 Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos,
elabore um programa que calcule e exiba o faturamento que é igual a quantidade x preço.
Calcule e exiba também o faturamento total que é o somatório de todos os faturamentos,
a média dos faturamentos e quantos faturamentos estão abaixo da média."""

from random import randint, uniform

lista_qtd = []
lista_preco = []

def faturamento(Q, P):
    lista_fat = []
    for n in range(len(P)):
        F = round(Q[n]*P[n], 2)
        lista_fat.append(F)
    return lista_fat

n = -1   
while n <= 20:
    n += 1
    try:
        quantidade = randint(1,20)
        lista_qtd.append(quantidade)
        preco = round(uniform(1, 100), 2)
        lista_preco.append(preco)
    except:
        print("Número inválido. Digite novamente!")
        
F = faturamento(lista_qtd, lista_preco)

fat_total = sum(F)
media = fat_total/len(F)

print("-="*10)
print("   FATURAMENTO    ")
print("-="*10)

cont = 0
for i in range(20):
    print(f"|{lista_qtd[i]:2} x {lista_preco[i]:5}| = {F[i]:7}")
    if F[i] < media:
        cont += 1 
    
print(f"\nO faturamento total é: R$ {fat_total:.2f}")
print(f"A média dos faturamentos é: R$ {media:.2f}")
print(f"Existem {cont} faturamentos abaixo da média.")




