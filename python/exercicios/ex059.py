from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
esc = 0
while esc != 5:
    print('=='*15)
    print('Menu de opções:')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    print('=='*15)
    esc = int(input('Digite uma opção: '))
    if esc == 1:
        soma = n1 + n2
        print('Resultado da soma {} + {} = {}'.format(n1, n2, soma))
    elif esc == 2:
        mult = n1 * n2
        print('Resultado da multiplicação {} X {} = {}'.format(n1, n2, mult))
    elif esc == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} é igual a {}'.format(n1, n2))
    elif esc == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif esc == 5:
        sleep(1)
        print('Saindo...')
    else:
        esc = int(input('Opção inválida. Tente novamente: '))