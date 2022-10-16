# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("Bem-vindo ao Banco FBB")
print("Notas disponíveis para saque: R$50, R$20, R$10 e R$1")

saque = int(input("Informe o valor do saque: "))

tupla = (50, 20, 10, 1)
for notas in tupla:
    cedulas = saque // notas
    saque = saque % notas
    if cedulas > 0:
        print(f"Total de {cedulas} cedulas de R${notas}")