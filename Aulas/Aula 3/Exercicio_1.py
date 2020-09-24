# UERJ - 23/09/2020
# Aula 3 de Algoritmos Computacionais

"""
Exercício 1

Leia o peso (kg) e a altura (metro) de uma pessoa e 
calcule o respectivo IMC usando a seuginte fórmula:
IMC = Peso/(Altura*Altura).
De acordo com o valor obtido informe uma mensagem
a esta pessoa:

IMC menor que 18,5: peso abaixo do normal
IMC entre 18,5 e 24,9: peso normal
IMC entre 25 e 29,9: pré-obesidade
IMC entre 30 e 34,9: obesidade grau 1
IMC entre 35,5 e 39,9: obesidade grau 2
IMC a partir de 40: obesidade grau 3
"""


def calculateIMC(weight, height):

    imc = round(weight/(height**2), 2)

    phrase = "\nSeu IMC é {} e você está com".format(imc)

    if (imc < 18.5):
        return print(phrase, "peso abaixo do normal.")
    elif (imc >= 18.5) and (imc < 24.9):
        return print(phrase, "peso normal.")
    elif (imc >= 25) and (imc < 29.9):
        return print(phrase, "pré-obesidade.")
    elif (imc >= 30) and (imc < 34.9):
        return print(phrase, "obesidade grau 1.")
    elif (imc >= 35) and (imc < 39.9):
        return print(phrase, "obesidade grau 2.")
    else:
        return print(phrase, "obesidade grau 3.")


def main():
    print("\n### Calculador de IMC ###")
    while True:
        while True:
            try:
                weight = float(
                    input("\nDigite seu peso em quilogramas: "))
                height = float(
                    input("\nDigite sua altura em metros: "))

                if height <= 0 and weight <= 0:
                    raise Exception()

                break
            except:
                print("\nPor favor, digite um peso e altura válidos.")

        calculateIMC(weight, height)

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
