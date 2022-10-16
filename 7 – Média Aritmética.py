# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

soma = 0
cont = 0
while cont < 2:
    nota = float(input(f"Informe a nota: "))
    cont += 1
    soma += nota
media = soma / cont
print(f"A media das notas é: {media}")