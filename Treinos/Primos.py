"""
Exercício de Treino - 23/09/2020

Determina se um número é primo, caso não seja, 
determina quantos e quais divisores ele possúi.
"""


def check_primo(num):
    div_num = 0
    divs = []

    for i in range(num):
        i += 1
        if num % i == 0:
            divs.append(i)
            div_num += 1

    if div_num <= 2 and num != 1:
        return print("\nO número", num, "é primo.\n")
    else:
        print("\nO número", num, "NÃO é primo pois possui",
              div_num, "divisores.\n")
        return print("Os seguintes numeros são divisores:", divs, "\n")


def main():
    print("\n### Checador de Números Primos ###")
    while True:
        try:
            num = int(input("\nEscreva um número inteiro positivo não nulo: "))
            if num < 1:
                raise Exception()
            else:
                break
        except:
            print("\nPor favor, digite um número válido.")

    return check_primo(num)


main()
