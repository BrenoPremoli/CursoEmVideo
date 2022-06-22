import datetime
atual = datetime.datetime.now()
ano = int(input('Digite o ano a ser analisado (coloque "0" para analisar o ano atual): '))
if ano == 0:
    ano = atual.year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{:.0f} é bissexto.'.format(ano))
else:
    print('{:.0f} não é bissexto.'.format(ano))
