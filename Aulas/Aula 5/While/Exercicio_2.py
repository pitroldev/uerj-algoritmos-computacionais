# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 2

Leia um valor n inteiro positivo e calcule o
enésimo termo da série de Fibonacci.
"""


def Fibonacci(n):
    first = 0
    second = 0
    i = 0
    while (n > i):
        second = first + second
        first = second - first
        i += 1

        if (second == 0):
            second = second + 1

    return first


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise Exception()

            break
        except:
            print("\nPor favor, digite um número inteiro positivo válido.")

    print("O termo", num, "da série de fibonacci é", Fibonacci(num))


main()
