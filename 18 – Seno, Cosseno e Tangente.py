# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

angulo = int(input("Digite um angulo: "))

import math

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"""O angulo de {angulo} Graus convertido para
Seno é: {seno:.2f}
Cosseno: {cosseno:.2f}
Tangente: {tangente:.2f}""")