impar = []
par = []
all = []
n = int(input('Digite um valor: '))
while True:
    all.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    opc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if opc == 'N':
        break
    elif opc == 'S':
        n = int(input('Digite um valor: '))
    else:
        print('Comando inválido.', end=' ')
print(f'Lista completa: {all}')
print(f'Lista de pares: {par}')
print(f'Lista de ímpares: {impar}')