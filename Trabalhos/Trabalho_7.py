"""
UERJ - 03/11/2020
Trabalho 7 de Algoritimos Computacionais

Escreva um programa para criar uma lista de tuplas contendo 
quatro itens relativos a uma mesma pessoa: (nome, email, dia nascimento, mês nascimento). 
Implemente funções para fazer um cadastro: incluir(), consultar(), consultar_aniversariante(), listar()
O programa deverá ter um laço principal, implementado na função main(), apresentando as opções disponíveis, 
bem como uma opção para encerrar a execução. Implemente um menu de opções em forma de uma função.
Para fins de teste, faça a inclusão de algumas pessoas no cadastro

- Não é necessário tratamento de erros na entrada
"""
def listar(userList):
    print("\nLista de todos os usuários cadastrados:")
    for user in userList:
        print(user)

def consultar_aniversariante(userList):
    day = int(input("\nDigite um dia: "))
    month = int(input("Digite um mês: "))

    print("\nLista de todos os usuários aniversariantes do dia {}/{}:".format(day, month))
    for user in userList:
        if (day == user[2] and month == user[3]):
            print(user)

def consultar(userList):
    name = input("\nDigite o nome do usuário: ")

    print("\nLista de todos os usuários com nome {}:".format(name))
    for user in userList:
        if (name.upper() == user[0].upper()):
            print(user)

def incluir(userList):
    nome = input("\nDigite o nome: ")
    email = input("Digite o email: ")
    dia = int(input("Digite o dia do aniversário: "))
    mes = int(input("Digite o mês do aniversário: "))

    print("\nUsuário", nome, "cadastrado com sucesso!")

    return userList.append((nome, email, dia, mes))

def menu():
    op = 0
    print("\n1. Incluir um cadastro.")
    print("2. Consultar um cadastro pelo nome.")
    print("3. Consultar um cadastro pelo aniversário.")    
    print("4. Listar todos os cadastros.")
    print("5. Para SAIR do programa.")
    try:
        op = int(input("\nSelecione uma opção: "))
        if 1 > op < 5:
            raise Exception
    except:
        print("\nPor favor, selecione uma opção válida, de 1 a 5.")
    return op


def main():
    userList = [("Clodoaldo", "Clodoaldo@email.com", 25, 5),
        ("Arlinda", "Arlinda@email.com", 12, 3),
        ("Cleidilucia", "Cleidilucia@email.com", 28, 1),
        ("Ornitorovisk", "Ornitorovisk@email.com", 5, 12)]

    while True:
        op = menu()        
        if op == 1:
            incluir(userList)
        elif op == 2:
            consultar(userList)
        elif op == 3:
            consultar_aniversariante(userList)
        elif op == 4:
            listar(userList)
        elif op == 5:
            break

        cancel = input("\nPressione ENTER para continuar ou digite S para sair: ")
        if cancel.upper() == "S":
            break

    
    print("\nFim do programa.")


main()