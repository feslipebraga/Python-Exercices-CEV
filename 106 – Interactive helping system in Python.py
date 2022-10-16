# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

from time import sleep

def msg(texto):
    tamanho = len(texto) + 4
    print('=' * tamanho)
    print(f"  {texto}")
    print('=' * tamanho)

def ajuda(txt):
    help(txt)

msg("SISTEMA DE AJUDA PYHELP")
while True:
    x = input("Função ou Biblioteca: ")
    print(f"Acessando o manual do comando '{x}'")
    sleep(1)
    ajuda(x)
    if x == "fim":
        msg("ATÉ LOGO!")
        break