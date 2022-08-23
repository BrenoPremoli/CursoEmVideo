n = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(f'Valores digitados: {n}')
print(f'O valor 9 aparece {n.count((9))} vezes')
if 3 in n:
    print(f'Primeiro valor 3 está na posição: {(n.index(3)+1)}')
else:
    print('O valor 3 não foi digitado.')
print('Valores pares: ', end = '')
for i in range(len(n)):
    if n[i] % 2 == 0:
        print(n[i], end=' ')