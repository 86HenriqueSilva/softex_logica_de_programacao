""" Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
 A partir dessas informações, o sistema mostra rá o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano,
 o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido."""

def idade(nome, ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    print(f"{nome}, você tem ou irá completar {idade} anos em {ano_atual}.")

nome = input("Insira seu nome completo: ")
while True:
    try:
        ano_nascimento = int(input("Insira o ano de nascimento: "))
        if ano_nascimento < 1922 or ano_nascimento > 2021:
            raise ValueError
        break
    except ValueError:
        print("Ano inválido. Insira um número entre 1922 e 2021.")

idade(nome, ano_nascimento)
