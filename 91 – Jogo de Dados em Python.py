# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadores = {"jogador1": randint(1, 6),
"jogador2": randint(1, 6),
"jogador3": randint(1, 6),
"jogador4": randint(1, 6)}

ranking = []

for k, v in jogadores.items():
    print(f"{k} jogou o número {v}")

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print("     RANKING DOS JOGADORES")
print()
for p, v in enumerate(ranking):
    print(f"{p+1}nd lugar = {v[0]} com {v[1]} pontos.")