def leiaDinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input(valor)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"ERRO! '{entrada}' NÃO É UM VALOR VÁLIDO.")
        else:
            valido = True
            return float(entrada)