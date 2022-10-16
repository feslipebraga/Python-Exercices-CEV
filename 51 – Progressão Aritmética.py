# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("PROGRESSÃO ARITMÉTICA")

a1 = float(input("Informe o 1nd termo da PA: "))
razao = float(input("Qual a razão da PA? "))

for c in range(1, 11):
    print(f"A{c} = {a1 + ((c - 1) * razao)}")