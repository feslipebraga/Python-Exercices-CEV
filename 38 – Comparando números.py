# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro: "))

if n1 > n2:
    print(f"O maior valor é {n1}")
elif n2 > n1:
    print(f"O maior valor é {n2}")
else:
    if n1 == n2:
        print("Não há maior, os dois valores são iguais.")