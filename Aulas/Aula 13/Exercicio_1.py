# UERJ - 17/11/2020
# Aula 13 de Algoritmos Computacionais

"""
Exercício 1 - Pilhas

Construir uma função para exibir o conteúdo da pilha
indicando qual elemento está na posição do topo da pilha
"""

def empilhar(element, pilha):
    pilha.append(element)

def desempilha(pilha):
    if not pilha_vazia(pilha):
        return pilha.pop()
    return None

def pilha_vazia(pilha):
    return len(pilha) == 0

def obter_topo(pilha):
    return pilha[len(pilha) - 1]

def main():
    Pilha = ["teste", "este"]

    topo = obter_topo(Pilha)
    print(topo)

main()
