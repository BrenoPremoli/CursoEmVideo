while True:
    n = int(input('\nDigite um número para ver a tabuada: '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} X {i:2} = {n * i}')
print('Programa encerrado.')