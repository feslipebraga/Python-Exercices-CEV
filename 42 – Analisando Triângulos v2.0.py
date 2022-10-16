a = float(input("Informe o valor da primeira reta: "))
b = float(input("Informe o valor da segunda reta: "))
c = float(input("Informe o valor da terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    print("Os valores das retas acima podem formar um triangulo")
    if a == b and b == c:
        print("O triângulo tem os 3 lados iguais e é EQUILÁTERO.")
    elif a == b and c != a or a == c and b != a or b == c and a != b:
        print("O triângulo tem 2 lados iguais e 1 diferente, é ISÓSCELES")
    elif a != b and b != c:
        print("O triângulo tem 3 lados diferentes, é ESCALENO")
else:
    print("Os valores NÃO podem formar um triangulo")