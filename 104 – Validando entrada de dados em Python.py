# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(texto):
    ok = False
    valor = 0
    while True:
        n = input(texto)
        if n.isnumeric():
            valor = int(n)
            ok = True
        if ok:
            break
        else:
            print("\033[0;31mERRO, INFORME UM NÚMERO INTEIRO.\033[m")
    return valor

x = leiaInt('Digite um número: ')
print(f'Você digitou o número {x}')