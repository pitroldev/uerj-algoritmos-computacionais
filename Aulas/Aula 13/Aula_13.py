# UERJ - 17/11/2020
# Aula 13 de Algoritmos Computacionais


class Node:
    """ Nó de uma estrutura encadeada. """
    def __init__(self, info = 0, previous_node = None): # Construtor
        self.info = info
        self.previous = previous_node

    def __repr__(self): # Representação
        return "%s -> %s" % (self.info, self.previous)


class Pilha:
    """ Pilha usando estrutura encadeada. """
    def __init__(self): # Construtor
        self.topo = None # Cria uma pilha vazia

    def __repr__(self): # Representação
        return "[" + str(self.topo) + "]"

    def empilhar(self, new_info):
        new_node = Node(new_info)
        new_node.previous = self.topo
        self.topo = new_node

    def pilha_vazia(self):
        return self.topo == None
    
    def desempilhar(self):
        if not Pilha.pilha_vazia(self):
            aux = self.topo.info
            self.topo = self.topo.previous
            return aux

    def obter_topo(self):
        if not Pilha.pilha_vazia(self):
            return self.topo.info
        return None



def main():
    pilha = Pilha()

    for i in range(5):
        pilha.empilhar(i)
        print("Inserido {} no topo da pilha: {}".format(i, pilha))
    
    print("O topo da lista é:", pilha.obter_topo())

    while not pilha.pilha_vazia():
        element = pilha.desempilhar()
        print("Removendo elemento {} do topo da pilha: {}".format(element, pilha))
    
main()