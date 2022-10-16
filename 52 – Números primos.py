# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print("ANALISANDO NUMEROS PRIMOS")
numero = int(input("Informe um número: "))

contador = 0

for c in range(1, numero+1):
    if numero % c == 0:
        contador = contador + 1
if contador == 2:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} NÃO é primo.")