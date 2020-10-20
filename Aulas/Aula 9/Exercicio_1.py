# UERJ - 20/10/2020
# Aula 9 de Algoritmos Computacionais

"""
Exercício 1

Escreva um programa que crie uma tupla com
todos os números entre 100 e 1000 que são
divisíveis por 7 mas não são multiplos de 3.
"""


def main():
    tupla = tuple()
    for i in range(100, 1001):
        if (i % 7 == 0) and (i % 3 != 0):
            tupla = tupla + (i,)
    print(tupla)

main()
