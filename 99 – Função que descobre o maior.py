# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior():
    numeros = []
    for x in range(5):
        numero = int(input(f"Numero [{x}]: "))
        numeros.append(numero)
        maior = max(numeros)
    print("ANALISANDO OS VALORES DIGITADOS:")
    for x in numeros:
        print(x, end=" ", flush=True)
        sleep(0.5)
    print(f"\nO maior valor informado foi o: {maior}")

maior()