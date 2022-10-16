# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
"onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    numero = int(input("Informe um número de 0 a 20: "))
    if numero >= 0 and numero <= 20:
        break
    else:
        print("Número inválido, tente novamente...")
print(f"O número informado foi o {contagem[numero]}")