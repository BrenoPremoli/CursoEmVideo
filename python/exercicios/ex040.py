n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
media = (n1 + n2) / 2
print('Valor da média: {}'.format(media))
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')