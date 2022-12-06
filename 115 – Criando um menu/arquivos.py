import menu

# VERIFICA SE O ARQUIVO EXISTE
def arqExiste(arq):
    try:
        a=open(arq, "rt")
        a.close
    except:
        print("O arquivo não existe.")
        return False
    else:
        print("O arquivo existe.")
        return True

# CRIA O ARQUIVO
def criarArquivo(arq):
    try:
        a=open(arq, "wt")
        a.close
    except:
        print(f"Ocorreu um erro ao criar o arquivo: {TypeError}")
    else:
        print(f"Arquivo {arq} criado com sucesso.")

# MOSTRA OS VALORES DO ARQUIVO
def listarArquivo(arq):
    try:
        a = open(arq, "rt")
    except:
        print(f"ERRO AO LER O ARQUIVO: {TypeError}")
    else:
        menu.cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close

# CADASTRAR PESSOAS
def cadastrarPessoa(arq):
    try:
        a = open(arq, "at")
    except:
        print(f"ERRO AO CADASTRAR: {TypeError}")
    else:
        menu.cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: ")).capitalize()
        idade = menu.leiaInt("Idade: ")
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print(f"ERRO AO ESCREVER NO ARQUIVO: {TypeError}")
        else:
            print(f"{nome} ADICIONADO COM SUCESSO")
            a.close