from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
opcao = int(input('Escolha \n[0] - PEDRA \n[1] - PAPEL \n[2] - TESOURA \nDIGITE: '))
if opcao >= 0 and opcao <= 2:
    print('=' * 24)
    print('O computador tirou {}'.format(itens[pc]))
    print('O jogador tirou {}'.format(itens[opcao]))
    print('=' * 24)
else:
    print('Opção inválida.')
if pc == 0:
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('Vitória do JOGADOR')
    elif opcao == 2:
        print('Vitória do PC')
if pc == 1:
    if opcao == 0:
        print('Vitória do PC')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('Vitória do JOGADOR')
elif pc == 2:
    if opcao == 0:
        print('Vitória do JOGADOR')
    elif opcao == 1:
        print('Vitória do PC')
    elif opcao == 2:
        print('EMPATE')