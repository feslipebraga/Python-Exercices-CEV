# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Informe a distância em km: "))

preco = 0.5 * distancia
preco2 = 0.45 * distancia

if distancia <= 200:
    print(f"O preço a pagar por {distancia}km é R${preco:.2f}")
else:
    print(f"O preço a pagar por {distancia}km é R${preco2:.2f}")