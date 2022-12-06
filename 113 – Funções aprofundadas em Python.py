# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(valor):
    while True:
        try:
            x = int(input(valor))
        except:
            print('\033[31mERRO. Digite um número INTEIRO válido.\033[m')
            print(f'\033[31mTipo de erro: {Exception.__class__}\033[m')
            continue
        else:
            return x

def leiaFloat(valor):
    while True:
        try:
            x = float(input(valor))
        except:
            print('\033[31mERRO. Informe um valor REAL válido.\033[m')
            print(f'\033[31mMotivo do ERRO: {Exception.__class__}\033[m')
        else:
            return x

n1 = leiaInt('Informe um número inteiro: ')
n2 = leiaFloat('Informe um número real: ')
print(f"Inteiro: {n1}")
print(f"Real: {n2}")

