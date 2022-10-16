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

def resumo(p, a, d):
    print('=' * 35)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 35)
    print(f"Preço analisado: \t{moeda(p)}")
    print(f"Dobro do preço: \t{dobro(p, True)}")
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f"{a}% de aumento: \t{aumentar(p, a, True)}")
    print(f"{d}% de redução: \t{diminuir(p, d, True)}")
    print('=' * 35)