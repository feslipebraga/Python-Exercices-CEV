# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Informe o valor do seu salário R$"))

aumento1 = salario * 1.1
aumento2 = salario * 1.15

if salario > 1250:
    print(f"Você recebeu um aumento de 10%, o valor final ficou: R${aumento1:.2f}")
else:
    print(f"Você recebeu um aumento de 15%, o valor final ficou: R${aumento2:.2f}")