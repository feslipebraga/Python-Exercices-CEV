# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

a1 = int(input("Informe o 1nd termo da PA: "))
razao = int(input("Informe a razão: "))
termo = a1
x = 0
while x < 10:
    print(termo)
    x += 1
    termo = termo + razao
    
# an = a1 + n-1 * razao
# A{x} = a1 + ((x - 1) * razao)