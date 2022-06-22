from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for i in range(1, 8):
    ano = int(input('Em que ano nasceu a {}ª pessoa? '.format(i)))
    if ano_atual - ano >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print('Maiores de idade: {}'.format(cont_maior))
print('Menores de idade: {}'.format(cont_menor))

