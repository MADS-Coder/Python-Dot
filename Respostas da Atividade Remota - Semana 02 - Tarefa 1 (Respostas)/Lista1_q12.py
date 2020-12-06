"""LISTA1_Q12 Escreva uma função que recebe, por parâmetro,
um valor inteiro e positivo e retorna o somatório desse valor."""

def somatorio(num):
    soma = 0
    for i in range(0, num+1):
        soma += i
    return soma

def main():
    numero = int(input(f"Digite um número qualquer para saber seu somatório: "))
    soma = somatorio(numero)
    print(f"O somatório de {numero} é {soma}.")

if __name__=="__main__":
    main()
        

