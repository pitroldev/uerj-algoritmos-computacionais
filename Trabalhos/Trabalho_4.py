"""
UERJ - 13/10/2020
Trabalho 4 de Algoritimos Computacionais


Escreva um programa que leia o nome de uma pessoa e 
imprima esse nome sem espaços iniciais e finais, com 
apenas um espaço entre as partes que compõem o nome,
 colocando a primeira letra de cada parte do nome em 
 maiúscula e as demais em minúscula. 

Exemplos:
   Ler 					   Imprimir
‘  antonio   carlos bonfim ‘ : ‘Antonio Carlos Bonfim’
‘ MARIA da silva   souZA  ‘ : ‘Maria Da Silva Souza’ 

- Usar lower() e upper()
"""


def parseName(name):
    separator = " "
    splittedName = name.split()
    capitalizedWords = []

    for word in splittedName:
        captalizedWord = word[0].upper() + word[1::].lower()
        capitalizedWords.append(captalizedWord)

    parsedName = separator.join(capitalizedWords)

    return parsedName


def main():
    name = input(str("Digite um nome: "))
    print(parseName(name))


main()
