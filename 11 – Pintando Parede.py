# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = int(input("Largura: "))
altura = int(input("Altura: "))
area = largura * altura

tinta = 1
metro_quadrado = 2

x = tinta * area / metro_quadrado

print(f"A quantidade necessária de tinta para pintar a área de {area}m2, será de {x}l")