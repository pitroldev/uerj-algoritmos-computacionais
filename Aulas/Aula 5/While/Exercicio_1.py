# UERJ - 30/09/2020
# Aula 5 de Algoritmos Computacionais

"""
Exercício 1

Leia um valor n inteiro positivo e calcule o
fatorial de n.
"""


def fatorial(n):
    total = 1
    i = 1
    while (n >= i):
        total = total * i
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

    print("O fatorial de", num, "é", fatorial(num))


main()
