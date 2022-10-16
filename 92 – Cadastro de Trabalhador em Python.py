# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
 
from datetime import datetime

anoAtual = datetime.now().year

dados = {}

dados["nome"] = input("Nome: ")
dados["anoNascimento"] = int(input("Ano de nascimento: "))
dados["ctps"] = int(input("CTPS (0 se não tem): "))
dados["idade"] = anoAtual - dados["anoNascimento"]

if dados["ctps"] != 0:
    dados["anoContratacao"] = int(input("Ano de contratação: "))
    dados["salario"] = int(input("Salário: "))
    dados["aposentadoria"] = dados["idade"] + ((dados["anoContratacao"] + 35) - anoAtual)

for k, v in dados.items():
    print(f"{k} = {v}")