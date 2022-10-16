# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
homemvelho = ''
idadehomemvelho = 0
mulheresmenosde20 = 0
contador_homem = 0
contador_mulher = 0

for x in range(1,5):
    print(f" ------ {x}ª Pessoa ----- ")
    nome = input("Nome: ").strip().capitalize()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()[0]
    somaidade = somaidade + idade
    if sexo == "M" and idade > idadehomemvelho:
        idadehomemvelho = idade
        homemvelho = nome
        contador_homem += 1
    if sexo == "F":
        contador_mulher += 1
        if idade < 20:
            mulheresmenosde20 += 1

# Média das idades
media = somaidade / x
print(f"A média da idade das pessoas é {media}")

# Nome e idade do homem mais velho
if contador_homem > 0:
    print(f"O homem mais velho se chama {homemvelho} e tem {idadehomemvelho} anos")
if contador_homem == 0:
    print("Nenhum homem foi informado")

# Quantas mulheres tem menos de 20 anos
if contador_mulher == 0:
    print("Nenhuma mulher foi informada")
if contador_mulher > 0 and mulheresmenosde20 == 0:
    print("Nenhuma mulher tem menos de 20 anos")
if contador_mulher > 0 and mulheresmenosde20 > 0:
    print(f"{mulheresmenosde20} mulher(es) tem menos de 20 anos.")