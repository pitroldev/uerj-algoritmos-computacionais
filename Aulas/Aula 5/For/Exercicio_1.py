# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 1

Leia um valor n inteiro positivo e imprima
todos os valores de 1 a n seguidos dos seus
respectivos quadrados.
"""


def squareNum(n):
    for i in range(1, n+1):
        print("O número", i, "ao quadrado é", i**2)


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise Exception()

            break
        except:
            print("\nPor favor, digite um número inteiro positivo válido.")

    squareNum(num)


main()
