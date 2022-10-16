valor_pago = float(input('Informe o valor do produto R$'))

avista = 0.9 * valor_pago
cheque = 0.9 * valor_pago
cartao1x = 0.95 * valor_pago
cartao2x = valor_pago
cartao3xoumais = 1.20 * valor_pago

print(f"""Qual será a forma de pagamento do produto?
[ 1 ] A vista 
[ 2 ] Cheque
[ 3 ] 1x no cartão de crédito ou débito
[ 4 ] 2x no cartão de crédito
[ 5 ] 3x ou mais no cartão de crédito""")
forma_pagamento = int(input("Escolha uma opção: "))

if forma_pagamento == 1:
    print(f"O valor do produto custa R${valor_pago:.2f}, com a forma de pagamento selecionada, o valor passará a ser R${avista:.2f}")
elif forma_pagamento == 2:
    print(f"O valor do produto custa R${valor_pago:.2f}, com a forma de pagamento selecionada, o valor passará a ser R${cheque:.2f}")
elif forma_pagamento == 3:
    print(f"O valor do produto custa R${valor_pago:.2f}, com a forma de pagamento selecionada, o valor passará a ser R${cartao1x:.2f}")
elif forma_pagamento == 4:
    print(f"O valor do produto custa R${valor_pago:.2f}, com a forma de pagamento selecionada, o valor passará a ser R${cartao2x:.2f}")
elif forma_pagamento == 5:
    print(f"O valor do produto custa R${valor_pago:.2f}, com a forma de pagamento selecionada, o valor passará a ser R${cartao3xoumais:.2f}")
else:
    print("Opção inválida. Selecione a correta. De 1 a 5.")
