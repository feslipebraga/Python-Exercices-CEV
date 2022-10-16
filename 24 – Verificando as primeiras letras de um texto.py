cidade = input("Informe o nome de uma cidade: ").upper()
santo = cidade[0:5]

if 'SANTO' in santo:
    print("A cidade começa com 'SANTO'")
else:
    print("Não tem 'SANTO' na cidade informada")