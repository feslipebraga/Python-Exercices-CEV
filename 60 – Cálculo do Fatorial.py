# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo 
# 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Informe um número: "))
print(f"{numero}! = ", end="")
x = numero
fatorial = 1
while x > 0:
    print(x, end=" ")
    print("x" if x > 1 else "=", end=" ")
    fatorial = fatorial * x
    x -= 1
print(f"{fatorial}")