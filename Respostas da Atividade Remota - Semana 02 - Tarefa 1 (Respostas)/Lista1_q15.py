"""LISTA1_Q15 Escreva uma função que recebe por parâmetro
um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)"""



def S(num):    
    aux1 = 2
    aux2 = 4.0
    for i in range(aux1-1, num):
        aux1 = (i**2)+1
        aux2 = i + 3
        print(f"{aux1}/{aux2}")
    

numero = int(input("Digite um numero: "))
while numero < 0:
    numero = int(input("Digite um valor positivo: "))
res = S(numero)
