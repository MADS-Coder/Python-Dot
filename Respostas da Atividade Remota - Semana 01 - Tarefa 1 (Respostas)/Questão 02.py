#Questão 02
"""Escreva um programa que leia o raio de um círculo e faça duas funções:
uma função chamada área que calcula e retorna a área do círculo e
outra função chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r^2; Perímetro = PI * 2 * r"""


def area(r):
    area = 3.14 * r**2
    return area

def perimetro(r):
    perimetro = 3.14 * 2 * r
    return perimetro

while True:
    try:
        raio = int(input("\nDigite o raio do círculo: "))
        print(f"\nA área do círculo é: {area(raio)}")
        print(f"\nO perímetro do círculo é: {perimetro(raio)}")
        break
    except:
        print("\nValor inválido: Digite novamente!")



