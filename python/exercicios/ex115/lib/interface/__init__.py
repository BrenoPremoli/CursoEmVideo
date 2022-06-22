def linha(tam = 42):
    return '=' * tam


def cabe(opc):
    print(linha())
    print(opc.center(42))
    print(linha())


def menu(lista):
    cabe('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[033m{c}\033[m - \033[36m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaOpc('\033[1;33mOpção: \033[m')
    return opc


def leiaOpc(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO - Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nERRO - O usuário não informou o número!\033[m')
            return 0
        else:
            return n