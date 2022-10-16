# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ("Água mineral 1,5l", 6.49,
"Coca diet 2l", 11.79,
"Cheetos", 9.99,
"Xícara personalizada", 14.99,
"Leite em pó 400g", 21.99)

linha = "-" * 40

print(linha)
print(f'{"LISTAGEM DE PREÇOS"}'.center(40))
print(linha)
for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f"{tupla[posicao]:<30}", end=" ")
    else:
        print(f"R${tupla[posicao]:>6.2f}")
print(linha)