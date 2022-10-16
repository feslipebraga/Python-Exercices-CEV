# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos["nome"] = input("Aluno: ").capitalize()
alunos["media"] = float(input("Média: "))

if (alunos["media"]) >= 7:
    alunos["situação"] = "APROVADO"
elif 5 <= (alunos["media"]) < 7:
    alunos["situação"] = "RECUPERAÇÃO"
else:
    alunos["situação"] = "REPROVADO"

def linha():
    print("-" * 20)

linha()    
for k, v in alunos.items():
    print(f"{k} = {v}")
linha()