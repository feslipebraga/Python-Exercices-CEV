# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

def aumento(p, t):
    x = p + (p * t/100)
    return x 

def diminuicao(p, t):
    x = p - (p * t/100)
    return x

def dobro(p):
    x = p * 2
    return x

def metade(p):
    x = p / 2
    return x

def cifrao(p, cifrao='R$'):
    return f'{cifrao}{p:.2f}'.replace('.', ',')