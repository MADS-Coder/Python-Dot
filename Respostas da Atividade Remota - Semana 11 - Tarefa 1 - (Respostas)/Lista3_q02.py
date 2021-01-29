'''Lista3_q02 Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra.
Se a letra for A o procedimento calcula a média aritmética das notas do aluno,
se for P, a sua média ponderada (pesos: 5, 3 e 2).
A função deve retornar a média calculada.'''


def media(nota, letra):
    if letra == 'A':
       média = sum(nota)/3
    elif letra == 'P':
        total_peso = 5+3+2
        média = (nota[0]*5 + nota[1]*3 + nota[2]*2)/total_peso
    return f"A média é: {média:.2f}"
   
notas = []
for n in range(1,4):
    nota = float(input(f"Digite a {n}º nota do aluno: "))
    notas.append(nota)
letras = input("\n[A] - Média Aritmética\n[P] - Média Ponderada\nDigita uma letra para saber a média desejada: ").upper()
print(media(notas, letras))
