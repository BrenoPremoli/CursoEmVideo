from time import sleep
def contar(i, f, g):
    if g < 0:
        g *= -1
    if g == 0:
        g = 1
    print(f'\nContagem de {i} até {f} de {g} em {g}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += g
            sleep(0.25)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= g
            sleep(0.25)
contar(1, 10, 1)
contar(10, 0, 2)
print('\nAgora é sua vez de personalizar.')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contar(inicio, fim, passo)