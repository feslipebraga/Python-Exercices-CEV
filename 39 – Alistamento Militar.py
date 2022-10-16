# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nasc = int(input("Informe seu ano de nascimento: "))
idade = 2022 - ano_nasc

if idade < 18:
    print(f"Você tem {idade} anos. Ainda não está na hora de alistar-se. Falta(m) {18 - idade} ano(s) para chegar a hora")
if idade == 18:
    print(f"Você tem {idade} anos. Já está na hora de alistar-se")
if idade > 18:
    print(f"Você tem {idade} anos. Já passou da hora de alistar-se.")