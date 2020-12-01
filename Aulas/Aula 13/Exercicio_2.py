# UERJ - 17/11/2020
# Aula 13 de Algoritmos Computacionais

"""
Exercício 2 - Filas

Construir uma função para exibir o conteúdo da fila
indicando a frente e o fim da fila
"""

def inserir(element, fila):
    fila.append(element)

def remover(fila):
    if not fila_vazia(fila):
        return fila.pop(0)
    return None

def fila_vazia(fila):
    return len(fila) == 0

def obter_frente(fila):
    return fila[0]

def obter_fim(fila):
    return fila[len(fila) - 1]

def main():
    fila = ["teste", "este"]

    print(obter_frente(fila))
    print(obter_fim(fila))

main()
