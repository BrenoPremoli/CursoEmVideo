matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_linha = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = (int(input(f'Digite um valor para [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_coluna += matriz[i][j]
        if i == 1:
            if maior_linha == 0 or maior_linha < matriz[i][j]:
                maior_linha = matriz[i][j]
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^6}]', end='')
    print()
print(f'Soma dos pares: {soma_pares}')
print(f'Soma da terceira coluna: {soma_coluna}')
print(f'Maior valor da segunda linha: {maior_linha}')