# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 1

Escreva um programa para ler um
valor n inteiro positivo e calcular a soma de 1 a n.
"""


def totalSum(num):
    total = 0
    i = 0
    while i <= num:
        total += i
        i += 1
    return total


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise Exception()

            break
        except:
            print("\nPor favor, digite um número inteiro positivo válido.")

    print("A soma de 1 até {} é igual a {}.".format(num, totalSum(num)))


main()
