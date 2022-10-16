# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

soma = produtos1000 = menor = contador = 0
barato = " "
while True:
    produto = str(input("Nome do produto: ")).capitalize()
    preco = float(input("Preço: R$"))
    contador += 1
    soma += preco
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        produtos1000 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Desejar continuar? ")).upper()[0]
    if continuar == "N":
        break
print(f"Total da compra: R${soma:.2f}")
print(f"Total de produtos acima de R$1000: {produtos1000}")
print(f"O produto mais barato: {barato}, custo: R${menor:.2f}")