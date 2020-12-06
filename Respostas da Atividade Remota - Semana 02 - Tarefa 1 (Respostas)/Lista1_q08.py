"""LISTA1_Q08 Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'.
Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'.
Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela.
O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não."""

def caractere(caract):        
    if caract == "S" or caract == "N":
        print(caract)
        while True:
            num = int(input("\nDigite um número para saber o seu cubo: "))
            cubo = num**3
            print(f"O cubo do {num} é {cubo}.")
            cont = str(input("Deseja continuar?[S/N]: ")).upper().strip()
            if cont == "N":
                break
            else:
                num = int(input("\nDigite um número para saber o seu cubo: "))
                cubo = num**3
                print(f"O cubo do {num} é {cubo}.")
                cont = str(input("Deseja continuar?[S/N]: ")).upper().strip()
                if cont == "N":
                    break
  
while True:
    carac = input(f"Digite um caractere qualquer: ").upper().strip()[0]
    if carac == "S" or carac == "N":
        dado = caractere(carac)
        break
    else:
        print("Caractere inválido. Digite novamente.")
        

