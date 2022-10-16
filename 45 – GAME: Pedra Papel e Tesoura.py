lista = [" ", "PEDRA", "PAPEL", "TESOURA"]

print("""[1] - PEDRA
[2] - PAPEL
[3] - TESOURA""")

jogador = int(input("Escolha uma opção: "))

import random

computador = random.randint(1,3)

print(f"Você escolheu {lista[jogador]}")

from time import sleep

sleep(1)
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
sleep(1)

print(f"O computador escolheu {lista[computador]}")

if jogador == 1: # PEDRA
    if computador == 1:
        print("EMPATE!")
    if computador == 2:
        print("COMPUTADOR VENCEU!")
    if computador == 3:
        print("VOCÊ VENCEU!")
elif jogador == 2: # PAPEL
    if computador == 1:
        print("VOCÊ VENCEU!")
    if computador == 2:
        print("EMPATE!")
    if computador == 3:
        print("COMPUTADOR VENCEU!")
elif jogador == 3: # TESOURA
    if computador == 1:
        print("COMPUTADOR VENCEU!")
    if computador == 2:
        print("VOCÊ VENCEU!")
    if computador == 3:
        print("EMPATE!")
else:
    print("Jogada inválida.")