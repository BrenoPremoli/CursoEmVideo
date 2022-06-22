from datetime import date
ano_atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano
if idade < 18:
    faltam = 18 - idade
    ano_faltam = faltam + ano_atual
    print('Você ainda irá se alistar no serviço militar futuramente. Falta {} ano(s).'.format(faltam))
    print('Seu alistamento será em: {}'.format(ano_faltam))
elif idade > 18:
    passou = idade - 18
    ano_passou = ano_atual - passou
    print('Já Passou do tempo de seu alistamento. Atrasou {} ano(s).'.format(passou))
    print('Seu alistamento era pra ter sido em: {}'.format(ano_passou))
else:
    print('Já é a hora de se alistar no exército. Você tem {} anos.'.format(idade))
    print('Seu alistamento é neste ano.')