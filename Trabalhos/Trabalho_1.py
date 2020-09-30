"""
UERJ - 22/09/2020
Trabalho 1 de Algoritimos Computacionais


Construir um programa que leia três valores numéricos inteiros e 
verifique se eles podem ser valores dos lados de um triângulo. 
Caso seja possível, testar qual o tipo de triângulo pode ser 
formado (equilátero, isósceles ou escaleno) e emitir 
uma mensagem apropriada. Caso não seja possível, 
informar esta ocorrência através de uma mensagem.
"""


def identifyTriangle(a, b, c):

    # Verifica se todos os números são positivos não-nulos.
    if (a <= 0) and (b <= 0) and (c <= 0):
        return print("\nNão é possível formar um triângulo com os números {}, {} e {}.".format(a, b, c))

    # Verifica se é possível formar um triângulo.
    if (a + b > c) and (a + c > b) and (b + c > a):

        phrase = "\n{}, {} e {} formam um triângulo".format(a, b, c)

        # Indentifica o tipo do triângulo formado.
        if a == b and b == c:
            return print(phrase, "equilátero.")
        elif a == b or b == c or c == a:
            return print(phrase, "isósceles.")
        else:
            return print(phrase, "escaleno.")

    else:
        return print("\nNão é possível formar um triângulo com os números {}, {} e {}.".format(a, b, c))


def main():
    while True:

        # Lê três números e verifica se são números inteiros válidos.
        while True:
            try:
                a = int(input("\nDigite um número inteiro: "))
                b = int(input("Digite um segundo número inteiro: "))
                c = int(input("Digite um terceiro número inteiro: "))
                break
            except:
                print("\nPor favor, digite números inteiros válidos.")

        identifyTriangle(a, b, c)

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
