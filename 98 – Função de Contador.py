# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada

def contador():
    for a in range(inicio, fim+1, passo):
        print(a, end=" ")
    if inicio > fim:
        for b in range(inicio, fim-1, -passo):
            print(f"{b}", end=" ")

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador()