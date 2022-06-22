cont = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m{}\033[m'.format(i), end=' ')
        cont += 1
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')
print('\n{} foi dividido {} vezes.'.format(n, cont))
if cont == 2:
    print('{} é um número primo.'.format(n))
else:
    print('{} não é um número primo.'.format(n))