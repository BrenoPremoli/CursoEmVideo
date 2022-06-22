peso_maior = 0
peso_menor = 0
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        elif peso < peso_menor:
            peso_menor = peso
print('Maior peso: {} Kg'.format(peso_maior))
print('Menor peso: {} Kg'.format(peso_menor))