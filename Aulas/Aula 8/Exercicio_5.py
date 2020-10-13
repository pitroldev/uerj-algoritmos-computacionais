# UERJ - 13/10/2020
# Aula 8 de Algoritmos Computacionais

"""
Exercício 5

Refaça mais uma vez esse exercício 4, mas agora
desconsiderando também espaços em branco.

- Por exemplo, a frase "Seco de raiva coloco no colo
caviar e doces" será considerada um palíndromo"
"""


def checkPalindrome(palavra):
    parsed = palavra.replace(" ", "").lower()
    if (parsed == parsed[::-1]):
        return True
    return False


def main():

    palavra = input(str("Digite uma palavra: "))
    print(palavra, "é um palíndromo?", checkPalindrome(palavra))


main()
