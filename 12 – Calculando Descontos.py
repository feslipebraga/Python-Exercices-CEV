# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe um valor R$"))
valor_com_desconto = preco * 0.95
print(f"O preço com 5% de desconto é R${valor_com_desconto:.2f}")