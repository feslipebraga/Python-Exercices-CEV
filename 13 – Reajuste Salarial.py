# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe seu salário: R$"))
salario_com_aumento = salario * 1.15
print(f"O valor do salário com 15% de aumento é R${salario_com_aumento:.2f}")