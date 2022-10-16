# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = []

def sorteia():
    for x in range(5):
        numero = randint(1, 10)
        numeros.append(numero)
    print(numeros)
print("OS VALORES SORTEADOS FORAM:")
sorteia()       

pares = []
def somaPar():
    for x in numeros:
        if x % 2 == 0:
            pares.append(x)
    soma = sum(pares)
    print(soma)
print("A SOMA DOS VALORES PARES:")
somaPar()