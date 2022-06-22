cont_18 = cont_f = cont_m = 0
sexo = ' '
opc = 'S'
while opc == 'S':
    sexo = opc = ' '
    idade = int(input('Idade: '))
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont_18 += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1
    while opc not in 'SN':
        opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
print(f'Pessoas com mais de 18 anos: {cont_18}')
print(f'Quantidade de homens cadastrados: {cont_m}')
print(f'Quantidade de mulheres com menos de 20 anos: {cont_f}')
# =============================================================================
cont_18 = cont_f = cont_m = 0
while True:
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont_18 += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'Pessoas com mais de 18 anos: {cont_18}')
print(f'Quantidade de homens cadastrados: {cont_m}')
print(f'Quantidade de mulheres com menos de 20 anos: {cont_f}')
