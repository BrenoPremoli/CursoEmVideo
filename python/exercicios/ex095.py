time = []  # lista
pessoa = {}  # dicionário dentro - lista
gols = []  # lista dentro - dicionário
opc = 'S'
while True:
    if opc == 'N':
        break
    elif opc == 'S':
        pessoa.clear()
        gols.clear()
        pessoa['nome'] = str(input('Nome do jogador: '))
        partidas = int(input(f'Quantas partidas {pessoa["nome"]} jogou? '))
        for i in range(partidas):
            gol = int(input(f'Quantos gols na partida {i + 1}? '))
            gols.append(gol)
        pessoa['gols'] = gols[:]
        pessoa['total'] = sum(gols)
        time.append(pessoa.copy())
    else:
        print('Comando inválido. ', end='')
    opc = str(input('Deseja continuar [S/N]? ')).strip().upper()
print('=='*30)
print('cod     ', end=' ')
for i in pessoa.keys():
    print(f'{i:<17}', end='')
for i, j in enumerate(time):
    print(f'\n{i+1:<9}', end='')
    for k in j.values():
        print(f'{str(k):<17}', end='')
print()
while True:
    n = int(input('Deseja mostrar dados de qual jogador? (Digite 999 para encerrar): '))
    if n <= len(time) and n > 0:
        print(f'DADOS DO JOGADOR -> {time[n-1]["nome"]}')
        for i, j in enumerate(time[n-1]["gols"]):
            print(f'Partida {i + 1} - {j} gols.')
    elif n == 999:
        break
    else:
        print('Numero inválido. ', end='')