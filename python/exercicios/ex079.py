n = []
while True:
    x = int(input('Digite um valor: '))
    if x not in n:
        n.append(x)
        print('Valor Adicionado.')
    else:
        print('Valor duplicado. Não será adicionado.')
    opc = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
    if opc == 'N':
        break
    elif opc != 'S':
        opc = str(input('Comando inválido. Deseja continuar (S/N)? ')).upper().strip()[0]
print(40 * '=')
n.sort()
print(f'Valores adicionados: {n}')