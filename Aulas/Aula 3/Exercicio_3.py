# UERJ - 23/09/2020
# Aula 3 de Algoritmos Computacionais

"""
Exercício 3

Leia uma temperatura em graus Celsius (C) 
e a converta para graus Fahrenheit (F).
Use a fórumla F = (9/5)*C+32
"""


def celsiusToFahrenheit(celsius):
    fahrenheit = (9/5)*celsius+32

    return fahrenheit


def main():
    print("\n### Conversor de Celsius para Fahrenheit ###")

    while True:
        while True:
            try:
                celsius = float(
                    input("\nDigite uma temperatura em graus celsius: "))

                break
            except:
                print("\nPor favor, digite uma temperatura válida.")

        fahrenheit = celsiusToFahrenheit(celsius)

        print("{}° Celsius são equivalentes a {}° Fahrenheit.".format(
            celsius, fahrenheit))

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
