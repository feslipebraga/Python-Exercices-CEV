# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    idade = 2022 - ano
    if idade < 16:
        return f"{idade} anos. Você não tem idade para votar, espere mais um pouco..." 
    if idade >= 16 and idade < 18:
        return f"{idade} anos. Seu voto é opcional =]" 
    if idade >= 18:
        return f"{idade} anos. Seu voto obrigatório, exerça sua cidadania!" 
    

anoNascimento = int(input("Ano de nascimento: "))
print(voto(anoNascimento))