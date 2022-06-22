pessoa = {'nome': 'Breno', 'sexo': 'M', 'idade': 18}
del pessoa['sexo'] # apagar
pessoa['nome'] = 'Bryan'
pessoa['peso'] = 86.4
for k, v in pessoa.items():
    print(f'{k} = {v}')
print()
# =========================================================
estado = dict()
brasil = list()
for i in range(3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for i in brasil:
    for k, v in i.items():
        print(f'{k} - {v}')
