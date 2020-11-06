"""
UERJ - 27/10/2020
Trabalho 6 de Algoritimos Computacionais


Construir um dicionário contendo 4 itens relativos
a uma mesma pessoa: {Nome: (Email, Dia de nascimento, Mês de nascimento)}
- Use números aleatórios para gerar dia e mês de nascimento. 
- Use a função chr(<num>), gere nomes aleatórios com até 10 letras. 
- O email terá o formato <nome>@xyz.com.br. 
Você deverá gerar dados para representar um grupo de 100 pessoas.
Complete o programa verificando se há na lista algum aniversariante
do dia. Você poderá informar o dia e o mês atuais. 
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
    
    return {nome: (email, day, month)}

def generateUserList():
    userlist = {}

    while (len(userlist) < 100):
        userlist.update(generateUser())

    return userlist

def checkBirthdayInUserList(userlist, day, month):

    birthdayNameList = []

    for name in userlist:
        user = userlist[name]
        if (day == user[1] and month == user[2]):
            birthdayNameList.append(name)
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
