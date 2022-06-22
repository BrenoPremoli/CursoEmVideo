pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Média do {pessoa["nome"]}: '))
print('='*15,' ANÁLISE ','='*15)
if pessoa['media'] < 5:
    pessoa['situacao'] = 'Reprovado'
elif pessoa['media'] >= 5 and pessoa['media'] < 7:
    pessoa['situacao'] = 'Recuperação'
else:
    pessoa['situacao'] = 'Aprovado'
for k, v in pessoa.items():
    print(f'{k}: {v}')