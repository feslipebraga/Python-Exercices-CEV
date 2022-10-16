# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) # 5 randint para sortear n diferentes

# print(numeros)

print("Valores sorteados:", end=" ")
for n in numeros:       # usando o for, conseguimos eliminar os parenteses da tupla
    print(f"{n}", end=" ")
print(f"\nO maior valor sorteado foi o {max(numeros)}")
print(f"O menor valor sorteador foi o {min(numeros)}")