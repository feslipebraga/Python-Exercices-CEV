# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]        # lista[0] = pares, lista[1] = impares.

for c in range(3):
    valor = int(input("Valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f"Os valores pares são {lista[0]} e os ímpares {lista[1]}")