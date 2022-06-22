galera = list()
dado = list()
totmenos = totmais = 0
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade com {i[1]} anos.')
        totmenos += 1
    else:
        print(f'{i[0]} é menor de idade com {i[1]} anos.')
        totmais += 1
print(f'Maiores de idade: {totmenos}')
print(f'Menores de idade: {totmais}')