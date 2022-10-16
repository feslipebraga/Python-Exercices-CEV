# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

def notas(*n, situacao=False):
    dados = {}
    dados["Qtd de notas"] = contadorNotas
    dados['Maior nota'] = max(listaNotas)
    dados['Menor nota'] = min(listaNotas)
    dados['Média'] = sum(listaNotas) / len(listaNotas)
    if situacao:
        if dados['Média'] >= 7:
            dados['Situação'] = "ÓTIMA"
        elif dados['Média'] >= 5:
            dados['Situação'] = "RAZOÁVEL"
        else:
            dados['Situação'] = "RUIM"
    return dados

contadorNotas = 0
listaNotas = []
while True:
    n = int(input("Nota [99 break]: "))
    if n == 99:
        break
    contadorNotas += 1
    listaNotas.append(n)
situacao = input('Deseja saber a situação do aluno? ').lower()[0]
if situacao == 's':
    print(notas(n, situacao=True))
else:
    print(notas(n))