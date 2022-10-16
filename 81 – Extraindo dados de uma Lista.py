# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    numero = int(input("Informe um número: "))
    lista.append(numero)
    continuar = str(input("Deseja continuar? ")).lower()[0]
    while continuar not in "sn":
        print("Opção inválida, tente novamente...")
        continuar = str(input("Deseja continuar? ")).lower()[0]
    if continuar == "n":
        break
print(f"Sua lista: {lista}")
print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)     # Não conseguimos colocar a funcão formatada dentro do print, nem criar uma variavel.
print(f"Sua lista em ordem decrescente {lista}")
if 5 in lista:
    print("Você digitou o número 5")
else:
    print("Você não digitiou o 5!")