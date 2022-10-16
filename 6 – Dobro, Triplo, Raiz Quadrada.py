# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
numero = int(input("Digite um número: "))
dobro = 2 * numero
triplo = 3 * numero
raiz = math.sqrt(numero)
print(f"""O dobro do valor: {dobro}
O triplo: {triplo}
A raiz quadrada: {raiz}""")