people = []
dado = []
maior = menor = 0
opc = 'S'
while True:
    if opc == 'N':
        break
    elif opc == 'S':
        dado.append(str(input('Nome: ')))
        dado.append(float(input('Peso [Kg]: ')))
        if len(people) == 1:
            maior = menor = dado[1]
        if maior < dado[1]:
            maior = dado[1]
        if menor > dado[1]:
            menor = dado[1]
        people.append(dado[:])
        dado.clear()
    else:
        print('Comando inválido.', end=' ')
    opc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
print(f'Total de pessoas cadastradas: {len(people)}')
print(f'Maior peso: {maior:.2f} Kg. Peso de ', end='')
for i in people:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print(f'\nMenor peso: {menor:.2f} Kg. Peso de ', end='')
for i in people:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')