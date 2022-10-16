# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero = int(input(f"Informe o 1º número: "))
x = 2
maior = menor = numero
while x <= 3:
    numero = int(input(f"Informe o {x}º número: "))
    x += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")
