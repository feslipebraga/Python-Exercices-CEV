# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

idade = 0
menores = 0
maiores = 0
ano_nascimento = 0

for contador in range(0, 7):
    ano_nascimento = int(input("Informe seu ano de nascimento: "))
    idade = 2022 - ano_nascimento
    if idade > 18:
        maiores = maiores + 1
    if idade < 18:
        menores = menores + 1

if maiores == 1:
    print("1 pessoa atingiu a maioridade")
elif maiores == 0:
    print("Nenhuma pessoa é maior de idade")
else:
    print(f"{maiores} pessoas atingiram a maioridade")

if menores == 1:
    print("1 pessoa ainda não é adulta")
elif menores == 0:
    print("Nenhuma pessoa é menor de idade")
else:
    print(f"{menores} pessoas ainda não são adultas.")