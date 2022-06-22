times = ('Corinthians', 'Palmeiras', 'São Paulo','Internacional',
         'Athletico-PR', 'Atlético-MG', 'Coritiba', 'Fluminense',
         'América-MG','Santos', 'Bragantino', 'Ceará', 'Goiás',
         'Atlético-GO','Flamengo', 'Botafogo', 'Cuiabá', 'Avaí',
         'Juventude', 'Fortaleza')
print(f'Lista de times do Brasileirão: {times}\n')
print(f'Os 5 primeiros são: {times[0:5]}\n')
print(f'Os últimos 4 são: {times[-4:]}\n')
print(f'Em ordem alfabética: {sorted(times)}\n')
for i in range(0, len(times)):
    if times[i] == 'Botafogo':
        x = i + 1
        print(f'O Botafogo está na {x}ª posição.')
print(f'O Botafogo está na {times.index("Botafogo")+1}ª posição.')
