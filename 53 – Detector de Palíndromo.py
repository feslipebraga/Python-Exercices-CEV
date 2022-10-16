# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Frase: ").upper().replace(" ", "")

inverso = ''

for letra in range(len(frase) -1, -1, -1):
    inverso = inverso + frase[letra]

print(f"Sua frase: {frase}")
print(f"Sua frase ao contrário: {inverso}")

if frase == inverso:
    print("É Palíndromo")
else:
    print("Não é palíndromo")