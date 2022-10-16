# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print("VOU PENSAR EM UM NÚMERO INTEIRO E DUVIDO VOCÊ ACERTAR")

from random import randint
computador = randint(0, 10)
jogador = int(input("Qual número, entre 0 e 10, eu pensei?\n"))
contador = 0 
while jogador != computador:
    contador += 1
    jogador = int(input("Errou, tente novamente.\n"))

if jogador == computador and contador > 0:
    print(f"PARÁBENS! O COMPUTADOR PENSOU NO NÚMERO {computador} E VOCÊ ACERTOU!")
    print(f"Foram necessárias {contador + 1} tentativas para acertar.")
if jogador == computador and contador == 0:
    print(f"PARÁBENS! O COMPUTADOR PENSOU NO NÚMERO {computador} E VOCÊ ACERTOU!")
    print(f"Foi necessário apenas 1 tentativa para acertar.")