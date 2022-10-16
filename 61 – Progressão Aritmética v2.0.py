# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = float(input("Informe o 1nd termo da PA: "))
razao = float(input("Informe a razão: "))
x = 0
calculo = a1 + ((x - 1) * razao)
while x < 10:
    x += 1
    print(f"A{x} = {a1 + ((x - 1) * razao)}")

# an = a1 + n-1 * razao