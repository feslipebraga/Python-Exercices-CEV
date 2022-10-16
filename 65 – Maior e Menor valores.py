# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = soma = maior = menor = 0

while True:
    numero = int(input("Número: "))
    contador = contador + 1
    soma = soma + numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuacao = input("Deseja continuar? [s/n] ").upper()[0]
    if continuacao == "N":
        break
media = soma / contador
print(f"Você digitou {contador} números no total")
print(f"A média entre os números é {media}")
print(f"O maior número é o {maior} e o menor é o {menor}")