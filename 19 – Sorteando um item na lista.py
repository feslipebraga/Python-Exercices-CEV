# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno1 = input(f"Informe o nome do 1º aluno: ")
aluno2 = input(f"Informe o nome do 2º aluno: ")
aluno3 = input(f"Informe o nome do 3º aluno: ")
aluno4 = input(f"Informe o nome do 4º aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)

print(f"O escolhido foi o {escolhido}")