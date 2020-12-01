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


def enqueue(element, queue):
    queue.append(element)

def dequeue(queue):
    if not isQueueEmpty(queue):
        return queue.pop(0)
    return None

def isQueueEmpty(queue):
    return len(queue) == 0

def getFirstElement(queue):
    if not isQueueEmpty(queue):
        return queue[0]
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
    queue = []

    while True:
        op = menu()        
        if op == 1:
            enqueue(int(input("Digite um número inteiro: ")), queue)

        elif op == 2:
            dequeuedItem = dequeue(queue)
            if dequeuedItem != None:
                print("Removido o número {} da fila".format(dequeuedItem))
            else:
                print("A fila está vazia, não há itens para remover.")

        elif op == 3:
            firstItem = getFirstElement(queue)
            if firstItem != None:
                print("O número {} esta na frente da fila.".format(firstItem))
            else:
                print("A fila está vazia, não há itens para mostrar.")

        elif op == 4:
            if getFirstElement(queue) != None:
                print(queue)
            else:
                print("A fila está vazia, não há itens para mostrar.")

        elif op == 5:
            break

        cancel = input("\nPressione ENTER para continuar ou digite S para sair: ")
        if cancel.upper() == "S":
            break
    
    print("\nFim do programa.")


main()