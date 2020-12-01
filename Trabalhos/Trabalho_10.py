"""
UERJ - 24/11/2020
Trabalho 10 de Algoritimos Computacionais


Escreva um programa que crie um classe para representar uma conta corrente de um banco.
A classe terá um número e um saldo. Defina métodos para depositar e sacar. 
Em casos de saques, caso o valor seja maior que o saldo, gere uma exceção ValueError. 
No método construtor, saldo terá valor default zero. 
Crie um objeto conta e faça alguns depósitos e saques e informe o saldo a cada operação.
- Não é necessário tratamento de erros na entrada
"""
import random

def gerarNumConta():
    conta_numero = ""
    for i in range(0,5):
        conta_numero = conta_numero + str(random.randint(0, 9))
    conta_numero = conta_numero + "-" + str(random.randint(0, 9))
    return conta_numero

class Conta:

    def __init__(self, num = gerarNumConta(), saldo = 0):
        self.num = num
        self.saldo = saldo

    def __repr__(self):
        return "\nNúmero da conta: "+ str(self.num) + "\nSaldo disponível: R$" + str(self.saldo)

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo

    def saque(self, valor):
        if self.saldo - valor >= 0:
            self.saldo = self.saldo - valor
            return self.saldo
        else:
            raise ValueError


def menu():
    op = 0
    print("\n1. Visualizar conta corrente.")
    print("2. Depositar.")
    print("3. Sacar.")    
    print("4. Para SAIR do programa.")
    try:
        op = int(input("\nSelecione uma opção: "))
        if 1 > op < 4:
            raise Exception
    except:
        print("\nPor favor, selecione uma opção válida, de 1 a 4.")
    return op



def main():
    contaCorrente = Conta()

    while True:
        op = menu()        
        if op == 1:
            print(contaCorrente)

        elif op == 2:
            valor = float(input("Digite um valor para depositar: "))
            saldo = contaCorrente.deposito(valor)
            print("\nVocê depositou R${} reais, o seu saldo atual é de R${}".format(valor, saldo))

        elif op == 3:
            try:
                valor = float(input("Digite um valor para sacar: "))
                saldo = contaCorrente.saque(valor)
                print("\nVocê sacou R${} reais, o seu saldo atual é de R${}".format(valor, saldo))
            except:
                print("\nVocê não possui esse dinheiro em conta, o seu saldo atual é de R${}".format(contaCorrente.saldo))

        elif op == 4:
            break

        cancel = input("\nPressione ENTER para continuar ou digite S para sair: ")
        if cancel.upper() == "S":
            break
    
    print("\nFim do programa.")


main()