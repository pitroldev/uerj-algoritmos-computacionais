# UERJ - 23/09/2020
# Aula 3 de Algoritmos Computacionais

"""
Exercício 2

Leia uma temperatura em graus Fahrenheit (F) 
e a converta para graus Celsius (C).
Use a fórumla C = (5/9)*(F-32)
"""


def fahrenheitToCelsius(fahrenheit):
    celsius = (5/9)*(fahrenheit-32)

    return celsius


def main():
    print("\n### Conversor de Fahrenheit para Celsius ###")

    while True:
        while True:
            try:
                fahrenheit = float(
                    input("\nDigite uma temperatura em graus fahrenheit: "))

                break
            except:
                print("\nPor favor, digite uma temperatura válida.")

        celsius = fahrenheitToCelsius(fahrenheit)

        print("{}° Fahrenheit são equivalentes a {}° Celsius.".format(
            fahrenheit, celsius))

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
