# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(p, t):
    x = p + (p * t/100)
    return x

def diminuir(p, t):
    x = p - (p * t/100)
    return x

def dobro(p):
    x = p * 2
    return x

def metade(p):
    x = p / 2
    return x