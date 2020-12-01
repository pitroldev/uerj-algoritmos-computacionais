"""
UERJ - 17/11/2020
Trabalho 9 de Algoritimos Computacionais


Escrever um programa para criar uma fila, representada por uma lista, 
e apresentar ao usuário as opções de inserir remover, obter a 
frente da fila e visualizar todo o conteúdo da fila, 
bem como uma opção para encerramento do programa. 
Utilize números inteiros como elementos para serem armazenados na fila.
- Não é necessário tratamento de erros na entrada
"""


class Node:
    def __init__(self, value = 0, next_node = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return "%s -> %s" % (self.value, self.next)


class Queue:
    def __init__(self, first_element = None):
        self.first = first_element

    def __repr__(self):
        return "[" + str(self.first) + "]"

    def isEmpty(self):
        return self.first == None

    def enqueue(self, new_value):
        new_node = Node(new_value)
        current = self.first
        if Queue.isEmpty(self):
            self.first = new_node
        else:
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def dequeue(self):
        current = self.first
        if not Queue.isEmpty(self):
            self.first = current.next
            return current.value
        return None

    def getFirstElement(self):
        if not Queue.isEmpty(self):
            return self.first.value
        return None


def menu():
    op = 0
    print("\n1. Inserir número na fila.")
    print("2. Remover número na fila.")
    print("3. Obter a frente da fila.")    
    print("4. Visualizar todo o conteúdo da fila.")
    print("5. Para SAIR do programa.")
    try:
        op = int(input("\nSelecione uma opção: "))
        if 1 > op < 5:
            raise Exception
    except:
        print("\nPor favor, selecione uma opção válida, de 1 a 5.")
    return op


def main():
    fila = Queue()

    while True:
        op = menu()        
        if op == 1:
            fila.enqueue(int(input("Digite um número inteiro: ")))

        elif op == 2:
            dequeuedItem = fila.dequeue()
            if dequeuedItem != None:
                print("Removido o número {} da fila".format(dequeuedItem))
            else:
                print("A fila está vazia, não há itens para remover.")

        elif op == 3:
            firstItem = fila.getFirstElement()
            if firstItem != None:
                print("O número {} esta na frente da fila.".format(firstItem))
            else:
                print("A fila está vazia, não há itens para mostrar.")

        elif op == 4:
            if fila.first != None:
                print(fila)
            else:
                print("A fila está vazia, não há itens para mostrar.")

        elif op == 5:
            break

        cancel = input("\nPressione ENTER para continuar ou digite S para sair: ")
        if cancel.upper() == "S":
            break
    
    print("\nFim do programa.")


main()