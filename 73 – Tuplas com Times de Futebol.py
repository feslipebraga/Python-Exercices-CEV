# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Flamengo.

times = ("Palmeiras", "Flamengo", "Corinthians", "Fluminense", "Athletico-PR", "Internacional", "Atlético-MG", "América-MG",
"Bragantino", "Santos", "São Paulo", "Botafogo", "Goiás", "Ceará SC", "Fortaleza", "Cuiabá", "Avaí", "Coritiba", "Atlético-GO", "Juventude")

linha = "-" * 40

print(f"{linha}")

print("\nTABETA DO CAMPEONATO BRASILEIRO DE FUTEBOL")

print(f"\n{linha}")

print("\nOs 5 primeiros times são: ")
# times[0:5]
for time in range(0, 5):
    print(f"{time + 1}º {times[time]}")

print(f"\n{linha}")

print("\nOs 4 últimos colocados são: ")
# times[-1:-4]
for time in range(19, 15, -1):
    print(f"{time+1}º {times[time]}")

print(f"\n{linha}")

print("\nTimes em ordem alfabética:")
print(sorted(times))

print(f"\n{linha}")

print(f"\nO Flamengo está na {times.index('Flamengo')+1}º posição")

print(f"\n{linha}")