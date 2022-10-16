import random 
numeros = []
aux = []
jogadas = int(input("Quantos palpites para a mega sena serão gerados? "))
x = 0
while x < jogadas:
    for c in range(6):
        numero = random.randint(1, 60)
        aux.append(numero)
        aux.sort()
    numeros.append(aux[:])
    aux.clear()
    x += 1 
print()
for x, y in enumerate(numeros):
    print(f"PALPITE {x+1}: {y}")