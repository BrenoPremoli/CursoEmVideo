largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Área da parede: {:.2f}m² \nLitro(s) de tinta(s) necessário(s): {:.2f}L'.format(area, tinta))