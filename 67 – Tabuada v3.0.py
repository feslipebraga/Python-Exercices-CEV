# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print("""Escolha um número para ver a sua tabuada
Digite um valor negativo a qualquer momento para encerrar o programa.""")

while True:
    numero = int(input("Número: "))
    if numero < 0:
        break
    for x in range(1, 11):
        print(f"{numero} x {x} = {numero * x}")
print("Programa encerrado com sucesso.")