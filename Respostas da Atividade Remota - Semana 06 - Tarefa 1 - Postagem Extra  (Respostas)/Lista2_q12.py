"""LISTA02_Q12 Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes.
A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas."""


gabprova = []
gabaluno = []
d = 0
#O laço abaixo solicita o gabarito das 30 questões e adiciona as mesmas
#em uma lista chamada (gabprova).
print("GABARITO DA PROVA")
for c in range(0,30):
    d += 1
    resp = input(f"Resposta da questão {d}: ")
    gabprova.append(resp)

#Solicita o nome do aluno.
nome = input("\nNome do aluno: ")

d = 0
#O laço abaixo solicita as respostas das 30 questões do aluno e adiciona as mesmas
#em uma lista chamada (gabaluno).
print("\nGABARITO DO ALUNO")
for c in range(0, 30):
    d += 1
    resposta = input(f"Resposta da questão {d}: ")
    gabaluno.append(resposta)

#O laço abaixo faz um loop 30 vezes e realiza uma condição.
#Se o valor na primeira posição da lista (gabprova) for igual ao valor
#da primeira posição da lista (gabaluno) a variável contador "a" incrementa mais 1,
#se não forem iguais a variável contador "b" incrementa mais 1.
#Onde a variável "a" representa os ACRETOS e a "b" os ERROS.
a = b = 0
for c in range(0, 30):
    if gabprova[c] == gabaluno[c]:
        a += 1
    else:
        b += 1
print(f"\nO aluno {nome} teve:\n{a} Acertos\n{b} Erros.") 

