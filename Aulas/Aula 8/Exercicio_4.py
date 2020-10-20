# UERJ - 13/10/2020
# Aula 8 de Algoritmos Computacionais

"""
Exercício 4

Refaça o exercício 3 sobre palíndromo, mas
agora considerando a existencia de maiúsculas
e minúsculas na cadeia dada. Isto é, considere 
"Ovo" como palíndromo
"""


def checkPalindrome(palavra):
    if (palavra.lower() == palavra[::-1].lower()):
        return True
    return False


def main():

    palavra = str(input("Digite uma palavra: "))
    print(palavra, "é um palíndromo?", checkPalindrome(palavra))


main()
