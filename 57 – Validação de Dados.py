# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Informe o sexo [M/F]: ").strip().capitalize()[0]

while sexo not in "MF":
    print("Dados incorretos.")
    sexo = input("Informe o sexo [M/F]: ").strip().capitalize()[0]

if sexo == "M":
    print("Sexo MASCULINO registrado com sucesso.")
if sexo == "F":
    print("Sexo FEMININO registrado com sucesso.")