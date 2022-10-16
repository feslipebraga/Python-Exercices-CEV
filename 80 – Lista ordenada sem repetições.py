# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção. No final, mostre a lista ordenada na tela.

list = []

for i in range(5):
    number = int(input(f"Informe o {i + 1} valor: "))
    if number not in list:
        list.append(number)
        print(f"O valor foi adicionado à lista.")
    else:
        while number in list:
            print("Número duplicado, tente outro...")
            number = int(input(f"Informe o {i + 1} valor: "))
        if number not in list:
            list.append(number)
print(sorted(list))