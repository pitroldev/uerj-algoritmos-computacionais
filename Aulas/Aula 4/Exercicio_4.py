# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 4

Leia números inteiros até o usuário informar 0.
Informar a soma dos números lidos, o total de
números lidos e a média aritimética deles.
"""


def main():
    total = 0
    i = 0
    num = 1

    while num != 0:
        while True:
            try:
                num = int(
                    input("\nDigite um número inteiro ou digite 0 para parar: "))
                break
            except:
                print("\nPor favor, digite um número inteiro válido.")

        if (num != 0):
            total += num
            i += 1

    if (i != 0):
        media = total/i
        print("Foram lidos", i, "números.")
        print("A soma total dos números é", total)
        print("A média aritimética deles é", media)
    else:
        print("Não foi lido nenhum número.")


main()
