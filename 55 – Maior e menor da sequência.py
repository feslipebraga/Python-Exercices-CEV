# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0

for c in range(1, 6):
    peso = float(input(f"Informe o peso da {c} pessoa: "))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"Maior peso {maior}, menor peso {menor}")