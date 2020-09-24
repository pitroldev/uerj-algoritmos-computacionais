# UERJ - 22/09/2020
# Aula 2 de Algoritmos Computacionais

"""
Exercício 1

Ler um número inteiro e imprimir PAR, caso o número seja par,
ou ÍMPAR, caso contrário.
"""


def main():
    while True:
        while True:
            try:
                num = int(
                    input("\nDigite um número e direi se ele é par ou impar: "))
                break
            except:
                print("\nPor favor, digite um número válido.")

        if num % 2 == 0:
            print("O número", num, "é par!")
        else:
            print("O número", num, "é ímpar!")

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
