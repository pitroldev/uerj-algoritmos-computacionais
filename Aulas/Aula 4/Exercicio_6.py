# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 6

Faça novamente o Exercício 5 solicitando
antes o número de alunos da turma.
"""


def mediaTurma(numberAlunos):
    total = 0
    i = 0
    aprovados = 0
    reprovados = 0

    while i < numberAlunos and numberAlunos != 0:
        while True:
            try:
                nota = float(
                    input("\nDigite a média final do aluno {}: ".format(i+1)))
                if (nota > 10) or (nota < 0):
                    raise Exception()
                break
            except:
                print("\nPor favor, digite uma nóta válida.")

        i += 1
        total += nota
        if (nota >= 5):
            aprovados += 1
        else:
            reprovados += 1

    print("\nTotal de alunos:", numberAlunos)
    print("Total de alunos aprovados:", aprovados)
    print("Total de alunos reprovados:", reprovados)
    print("Média da turma:", total/numberAlunos)


def main():

    while True:
        try:
            numberAlunos = int(input("Quantos alunos são? "))
            if (numberAlunos < 0):
                raise Exception()
            break
        except:
            print("\nPor favor, digite um número de alunos válido.")

    if (numberAlunos != 0):
        mediaTurma(numberAlunos)
    else:
        print("\nNão foi lido nenhuma nota.")


main()
