from random import randint
from time import sleep
from operator import itemgetter
pessoa = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)}
rank = {}
for k, v in pessoa.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('\nRANKING')
rank = sorted(pessoa.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º Lugar - {v[0]} tirou {v[1]} no dado.')

