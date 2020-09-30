# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 2

Leia um valor n inteiro positivo e imprima
todos os valores de 1 a n seguidos dos seus
respectivos cubos.
"""


def cubeNum(n):
    for i in range(1, n+1):
        print("O número", i, "ao cubo é", i**3)


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise Exception()

            break
        except:
            print("\nPor favor, digite um número inteiro positivo válido.")

    cubeNum(num)


main()
