#Questão 11
"""Faça uma função que recebe, por parâmetro, um valor inteiro e positivo
e retorna o número de divisores desse valor."""

def divisores(n):
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1
    print(f"\nO número de divisores de {n} é {qtd}.")
    
while True:
    try:
        num = int(input("\nDigite um número positivo maior que ZERO: "))
        if num < 0:
            print("\nO número informado é negativo. Digite novamente!")
        elif num == 0:
            print("\nO ZERO não é um número composto pois possui uma infinidade de divisores.")
            break
        else:
            divisores(num)
            break
    except:
        print("\nNúmero inválido. Digite novamente!")



