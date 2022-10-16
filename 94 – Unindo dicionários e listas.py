# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

def linha():
    print("-" * 30)

pessoas = []
pessoa = {}
soma = 0

print(".     ==> CADASTRO DE PESSOAS <==     .")
while True:
    pessoa["nome"] = input("Nome: ").capitalize()
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    while True:
        pessoa["sexo"] = input("Sexo [M/F]: ").upper()
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Insira M ou F.")
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        resume = input("Desejar continuar? ").upper()[0]
        if resume in "SN":
            break
        print("ERRO! Insira 'SIM' ou 'NÃO'.")
    if resume == "N":
        break

print(pessoas)
linha()
print(f"No total foram cadastradas {len(pessoas)} pessoas.")

media = soma / len(pessoas)
print(f"A média de idade das pessoas é {media:.2f} anos")
print(f"A(s) mulher(es) cadastradas foi/foram: ", end="")
for f in pessoas:
    if f["sexo"] == "F":
        print(f["nome"], end=" ")
print()
for i in pessoas:
    if i["idade"] > media:
        print(f"{i['nome']} tem {i['idade']} anos e está acima da média. ")