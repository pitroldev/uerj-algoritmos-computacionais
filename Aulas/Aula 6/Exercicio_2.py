# UERJ - 06/10/2020
# Aula 6 de Algoritmos Computacionais

"""
Exercício 2

Gere uma lista com 100 números de 0 a 99,
usando range() e, com valores negativos no
fatiamento, crie um programa que imprima:

• 1 -> O último elemento da lista original e depois,
decrescendo, os elementos distantes 3 posições a
partir do final até o início;

• 2 -> Os elementos entre o índice 87 (inclusive) e o
índice 34 (exclusive), em ordem decrescente de índices;

• 3 -> Todos os elementos, exceto os dois últimos
"""


def main():

    lista = [i for i in range(100)]

    print("#1", lista[::-4])
    print("#2", lista[87:34:-1])
    print("#3", lista[:98:])


main()
