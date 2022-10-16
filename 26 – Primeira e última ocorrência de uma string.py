frase = input("Informe uma frase: ").lower()

letra_A = frase.count("a")
posicao_A_inicio = frase.find("a")
posicao_A_final = frase.rfind("a")

print(f"Aparece {letra_A} vezes a letra 'A'")
print(f"A primeira letra A está na posição {posicao_A_inicio + 1}")
print(f"A ultima letra A está na posição {posicao_A_final + 1}")