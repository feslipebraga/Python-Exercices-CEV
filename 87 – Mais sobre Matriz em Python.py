# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira_coluna = 0
maior = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Valor [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]}]", end=" ")
    print()
print(f"A soma dos pares é {pares}")
for linha in range(3):
    terceira_coluna += matriz[linha][2]
print(f"A soma dos valores da 3nd coluna é {terceira_coluna}")
for coluna in range(3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f"O maior valor da 2nd coluna é o {maior}")