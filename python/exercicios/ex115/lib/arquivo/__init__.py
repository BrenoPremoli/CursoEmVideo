from exercicios.ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO - Criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(msg):
    try:
        a = open(msg, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabe('CADASTRO DE PESSOAS')
        for lin in a.readlines():
            nome, idade = lin.strip().split(';')
            print(f'{nome:<30}{idade:>3} anos.')
        a.close()



def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO - Abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO - Escrita dos dados!')
        else:
            print(f'Novo cadastro de {nome} criado.')
            a.close()
