# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

notasAlunos = []

def linha():
    print("-=" * 20)

while True:
    nome = input("Nome: ").capitalize()
    nota1 = float(input(f"Nota [1]: "))
    nota2 = float(input(f"Nota [2]: "))
    media = (nota1 + nota2) / 2
    notasAlunos.append([nome, nota1, nota2, media])
    resume = input("Deseja cadastradar outro aluno? ").lower()[0]
    while resume not in "sn":
        print("Dados inválidos, tente novamente...")
        resume = input("Deseja cadastradar outro aluno? ")
    if resume == "n":
        break
print(notasAlunos)

linha()
print(f'{"No.":<4} {"Nome":>10} {"Média":>10}')
for pos, x in enumerate(notasAlunos):
    print(f"{pos:<4} {x[0]:>10} {x[3]:>10}")
linha()

print("Digite 999 para parar.")
while True:
    opcao = int(input("Desejar saber as notas de qual aluno? "))
    if opcao == 999:
        print("Obrigado por me utilizar :)")
        break
    else:
        print(f"Notas do {notasAlunos[opcao][0]} foram {notasAlunos[opcao][1]} e {notasAlunos[opcao][2]}")
