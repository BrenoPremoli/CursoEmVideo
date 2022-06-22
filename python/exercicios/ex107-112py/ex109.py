import moeda

n = float(input('Digite o preço R$ '))
print(f'Medade de {moeda.moeda(n)}: {moeda.metade(n, True)}')
print(f'Dobro de {moeda.moeda(n)}: {moeda.dobro(n, True)}')
print(f'Aumento de 10% de {moeda.moeda(n)}: {moeda.aumento(n, 10, True)}')
print(f'Redução de 13% de {moeda.moeda(n)}: {moeda.reduz(n, 13, True)}')