# UERJ - 06/10/2020
# Aula 6 de Algoritmos Computacionais

"""
Exercício 4

Dada a lista [0,1,2,3,4,5,6,7,8,9], usando filtros:

• Gere a lista [5,6,7,8,9,0,1,2,3,4]
• Gere a lista [1,3,5,7,9,0,2,4,6,8]
"""


def main():

    lista = [i for i in range(10)]

    print([x for x in lista if x > 4] + [x for x in lista if x < 5])
    print([x for x in lista if x % 2 == 1] + [x for x in lista if x % 2 == 0])


main()
