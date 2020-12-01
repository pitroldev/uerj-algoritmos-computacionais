# UERJ - 10/11/2020
# Aula 12 de Algoritmos Computacionais

"""
Exercício 1

Escreva um programa que faça uma cópia do
"Arq.txt" criado anteriormente com o nome de "Arq2.txt"
"""

def createFile(text):
    with open("Aqr.txt", "w") as file:
        file.write(text)

def duplicateFile(filename, new_filename):
    with open(filename, "r") as file:
        text = file.read()
    
    with open(new_filename, "w") as new_file:
        new_file.write(text)
    
def main():
    createFile("Teste\n")
    duplicateFile("Aqr.txt", "Aqr2.txt")

main()
