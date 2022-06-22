n = []
n.append(int(input('Digite um valor: ')))
while True:
    opc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if opc == 'N':
        break
    elif opc == 'S':
        n.append(int(input('Digite um valor: ')))
    else:
        print('Comando inválido.', end=' ')
print(f'Quantidade de elementos digitados: {len(n)}')
n.sort(reverse=True)
print(f'Valores em ordem decrescente: {n}')
if 5 in n:
    print('O valor 5 foi encontrado na lista :)')
else:
    print('O valor 5 não foi encontrado na lista :(')