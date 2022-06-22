from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10))
print(f'Números sorteados: {n}')
x = sorted(n)
print(f'Maior valor: {x[4]}')  # print(f'Maior valor: {max(n)}')
print(f'Menor valor: {x[0]}')  # print(f'Menor valor: {min(n)}')
