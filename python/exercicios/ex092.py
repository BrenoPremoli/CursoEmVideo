from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 - não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contrato'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposenta'] = pessoa['idade'] + (pessoa['contrato'] + 35) - datetime.now().year
print('\nDADOS')
for k, v in pessoa.items():
    print(f'{k}: {v}')