pessoa = {}
gols = []
pessoa['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {pessoa["nome"]} jogou? '))
for i in range(partidas):
    gol = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(gol)
pessoa['gols'] = gols[:]
pessoa['total'] = sum(gols)
print('=='*30)
print(pessoa)
print('=='*30)
for k, v in pessoa.items():
    print(f'{k} - {v}')
print('=='*30)
print(f'O jogador {pessoa["nome"]} jogou {len(pessoa["gols"])} partidas.')
for i in range(partidas):
    print(f'Na partida {i+1} - {gols[i]} gols.')
print(f'Total de gols: {pessoa["total"]}')