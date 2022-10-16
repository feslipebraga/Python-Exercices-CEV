# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
numero = randint(0, 5)

usuario = int(input("Qual número entre 0 e 5 o computador pensou?\n"))
if usuario == numero:
    print(f"O computador escolheu o número {numero} e você também.\nVOCÊ ACERTOU!!!")
else:
    print(f"O computador escolheu o número {numero} e você {usuario}.\nVocê perdeu! :(")