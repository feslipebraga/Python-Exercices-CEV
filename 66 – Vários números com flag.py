# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

contador = soma = 0

while True:
    numero = int(input("Número: "))
    if numero == 999:
        break
    contador = contador + 1
    soma = soma + numero
    
print(f"{contador} numeros foram digitados")
print(f"{soma} é a soma entre eles")