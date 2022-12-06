# FAZ LEITURA DE UM INTEIRO
def leiaInt(n):
    while True:
        try:
            num = int(input(n))
        except:
            print("ERRO: Digite uma opção válida...")
        else:
            return num

# CRIA UMA LINHA
def linha():
    tam = 40
    print("-" * tam)

# CRIA 2 LINHAS COM UMA MENSAGEM CENTRALIZADA NO MEIO
def cabecalho(txt):
    linha()
    print(txt.center(40))
    linha()

# CRIA O MENU DE OPCÕES NUMERADOS ATRAVÉS DE UMA LISTA
def leiaOpcoes(lista):
    cabecalho("MENU PRINCIPAL")
    for c, v in enumerate(lista):
        print(f"{c+1} - {v}")
    linha()
    opcao = leiaInt("Sua opção: ")
    return opcao                        # RETORNA O VALOR DE "OPCAO" PARA A VARIAVEL "OPCOES" NO SISTEMA.
