peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.1f}")

if imc <= 18.5:
    indice = "abaixo do peso"
elif imc <= 25:
    indice = "peso ideal"
elif imc <= 30:
    indice = "sobrepeso"
elif imc <= 40:
    indice = "obesidade"
else:
    indice = "obesidade mórbida"
print(f"A faixa de IMC dessa pessoa está em: {indice}")