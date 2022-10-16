# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

c_oposto = float(input("Digite o valor do cateto oposto: "))
c_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = ((c_oposto ** 2) + (c_adjacente ** 2)) ** 0.5

print(f"O valor da hipotenusa é igual a {hipotenusa:.2f}")