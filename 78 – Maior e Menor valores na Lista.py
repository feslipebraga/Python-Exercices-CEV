# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for posicao in range(5):
    lista.append(int(input(f"Informe um valor para a posição {posicao}: ")))
print(f"Os valores informados foram {lista}")
print(f"O menor valor foi o {min(lista)} na posição {lista.index(min(lista))}")
print(f"O maior valor foi o {max(lista)} na posição {lista.index(max(lista))}")