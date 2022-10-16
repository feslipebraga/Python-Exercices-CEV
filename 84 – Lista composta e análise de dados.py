# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
maior = menor = 0

while True:
    nome = str(input("Nome: ")).capitalize()
    peso = float(input("Peso: "))
    dados.append(nome)
    dados.append(peso)
    if len(lista) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    lista.append(dados[:])
    dados.clear()
    resume = str(input("Desejar continuar? ")).lower()[0]
    if resume == "n":
        break
print(lista)
print(f"Ao todo você cadastrou {len(lista)} pessoas.")
print(f"O maior peso informado foi {maior}kg e pertece a", end=" ")
for i in lista:
    if i[1] == maior:
        print(f"{i[0]}")
print()
print(f"O menor peso informado foi {menor}kg e pertence a", end=" ")
for i in lista:
    if i[1] == menor:
        print(f"{i[0]}")
print()