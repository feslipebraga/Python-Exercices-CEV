import menu
import arquivos
from time import sleep

arquivo = "arquivo.txt"

if not arquivos.arqExiste(arquivo):
    arquivos.criarArquivo(arquivo)

while True:
    opcoes = menu.leiaOpcoes(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if opcoes == 1:
        #VER PESSOAS CADASTRADAS
        arquivos.listarArquivo(arquivo)
        sleep(2)

    elif opcoes == 2:
        #CADASTRAR NOVA PESSOA
        arquivos.cadastrarPessoa(arquivo)
        sleep(2)

    elif opcoes == 3:
        menu.cabecalho("SAINDO DO SISTEMA... ATÉ LOGO!")
        sleep(2)
        break

    else:
        sleep(1)