"""
UERJ - 20/10/2020
Trabalho 5 de Algoritimos Computacionais


Gerar tuplas contendo 4 itens relativos a uma mesma pessoa:
Nome; Email; Dia de nascimento; Mês de nascimento.
Use uma tupla para cada pessoa e armazene-as em uma lista com capacidade para 100 pessoas. 
Utilize números aleatórios para gerar dia e mês de nascimento. 
Usando a função chr(<num>), gere nomes aleatórios com até 10 letras. 
Use esse nome para construir o endereço eletrônico (email) com o formato <nome>@xyz.com.br. 
Após criar a lista de 100 pessoas, complete o programa verificando se há na lista algum 
aniversariante do dia. Você poderá informar o dia e o mês atuais. 
A saída do programa será a lista de nomes dos aniversariantes. 

- Não é necessário tratamento de erros na entrada
"""

import random

def generateUser():
    nome = ""

    for i in range(1, random.randint(4,10)):
        if i == 1:
            character = chr(random.randint(65, 90))
        else:            
            character = chr(random.randint(97, 122))
        nome += character
    
    email = nome + "@xyz.com.br"

    month = random.randint(1, 12)

    if (month == 2):
        day = random.randint(1, 29)
    elif (month % 2 != 0 and month < 8) or (month >= 8 and month % 2 == 0):
        day = random.randint(1, 31)
    else:        
        day = random.randint(1, 30)
    
    user = nome, email, day, month
    return user

def generateUserList():
    userlist = []

    while (len(userlist) < 100):
        userlist.append(generateUser())

    return userlist

def checkBirthdayInUserList(userlist, day, month):

    birthdayNameList = []

    for user in userlist:
        if (day == user[2] and month == user[3]):
            birthdayNameList.append(user[0])
    return birthdayNameList

def main():

    userList = generateUserList()
    control = ""

    while (control.upper() != "S"):

        day = int(input("\nDigite um dia: "))
        month = int(input("Digite um mês: "))

        birthdays = checkBirthdayInUserList(userList, day, month)

        if len(birthdays) > 0:
            print("\nLista dos nomes dos aniversariantes no dia {}/{}:".format(day, month))
            for name in birthdays:
                print(name)
        else:
            print("\nNão existem aniversariantes no dia {}/{}".format(day, month))

        control = input("\nDigite S para sair ou aperte ENTER para continuar: ")
    print("Fim do programa.")

main()
