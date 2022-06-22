from datetime import date
ano_atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano
print('Idade do atleta: {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')