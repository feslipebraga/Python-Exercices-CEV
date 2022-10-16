# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(player="<desconhecido>", goal=0):
    print(f'O jogador {player} fez {goal} gol(s) no campeonato.')

jogador = input("Nome do jogador: ").capitalize()
gols = input("Número de Gols: ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador == "":
    ficha(goal = gols)
else:
    ficha(jogador, gols)