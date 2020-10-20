# UERJ - 20/10/2020
# Aula 9 de Algoritmos Computacionais

"""
Exercício 2


"""


def main():
    tupla = tuple()
    for i in range(100, 1001):
        if (i % 7 == 0) and (i % 3 != 0):
            tupla = tupla + (i,)
    print(tupla)

main()