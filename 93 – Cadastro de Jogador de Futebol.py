# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

def l():
    print("-" * 40)

campeonato = {}
gols = []

campeonato["nome"] = input("Nome do Jogador: ").capitalize()
campeonato["partidas"] = int(input("Quantidade de partidas: "))
for x in range(1, campeonato["partidas"] + 1):
    gols.append(int(input(f"Quantidade de gols na partida {x}: ")))

soma = sum(gols)

campeonato["gols"] = gols
campeonato["totalGols"] = soma
l()
print(campeonato)
l()
for k, v in campeonato.items():
    print(f"No campo {k} tem o valor {v}")
l()
print(f"O jogador {campeonato['nome']} jogou {campeonato['partidas']} partidas. ")
for i, x in enumerate(gols):
    print(f"Na partida {i+1} ele fez {x} gol(s)")
print(f"Foi um total de {soma} gol(s).")