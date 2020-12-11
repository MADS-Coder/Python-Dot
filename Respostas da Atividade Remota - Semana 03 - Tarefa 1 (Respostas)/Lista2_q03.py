"""LISTA02_Q03 Faça um programa que dada uma seqüência de n números,
imprimi-la na ordem inversa à da leitura."""


lista = []
while True:
    try:
        num = int(input("Digite um numero [999] para: "))
        if num == 999:
            break
        else: lista.append(num)
    except:
        print("Dados inválidos!. Digite apenas números.")

invertido = lista[::-1]
print(f"A ordem invertida é: {invertido}.")
