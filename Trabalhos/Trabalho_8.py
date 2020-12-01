"""
UERJ - 10/11/2020
Trabalho 8 de Algoritimos Computacionais

Escreva um programa para criar uma lista de tuplas contendo quatro itens relativos a uma mesma pessoa:
(nome, email, dia nascimento, mês nascimento).
Implemente funções para fazer um cadastro: incluir(), consultar(), consultar_aniversariante(), listar()
O programa deverá implementar um laço principal na função main(), apresentando as opções disponíveis,
 bem como uma opção para encerrar a execução. Implemente um menu de opções em forma de uma função.
Use um arquivo texto para salvar os dados. Esse arquivo deverá ser lido a cada vez que
o programa começar e deverá ser gravado a cada vez que o programa terminar.  
"""

def ler_usuarios():
    try:
        with open("userList.txt", "r") as userList:
            return userList.readlines()
    except:
        return []


def gravar_usuario(user):
    try:
        with open("userList.txt", "a") as userList:
            userList.write(str(user)+"\n")
    except:
        print("Erro ao escrever no arquivo.")


def listar():
    userList = ler_usuarios()
    print("\nLista de todos os usuários cadastrados:")
    for user in userList:
        print(user)

def consultar_aniversariante():
    userList = ler_usuarios()
    day = int(input("\nDigite um dia: "))
    month = int(input("Digite um mês: "))

    print("\nLista de todos os usuários aniversariantes do dia {}/{}:".format(day, month))
    for string_user in userList:
        user = eval(string_user)
        if (day == user[2] and month == user[3]):
            print(user)

def consultar():
    userList = ler_usuarios()
    name = input("\nDigite o nome do usuário: ")
    print("\nLista de todos os usuários com nome {}:".format(name))
    for string_user in userList:
        user = eval(string_user)
        if (name.upper() == user[0].upper()):
            print(user)

def incluir():
    while True:
        try:
            nome = input("\nDigite o nome: ")
            email = input("Digite o email: ")
            dia = int(input("Digite o dia do aniversário: "))
            if dia > 31 or dia < 1:
                raise Exception
            mes = int(input("Digite o mês do aniversário: "))
            if mes > 12 or mes < 1:
                raise Exception

            break
        except:
            print("\nPor favor, digite valores válidos.")

    print("\nUsuário", nome, "cadastrado com sucesso!")
    return gravar_usuario((nome, email, dia, mes))

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
    if len(ler_usuarios()) == 0:
        gravar_usuario(("Clodoaldo", "Clodoaldo@email.com", 25, 5))
        gravar_usuario(("Arlinda", "Arlinda@email.com", 12, 3))
        gravar_usuario(("Cleidilucia", "Cleidilucia@email.com", 28, 1))

    while True:
        op = menu()        
        if op == 1:
            incluir()
        elif op == 2:
            consultar()
        elif op == 3:
            consultar_aniversariante()
        elif op == 4:
            listar()
        elif op == 5:
            break

        cancel = input("\nPressione ENTER para continuar ou digite S para sair: ")
        if cancel.upper() == "S":
            break

    
    print("\nFim do programa.")


main()