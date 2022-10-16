# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("*" * 10, "TABUADA", "*" * 10)
numero = int(input("Informe um número: "))
for c in range(1, 11):
    print(f"{c} x {numero} = {c * numero}")