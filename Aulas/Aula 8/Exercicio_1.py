# UERJ - 13/10/2020
# Aula 8 de Algoritmos Computacionais

"""
Exercício 1

Dada a cadeia "Periodo Letivo Online da UERJ"
escreva um programa que imprima:

1. Os caracteres de índices pares;
2. Os caracteres de índices ímpares;
3. Os caracteres entre os índices 2 (inclusive)
e 4 (exclusive);
4. O caractere de índice 1 e depois os caracteres
distantes 3 posições a partir de, até o final;
"""


def main():

    cadeia = "Periodo Letivo Online da UERJ"
    print("#1", cadeia[::2])
    print("#2", cadeia[1::2])
    print("#3", cadeia[2:4])
    print("#4", cadeia[1::4])


main()
