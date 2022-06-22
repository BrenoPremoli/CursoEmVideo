pessoa = []
dado = {}
opc = 'S'
soma_idade = 0
while True:
    if opc == 'N':
        break
    elif opc == 'S':
        dado['nome'] = str(input('Nome: '))
        while True:
            dado['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
            if dado['sexo'] in 'MF':
                break
            else:
                print('Comando inválido. ', end='')
        dado['idade'] = int(input('Idade: '))
        pessoa.append(dado.copy())
        soma_idade += dado['idade']
    else:
        print('Comando inválido.', end=' ')
    opc = str(input('Deseja continuar [S/N]? ')).strip().upper()
print(f'Pessoas cadastradas: {len(pessoa)}')
print(f'Média de idade: {soma_idade/len(pessoa):.1f} anos.')
print('Mulheres cadastradas: ', end='')
for i in pessoa:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}... ', end='')
print('\nLista de pessoas que estão acima da média:')
for i in pessoa:
    if i['idade'] > soma_idade/len(pessoa):
        for k, v in i.items():
            print(f'{k} - {v}', end='; ')
        print()



