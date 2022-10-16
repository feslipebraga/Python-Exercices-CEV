# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Informe a velocidade: "))
taxa = 7 * (velocidade - 80)

if velocidade > 80:
    print(f"Você ultrapassou a velocidede permitida!")
    print(f"Será necessário pagar uma multa de R${taxa:.2f}")
else:
    print("Boa viagem!")