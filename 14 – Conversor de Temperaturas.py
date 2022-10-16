# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_C = float(input("Informe uma temperatura em graus Celsius: "))
conversor = (temperatura_C * 1.8) + 32
print(f"{temperatura_C}°C em Fahrenheit é {conversor}°F")