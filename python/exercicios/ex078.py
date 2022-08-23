n = []
maior = 0
menor = 0
for i in range(5):
    n.append(int(input(f'Digite um valor para a posição {i}: ')))
print(f'\nValores digitados: {n}')
print('Maior valor: ', end='')
for i in range(5):
    if i == 0:
        maior = n[i]
    else:
        if maior < n[i]:
            maior = n[i]
print(f'{maior}. Posição: ', end='')
for i in range(5):
    if maior == n[i]:
        print(f'{i}...', end='')
print('\nMenor valor: ', end='')
for i in range(5):
    if i == 0:
        menor = n[i]
    else:
        if menor > n[i]:
            menor = n[i]
print(f'{menor}. Posição: ', end='')
for i in range(5):
    if menor == n[i]:
        print(f'{i}...', end='')
print('\n')
# =================================================================
n = []
maior = 0
menor = 0
for i in range(5):
    n.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = n[i]
    else:
        if maior < n[i]:
            maior = n[i]
        if menor > n[i]:
            menor = n[i]
print(f'\nValores digitados: {n}')
print(f'Maior valor: {maior}. Posição: ', end='')
for i, j in enumerate(n):
    if maior == j:
        print(f'{i}...', end='')
print(f'\nMenor valor: {menor}. Posição: ', end='')
for i, j in enumerate(n):
    if menor == j:
        print(f'{i}...', end='')