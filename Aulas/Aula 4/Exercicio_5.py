# UERJ - 29/09/2020
# Aula 4 de Algoritmos Computacionais

"""
Exercício 5

Leia números reais representando médias finais
dos alunos de uma turma, na faixa de 0 a 10,
até o usuário informar "F" ou "f" (de "fim").
Considere 5.0 como o mínimo para a aprovação.
Informe o número de alunos da turma, a média 
da turma, quantos alunos foram aprovados e
quantos não foram aprovados.
"""


def main():
    shouldContinue = ""
    numberAlunos = 0
    total = 0
    aprovados = 0
    reprovados = 0

    while shouldContinue != "F" and shouldContinue != "f":
        while True:
            try:
                nota = float(
                    input("\nDigite a média final do aluno {}: ".format(numberAlunos+1)))
                if (nota > 10) or (nota < 0):
                    raise Exception()
                break
            except:
                print("\nPor favor, digite uma nóta válida.")

        numberAlunos += 1
        total += nota
        if (nota >= 5):
            aprovados += 1
        else:
            reprovados += 1

        shouldContinue = str(
            input("Digite F para terminar ou enter para continuar: "))

    if (numberAlunos != 0):
        print("\nTotal de alunos:", numberAlunos)
        print("Total de alunos aprovados:", aprovados)
        print("Total de alunos reprovados:", reprovados)
        print("Média da turma:", total/numberAlunos)
    else:
        print("\nNão foi lido nenhuma nota.")


main()
