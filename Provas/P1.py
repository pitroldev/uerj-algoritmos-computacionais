"""
UERJ - 01/12/2020
Prova 1 de Algoritimos Computacionais


Escreva um programa para ler um arquivo texto fornecido (“Receita de Ano Novo.txt”) 
e fazer a contagem de espaços, de cada letra maiúscula e de cada letra minúscula, 
imprimir os valores encontrados e identificar a letra (maiúscula ou minúscula) 
com maior número de ocorrências.

Funções: o programa terá duas funções:

a) Uma para abrir o arquivo, ler o texto e fechar o arquivo. Essa função deverá retornar o texto
lido.
b) Outra função para processar o texto. Essa função receberá o texto como argumento.
c) Essas duas funções deverão ser chamadas a partir da função principal (main()).

Importante: na avaliação da solução apresentada, será considerada a estrutura usada para construir o
programa.

Observações:

a) O texto contido no arquivo não possui letras acentuadas nem o caractere ‘ç’, isto é, todos os
caracteres possuem códigos ASCII até 127.
b) O texto contido no arquivo possui alguns sinais de pontuação.
c) Os códigos ASCII na faixa 0 a 31 são caracteres de controle e não devem ser considerados (por
exemplo, caractere de nova linha e marcas de tabulação).

Códigos ASCII:
‘A’ – ’Z’: 65 – 90;
‘a’ – ’z’: 97 – 122;
‘ ’ : 32 (espaço em branco)

Lembre-se que você dispõe das funções ord(<caractere>), que retorna o código ASCII de <caractere>,
e chr(<código>), que retorna o caractere que tem <código> ASCII.

Escolha uma estrutura de dados adequada à representação do problema a ser resolvido
"""

def readFile():
    try:
        with open("Receita de Ano Novo.txt", "r") as filetxt:
            return filetxt.read()
    except:
        print("Erro ao ler o arquivo.")
        return ""

def processText(text):    
    upperDictionary = {}
    lowerDictionary = {}
    letter = ""

    whiteSpacesCount = 0

    for i in range(65, 91):
        upperDictionary[chr(i)] = 0
    for i in range(97, 123):
        lowerDictionary[chr(i)] = 0

    for l in text:
        if ord(l) >= 65 and ord(l) <= 90:
                upperDictionary[l] += 1
        if ord(l) >= 97 and ord(l) <= 122:
                lowerDictionary[l] += 1
        if ord(l) == 32:
            whiteSpacesCount += 1


    # Identificando letra maiúscula ou minúscula com maior ocorrência
    occurrences = 0
    joinedDictionary = upperDictionary.copy()
    joinedDictionary.update(lowerDictionary)

    for l in joinedDictionary:
        if (joinedDictionary[l] > occurrences):
            occurrences = joinedDictionary[l]
            letter = l

    # Mostrando em tela
    print("\nContagem de letras maiúsculas:\n", upperDictionary)

    print("\nContagem de letras minúsculas:\n", lowerDictionary)

    print("\nO espaço em branco aparece {} vezes.".format(whiteSpacesCount))

    print("\nA letra '{}' é a letra com mais ocorrências e aparece {} vezes.".format(letter, occurrences))


def main():
    text = readFile()
    processText(text)
    print("\nFIM DO PROGRAMA")


main()