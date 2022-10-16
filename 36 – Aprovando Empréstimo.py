# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Informe o valor da casa: "))
salario_comprador = float(input("Informe seu salario: "))
tempo = int(input("Em quantos anos você quer pagar? "))

mensalidade = casa / (tempo * 12)
trintaporcento = 0.3 * salario_comprador

if mensalidade > trintaporcento:
    print("Empréstimo negado.")
    print(f"O valor da mensalidade é R${mensalidade}")
    print(f"30 % do seu salário é menor que o valor da mensalidade. R${trintaporcento}")
else:
    print("Empréstimo aprovado.")
    print(f"O valor da mensalidade é R${mensalidade}")
    print(f"30 % do seu salário é maior que o valor da mensalidade. R${trintaporcento}")