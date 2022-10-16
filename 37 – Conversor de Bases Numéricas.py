# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Informe um número inteiro: "))
conversor = int(input("""Para qual base você deseja converter o número?
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL\n"""))

if conversor == 1:
    print(f"O numero {numero} convertido para binario é {bin(numero)[2:]}")
elif conversor == 2:
    print(f"O numero {numero} convertido para octal é {oct(numero)[2:]}")
elif conversor == 3:
    print(f"O numero {numero} convertido para hexadecimal é {hex(numero)[2:]}")
else:
    print("Opção inválida.")