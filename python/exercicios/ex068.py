from random import randint
cont_eu = 0
while True:
    n_pc = (randint(0, 10))
    n_eu = int(input('Digite um valor: '))
    if n_eu > 10 or n_eu < 0:
        print('Valor inválido.')
        break
    eu = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    soma = n_eu + n_pc
    if eu == 'P' or eu == 'I':
        if eu == 'P':
            comp = 'I'
        else:
            comp = 'P'
        if eu == 'P' and soma % 2 == 0:
            print(f'Você jogou {n_eu} e o computador {n_pc}. Deu PAR -> {soma}. \nVocê VENCEU!')
            cont_eu += 1
        elif eu == 'I' and soma % 2 != 0:
            print(f'Você jogou {n_eu} e o computador {n_pc}. Deu ÍMPAR -> {soma}. \nVocê VENCEU!')
            cont_eu += 1
        elif eu == 'I' and soma % 2 == 0:
            print(f'Você jogou {n_eu} e o computador {n_pc}. Deu PAR -> {soma}. \nVocê PERDEU!')
            break
        elif eu == 'P' and soma % 2 != 0:
            print(f'Você jogou {n_eu} e o computador {n_pc}. Deu ÍMPAR -> {soma}. \nVocê PERDEU!')
            break
    else:
        print('Comando inválido.')
print(f'Total de vitórias consecutivas: {cont_eu}')
# ==================================================================================================
print()
cont_eu = 0
while True:
    n_eu = int(input('Digite um valor: '))
    n_pc = (randint(0, 10))
    soma = n_eu + n_pc
    eu = ' '
    while eu not in 'PI':
        eu = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {n_eu} e o computador {n_pc}. Total: {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if eu == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont_eu += 1
        else:
            print('Você PERDEU!')
            break
    elif eu == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont_eu += 1
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print(f'Total de vitórias consecutivas: {cont_eu}')


