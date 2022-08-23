sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = input(str('Dado inválido. Tente novamente. Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))