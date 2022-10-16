# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

def aumentar(p, t, f=False):
    x = p + (p * t/100)
    return x if not f else moeda(x)

def diminuir(p, t, f=False):
    x = p - (p * t/100)
    return x if not f else moeda(x)

def dobro(p, f=False):
    x = p * 2
    return x if not f else moeda(x)

def metade(p, f=False):
    x = p / 2
    return x if not f else moeda(x)

def moeda(p, cifrao='R$'):
    return f'{cifrao}{p:.2f}'.replace('.', ',')
