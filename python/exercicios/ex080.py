n = []
for i in range(5):
    x = int(input('Digite um número: '))
    n.append(x)
    if i == 0:
        print('Adicionado ao final da lista.')
    elif n[i-1] > n[i]:
        n.sort()
        for i in range(len(n)):
            if x == n[i]:
                print(f'Adicionado a posição {i} da lista.')
                print(n)
                break
    else:
        print('Adicionado ao final da lista.')
print(f'Valores digitados: {n}\n')
# =================================================================
n = []
for i in range(5):
    x = int(input('Digite um número: '))
    if i == 0 or x > n[i-1]:
        n.append(x)
        print('Adicionado ao final da lista.')
    else:
        for i in range(len(n)):
            if x < n[i]:
                n.insert(i, x)
                print(f'Adicionado a posição {i} da lista.')
                print(n)
                break
print(f'Valores digitados: {n}')