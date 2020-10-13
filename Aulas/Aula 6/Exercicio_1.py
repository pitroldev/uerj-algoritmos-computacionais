# UERJ - 06/10/2020
# Aula 6 de Algoritmos Computacionais

"""
Exercício 1

Dada a lista [10, 2, 32, 14, 35, 46, 17, 58, 199, 19],
usando fatiamento, imprima

• 1 -> Os elementos de índices pares
• 2 -> Os elementos de índices impares
• 3 -> Os elementos entre os índices 2(inclusive) e 4 (exclusive)
• 4 -> O elemento de índice 1 e depois os elemenotos distantes
3 posições depois a partir de 1, até o final
"""


def main():

    lista = [10, 2, 32, 14, 35, 46, 17, 58, 199, 19]

    print("#1", lista[::2])
    print("#2", lista[1::2])
    print("#3", lista[2:4])
    print("#4", lista[1::4])


main()
