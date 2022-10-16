nome = input("Informe seu nome completo: ")

print("Analisando seu nome...")
print(f"Ele com letras maiusculas: {nome.upper()}")
print(f"Ele com letras minusculas: {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras.")
print(f"O primeiro nome tem {nome.find(' ')} letras")