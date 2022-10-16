import moedas 

numero = int(input("Valor: R$ "))
print(f"A metade de {moedas.moeda(numero)} é {moedas.metade(numero, True)}")
print(f"O dobro de {moedas.moeda(numero)} é {moedas.dobro(numero, True)}")
print(f"Aumentando 10% de {moedas.moeda(numero)} = {moedas.aumentar(numero, 10, True)}")
print(f"Diminuindo 10% de {moedas.moeda(numero)} = {moedas.diminuir(numero, 10, True)}")