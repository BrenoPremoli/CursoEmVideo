def ficha(jogador, gols=0):
    return f'\nJogador: {jogador} -> Gols: {gols}'
player = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if player.strip() == '':
    player = '<desconhecido>'
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
print(ficha(player, gol))
# ===========================================================
def ficha(jogador='<desconhecido>', gols=0):
    print(f'\nJogador: {jogador} -> Gols: {gols}')
player = str(input('\nNome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if player.strip() == '':
    ficha(gols=gol)
else:
    ficha(player, gol)