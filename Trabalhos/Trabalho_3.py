"""
UERJ - 06/10/2020
Trabalho 3 de Algoritimos Computacionais


Use o trabalho anterior para gerar uma lista de números primos até 1000. 
Esses números deverão formar uma lista, LPrimos. A seguir, faça uma 
repetição que permita ao usuário consultar números, entre 2 e 1000, 
verificando em LPrimos se ele é primo ou não. 

- Por ora não deverá haver a preocupação com o tratamento de erro.
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


def genPrimes(num):
    i = 1
    primesList = []
    while i < num:
        i += 1
        if checkPrime(i):
            primesList.append(i)
    return primesList


def main():
    LPrimos = genPrimes(1000)

    shouldContinue = ""
    while shouldContinue != "F" and shouldContinue != "f":
        num = int(input(
            "\nEscreva um número inteiro positivo maior ou igual a 2 e menor que 1000: "))

        if num in LPrimos:
            print(num, "é um número primo.")
        else:
            print(num, "NÃO é um número primo.")

        shouldContinue = str(
            input("\nDigite F para terminar ou aperte enter para continuar: "))


main()
