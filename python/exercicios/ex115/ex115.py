from lib.interface import *
from lib.arquivo import *
from time import sleep
arq = 'arquivo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    res = menu(['Ver cadastros', 'Novo cadastro', 'Sair'])
    if res == 1:  # listar o conteúdo do arquivo
        lerArquivo(arq)
    elif res == 2:  # cadastrar nova pessoa
        cabe('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaOpc(('Idade: '))
        cadastrar(arq, nome, idade)
    elif res == 3:
        cabe('Encerrando...')
        break
    else:
        print('\033[0;31mERRO - Digite uma opção válida!\033[m')
    sleep(1)