# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 7

Leia um valor n inteiro positivo e calcule a
soma dos n primeiros termos da série de Fibonacci.
"""


def sumFibonacci(n):
    total = 0
    first = 0
    second = 0
    for i in range(n):
        second = first + second
        first = second - first

        if (second == 0):
            second = second + 1

        total += first
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

    print("A soma dos", num,
          "primeiros termos da série de Fibonacci é", sumFibonacci(num))


main()
