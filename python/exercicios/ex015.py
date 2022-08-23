km = float(input('Quantidade de Km percorridos pelo carro: '))
dia = int(input('Quantidade de dias que o carro foi alugado: '))
precoKm = km * 0.15
precoDia = dia * 60
total = precoKm + precoDia
print('Total a pagar: R$ {:.2f}'.format(total))
#---------------------------------------------------------------------
km = float(input('Quantidade de Km percorridos pelo carro: '))
dia = int(input('Quantidade de dias que o carro foi alugado: '))
total = (km * 0.15) + (dia * 60)
print('Total a pagar: R$ {:.2f}'.format(total))