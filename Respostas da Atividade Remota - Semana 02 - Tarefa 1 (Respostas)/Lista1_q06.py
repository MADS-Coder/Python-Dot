"""LISTA1_Q06 Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO."""

def poligonos(num_lado, med_lado):
    if num_lado == 3:
        P = med_lado * 3
        return P
    elif num_lado == 4:
        A = med_lado**2
        return A
    elif num_lado == 5:
        return "PENTÁGONO"
       
while True:
    try:
        num = int(input(f"Digite um numero de lados de um polígono [3, 4 ou 5]: "))
        media_lado = int(input(f"Digite a media do lado de um polígono: "))
        poli = poligonos(num, media_lado)
        if num == 3:
            print(f"O polígono é um TRIÂNGULO e o seu perímetro é {poli} cm.")
            break
        elif num == 4:
            print(f"O polígono é um QUADRADO e o sua Área é {poli} cm.")
            break
        else:
            print(f"O polígono é um {poli}.")
            break          
    except:
        print("Número inválido!, digite novamente")
