"""
UERJ - 30/09/2020
Trabalho 2 de Algoritimos Computacionais


Construir um programa para ler um número inteiro positvo n
e imprimir todos os números primos na faixa de [2, n].

- Considere que sempre será digitado um número
inteiro positivo, maior ou igual a 2; ou seja, por
ora não deverá haver a preocupação com o tratamento de erro.
"""


def checkPrime(num):
    divs = 0
    i = 1

    while i < num and i*i <= num:
        if num % i == 0:
            divs += 1
        i += 1

    if divs < 2 and num != 1:
        return True
    else:
        return False


def checkRange(num):
    i = 1

    while i < num:
        i += 1
        if checkPrime(i):
            print("O número", i, "é primo.")


def main():
    num = int(input("\nEscreva um número inteiro positivo maior ou igual a 2: "))
    return checkRange(num)


main()
