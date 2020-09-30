# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 7

Voltando ao Exercício 1, como permitir
que o usuário possa fazer diversas somas?
"""


def totalSum(num):
    total = 0
    i = 0
    while i <= num:
        total += i
        i += 1
    return total


def main():
    num = 1

    while num > 0:
        while True:
            try:
                num = int(
                    input("Digite o número final ou digite 0 para terminar: "))
                if (num < 0):
                    raise Exception()
                break
            except:
                print("\nPor favor, digite um número inteiro positivo válido.")

        if (num != 0):
            print("A soma total dos números de 1 até {} é de {}.".format(
                num, totalSum(num)))


main()
