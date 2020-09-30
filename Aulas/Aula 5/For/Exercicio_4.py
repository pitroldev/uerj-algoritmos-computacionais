# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 4

Leia um valor n inteiro positivo e calcule o
fatorial de n.
"""


def fatorial(n):
    total = 1
    for i in range(1, n+1, 1):
        total = total * i
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

    print("O fatorial de", num, "é", fatorial(num))


main()
