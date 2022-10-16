import random
n1 = input('Primeira pessoa: ')
n2 = input('Segunda pessoa: ')
n3 = input('Terceira pessoa: ')
n4 = input('Quarta pessoa: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(f'A sequência da lista é: {lista}')