lista = []
cont = 0
opc = 'S'
while True:
    if opc == 'N':
        break
    elif opc == 'S':
        nome = str(input('Nome: '))
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        media = (n1 + n2) / 2
        lista.append([nome, [n1, n2], media])
        cont += 1
    else:
        print('Comando inválido.', end=' ')
    opc = str(input('Deseja continuar [S/N]? ')).strip().upper()
print(f'{"Nº":<4}{"Nome":<15}{"Média":<6}')
for i, a in enumerate(lista):
    print(f'{i+1:<3} {a[0]:<15} {a[2]:<5.2f}')
n = 0
while True:
    n = int(input('Deseja mostrar notas de qual aluno? (Digite 999 para encerrar): '))
    if n <= cont and n > 0:
        print(f'Notas de {lista[n-1][0]}: {lista[n-1][1]}')
    elif n == 999:
        break
    else:
        print('Numero inválido. ', end='')