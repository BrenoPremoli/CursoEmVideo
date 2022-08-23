# nome = str(input('Qual é seu nome? '))
# if nome == 'Breno':
#    print('Que nome lindo você tem!')
# else:
#    print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {:.2f}'.format(m))
print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!') #Condição simplificada
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')