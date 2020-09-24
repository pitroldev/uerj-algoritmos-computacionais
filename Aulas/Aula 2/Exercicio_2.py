# UERJ - 22/09/2020
# Aula 2 de Algoritmos Computacionais

"""
Exercício 2

Ler um número inteiro e imprimir True, caso o número seja par,
ou False, caso contrário.
"""


def main():
    while True:
        while True:
            try:
                num = int(input("\nDigite um número: "))
                break
            except:
                print("\nPor favor, digite um número válido.")

        print(num, "é par?", num % 2 == 0)

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
