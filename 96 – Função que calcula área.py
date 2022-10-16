# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l * c
    print(f"A área do terreno é {area}m²")

largura = int(input("Largura: "))
comprimento = int(input("Comprimento: "))
area(largura, comprimento)