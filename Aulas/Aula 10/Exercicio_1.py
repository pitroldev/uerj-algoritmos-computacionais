# UERJ - 27/10/2020
# Aula 10 de Algoritmos Computacionais

"""
Exercício 1

Escreva um programa que crie um dicionário
relacionando o nome dos estados brasileiros
(como chaves) às respectivas siglas, O Programa
deve perguntar ao usuário o nome de um estado
e chamar uma função que devolva a sua sigla.
O nome do estado pode estar em maiúsculas ou 
minúsculas e mesmo assim o programa deve dar 
a resposta correta.
"""


def main():
    estados_siglas = {"rio de Janeiro": "RJ", "bahia": "BH", "são paulo": "SP" }

    estado = input("Digite o nome de um estado: ")

    if estado.lower() in estados_siglas:
        selecionado = estados_siglas[estado.lower()]
        print("A sigla de {} é {}.".format(estado, selecionado))    
    else: 
        print("Estado inválido.")

main()
