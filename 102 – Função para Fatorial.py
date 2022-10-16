# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    f = 1
    print(f"O fatorial do número {num}! é =", end=" ")
    if show == "s":
        show = True
        for x in range(num, 0, -1):
            f *= x
            if x > 1:
                print(f"{x} x", end=" ")
            else:
                print(f"{x} = {f}", end=" ")

numero = int(input("Informe um valor para saber seu fatorial: "))
show = input("Deseja mostrar o resultado? ").lower()[0]
fatorial(numero, show)