# UERJ - 13/10/2020
# Aula 8 de Algoritmos Computacionais

"""
Exercício 3

Um palíndromo é uma cadeia que lida ao
contrário é idêntica a ela mesma ("ovo", "osso"
e "arara" são exemplos). Escreva uma função
que recebe uma cadeia como parâmetro e
retorne True caso ela seja um palíndromo.
"""


def checkPalindrome(palavra):
    if (palavra == palavra[::-1]):
        return True
    return False


def main():

    palavra = input(str("Digite uma palavra: "))
    print(palavra, "é um palíndromo?", checkPalindrome(palavra))


main()
