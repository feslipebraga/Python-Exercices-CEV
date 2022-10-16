# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

print("ADICIONANDO VALORES A UMA LISTA")
while True:
    numero = int(input("Digite um valor: "))
    if numero not in lista:
        lista.append(numero)
        print("Valor adicionado com sucesso!")
    else:
        print("Número já adicionado anteriormente, tente outro...")
    continuacao = str(input("Deseja continuar? ")).lower()[0]
    if continuacao == "n":
        break
    while continuacao not in "sn":
        print("Dados inválidos, tente novamente.")
        continuacao = str(input("Deseja continuar? ")).lower()[0]
print(f"Você digitou os valores {lista}")