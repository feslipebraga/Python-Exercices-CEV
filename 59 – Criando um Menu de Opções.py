'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input("Informe um valor: "))
n2 = float(input("Informe outro: "))
opcao = 0
maior = 0
menor = 0

from time import sleep

while opcao != 5:
    sleep(1)
    print("_" * 30)
    print("""VOCÊ TEM AS SEGUINTES OPÇÕES:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    print("_" * 30)
    opcao = int(input("Qual deseja realizar?\n"))
    if opcao == 1:
        print(f"A soma dos valores: {n1} + {n2} = {n1 + n2}")
    if opcao == 2:
        print(f"A multiplicação dos valores: {n1} x {n2} = {n1 * n2}")
    if opcao == 3:
        if n1 > maior:
            maior = n1
        if n2 > maior:
            maior = n2
        print(f"O maior número informado foi o: {maior}")
    if opcao == 4:
            n1 = float(input("Informe um valor: "))
            n2 = float(input("Informe outro: "))
    if opcao == 5:
        print("Saindo...")
        print("Obrigado por me utilizar =)")