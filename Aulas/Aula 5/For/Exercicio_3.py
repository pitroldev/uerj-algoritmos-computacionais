# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 3

Leia um valor n inteiro positivo e imprima
todos os valores de n a 1 seguidos dos seus
respectivos quadrados e cubos.
"""


def expNum(n):
    for i in range(n, 0, -1):
        print("O número", i, "ao cubo é", i**3, "e ao quadrado é", i**2)


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise Exception()

            break
        except:
            print("\nPor favor, digite um número inteiro positivo válido.")

    expNum(num)


main()
