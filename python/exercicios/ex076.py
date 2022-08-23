preco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
for i in range(len(preco)):
    if i % 2 == 0:
        print(f'{preco[i]:.<30}', end='')
    else:
        print(f'R$ {preco[i]:>6.2f}')
print('='*40)