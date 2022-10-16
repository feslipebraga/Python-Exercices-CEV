# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Informe o valor da primeira reta: "))
b = float(input("Informe o valor da segunda reta: "))
c = float(input("Informe o valor da terceira reta: "))

# if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + c):     # É uma possibilidade.
if a < b + c and b < a + c and c < a + b:
    print("Os valores das retas acima podem formar um triangulo")
else:
    print("Os valores NÃO podem formar um triangulo")