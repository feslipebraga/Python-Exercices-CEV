# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input("Informe a km percorrida: "))
dias_alugados = int(input("Por quantos dias o carro foi alugado: "))
preco = (60 * dias_alugados) + (0.15 * km_percorrido)
print(f"O valor a pagar pelo aluguel do aluguel é de R${preco}")