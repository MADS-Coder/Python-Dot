#Questão 05
"""Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso
ideal que receba a altura e o sexo via parâmetro e que calcule e
retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima)."""


def peso_ideal(a, s):
    if a == 2:
        homens = (72.7*a)
        return homens
    else:
        mulheres = (62.1*a) - 44.7
        return mulheres

while True:
    try:
        altura = float(input("\nInforme a altura: "))
        sexo = input("\nInforme o sexo: ").upper().strip()[0]
        if sexo == 'M':
            a = 2
            print(f"\nO peso ideal de acordo com os dados informados é: {peso_ideal(altura, sexo)}")
            break
        elif sexo == 'F':
            a = 1
            print(f"\nO peso ideal de acordo com os dados informados é: {peso_ideal(altura, sexo)}")
            break
    except:
        print("\nDados inválidos. Digite novamente")
        




