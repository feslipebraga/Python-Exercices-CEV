# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
impar = []
par = []

print("Digite um número negativo para parar o programa")

while True:
    numero = int(input("Informe um valor: "))
    if numero < 0:
        break
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    elif numero % 2 == 1:
        impar.append(numero)

print(f"""As listas foram criadas.
LISTA COM TODOS OS NUMEROS: {lista}
NÚMEROS PARES: {par}
NÚMEROS ÍMPARES: {impar}""")