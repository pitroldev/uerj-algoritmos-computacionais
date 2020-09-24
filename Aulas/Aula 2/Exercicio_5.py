# UERJ - 22/09/2020
# Aula 2 de Algoritmos Computacionais

"""
Exercício 5

Ler uma média semestral e emitir a mensagem correspondente para a seguinte situação:

- A UERJ usa o seguinte critério para realização de prova final,
em relação à média obtida pelo aluno no semestre:
 • Se Média >= 7,0 => aprovação direta
 • Se 4,0 <= Média < 7,0 => fazer prova final
 • Se Média < 4,0 => reprovação direta
"""


def checkStatus(num):
    if num >= 7:
        return 'Aprovado'
    elif num >= 4 and num < 7:
        return 'Prova Final'
    else:
        return 'Reprovado'


def main():
    while True:
        while True:
            try:
                num = float(input("\nDigite uma nota: "))
                break
            except:
                print("\nPor favor, digite uma nota válida.")

        print("\nO status do aluno é:", checkStatus(num))

        shouldContinue = str(
            input("\nDigite S para sair do programa ou aperte ENTER para continuar: "))
        if shouldContinue.upper() == "S":
            return


main()
