import moeda

numero = int(input('Informe um valor: R$'))
print(f"O dobro de {numero} é {moeda.dobro(numero)}")
print(f"A metade de {numero} é {moeda.metade(numero)}")
print(f"Aumentando 10% de {numero} temos {moeda.aumentar(numero, 10)}")
print(f"Dimuniundo 10% de {numero} temos {moeda.diminuir(numero, 10)}")