# UERJ - 22/09/2020
# Aula 2 de Algoritmos Computacionais

"""
Exercício 4

Ler três números inteiros e imprimi-los em ordem crescente.
"""


def orderAsc(a, b, c):
    if a > b:
        if b > c:
            return [c, b, a]
        else:
            if a > c:
                return [b, c, a]
            else:
                return [b, a, c]
    else:
        if b > c:
            if a > c:
                return [c, a, b]
            else:
                return [a, c, b]
        else:
            return [a, b, c]


def main():
    while True:
        while True:
            try:
                a = int(input("\nDigite um número: "))
                b = int(input("Digite um segundo número: "))
                c = int(input("Digite um terceiro número: "))
                break
            except:
                print("\nPor favor, digite números válidos.")

        print("\nOs números a seguir estão ordenados de forma crescente:",
              orderAsc(a, b, c))

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
