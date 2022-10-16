# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

total18 = total_homem = mulher20 = 0

while True:
    print("CADASTRO DE PESSOAS")
    idade = int(input("Idade: "))
    if idade >= 18:
        total18 += 1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper()[0]
        if sexo == "M":
            total_homem += 1
        if sexo == "F" and idade < 20:
            mulher20 += 1
    continuacao = str(input("Deseja continuar? ")).upper()[0]
    if continuacao == "N":
        break
print(f"O total de pessoas com 18 anos ou mais é: {total18}")
print(f"O total de homens cadastrados é: {total_homem}")
print(f"O total de mulheres com menos de 20 anos é: {mulher20}")