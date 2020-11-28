#Questão 03
"""Escreva um programa para ler uma temperatura em graus Fahrenheit.
Faça uma função chamada celsius para calcular e
retornar o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5"""

def celsius(F):
    C = ((F-32)/9)*5
    return C

while True:
    try:
        temperatura = float(input("\nDigite o valor de uma temperatura em (Fahrenheit): "))
        print(f"\nA temperatura em Celsius é: {celsius(temperatura):.5f}")
        break
    except:
        print("\nValor inválido. Digite novamente!")



