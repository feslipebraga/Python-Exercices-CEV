# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input("Digite um número: ")),
int(input("Digite outro número: ")),
int(input("Digite mais um número: ")),
int(input("Digite o último número: ")))

print(f"Você digitou os valores {numeros}")

print(f"O número 9 aparece {numeros.count(9)} vezes")       # count conta a qtd de num ou str solicitadas
if 3 in numeros:
    print(f"O primeiro valor 3 encontra-se na posição {numeros.index(3)+1}")
else:
    print("Não foi digitado o valor 3")
print(f"Os números pares digitados foram", end=" ")
for n in numeros:
    if n % 2 == 0:
        print(f"{n}", end=" ")