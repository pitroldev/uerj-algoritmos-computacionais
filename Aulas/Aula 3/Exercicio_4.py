# UERJ - 23/09/2020
# Aula 3 de Algoritmos Computacionais

"""
Exercício 4

Leia 3 notas, P1, P2, e NR e calcule a média final
dando peso 2 as notas da P1 e P2, e peso 1 para a NR.
Imprimir a média final e, se ela for maior
ou igual a 7.0, informar que o aluno está aprovado.
"""


def calculateMedia(p1, p2, nr):
    media = (p1*2 + p2*2 + nr)/5

    phrase = "A média do aluno é {} e ele está".format(media)

    if (media > 7):
        print(phrase, "aprovado.")
    else:
        print(phrase, "reprovado.")


def main():

    while True:
        while True:
            try:
                p1 = float(input("\nDigite a nota da P1: "))
                p2 = float(input("\nDigite a nota da P2: "))
                nr = float(input("\nDigite a nota do relatório: "))

                if (0 > p1) or (0 > p2) or (0 > nr) or (p1 > 10) or (p2 > 10) or (nr > 10):
                    raise Exception()

                break
            except:
                print("\nPor favor, digite notas válidas entre 0 e 10.")

        calculateMedia(p1, p2, nr)

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
