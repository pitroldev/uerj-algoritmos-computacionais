# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 3

Leia um valor n inteiro positivo e imprima os
n primeiros termos da série de Fibonacci.
"""


def Fibonacci(n):
    first = 0
    second = 0
    i = 0
    while (n > i):
        second = first + second
        first = second - first
        i += 1

        print("O termo", i, "da série de Fibonacci é", first)

        if (second == 0):
            second = second + 1


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise Exception()

            break
        except:
            print("\nPor favor, digite um número inteiro positivo válido.")

    Fibonacci(num)


main()
