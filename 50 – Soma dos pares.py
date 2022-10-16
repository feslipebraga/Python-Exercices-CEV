# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input(f"Informe o {c}nd número: "))
    if numero % 2 == 0:
        contador = contador + 1
        soma += numero
print(f"A soma dos {contador} números pares informados é igual a {soma}")