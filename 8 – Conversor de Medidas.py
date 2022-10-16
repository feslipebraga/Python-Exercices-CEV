# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = int(input("Informe uma medida em metros: "))

cm = valor * 100
mm = valor * 1000

print(f"O valor convertido para cm é: {cm}cm e em mm é: {mm}mm")