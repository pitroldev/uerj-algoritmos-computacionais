# UERJ - 22/09/2020
# Aula 2 de Algoritmos Computacionais

"""
Exercício 3

Ler três números inteiros e imprimir o maior deles.
"""


def higherNumber(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


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

        print("\nO maior deles é o número", higherNumber(a, b, c))

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
