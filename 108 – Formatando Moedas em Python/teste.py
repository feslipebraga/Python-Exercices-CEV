import moeda

numero = int(input("Digite um valor: R$"))
print(f"A metade de {moeda.cifrao(numero)} é {moeda.cifrao(moeda.metade(numero))}")
print(f"O dobro de {moeda.cifrao(numero)} é {moeda.cifrao(moeda.dobro(numero))}")
print(f"Aumentando 10% de {moeda.cifrao(numero)} fica {moeda.cifrao(moeda.aumento(numero, 10))}")
print(f"Diminuindo 10% de {moeda.cifrao(numero)} fica {moeda.cifrao(moeda.diminuicao(numero, 10))}")