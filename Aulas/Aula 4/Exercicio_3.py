# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 3

Leia números inteiros até o usuário informar
"N" ou "n". Para cada número, dizer se ele é
múltiplo de 7.
"""


def main():
    shouldContinue = "S"

    while shouldContinue != "n" and shouldContinue != "N":

        while True:
            try:
                num = int(
                    input("\nDigite um número inteiro: "))
                break
            except:
                print("\nPor favor, digite um número inteiro válido.")

        if (num % 7 == 0):
            print("O número", num, "é múltiplo de 7!")
        else:
            print("O número", num, "não é múltiplo de 7!")

        shouldContinue = str(input("Deseja continuar? (S/N): "))


main()
