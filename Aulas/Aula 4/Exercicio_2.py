# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 2

Leia números inteiros até o usuário informar 0,
para cada número, dizer se ele é par ou impar.
"""


def main():
    num = 1
    while num != 0:

        while True:
            try:
                num = int(
                    input("\nDigite um número inteiro ou digite 0 para parar: "))
                break
            except:
                print("\nPor favor, digite um número inteiro válido.")

        if (num % 2 == 0) and (num != 0):
            print("O número", num, "é par!")
        elif (num % 2 == 1):
            print("O número", num, "é impar!")


main()
