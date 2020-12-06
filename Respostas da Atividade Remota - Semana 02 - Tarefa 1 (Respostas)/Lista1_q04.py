"""LISTA1_Q04 Escreva um programa para ler as notas das duas avaliações de um aluno no semestre.
Faça um procedimento que receba as duas notas por parâmetro e
calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!”
somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)."""

def notas(n1, n2):
    soma = n1+n2
    media = round(soma/2, 2)
    return media
    
while True:
    try:
        nota1 = float(input(f"Digite a {1}º nota do aluno: "))
        nota2 = float(input(f"Digite a {2}º nota do aluno: "))
        media = notas(nota1, nota2)
        if media >= 6:
            print("PARABÉNS! Você foi aprovado!")
            break
        else:
            print("Nota abaixo da média desejada.")
            break
    except:
        print("Número inválido!, digite novamente")
