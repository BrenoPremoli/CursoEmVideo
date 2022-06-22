import moeda

n = float(input('Digite o preço R$ '))
print(f'Medade: R$ {moeda.metade(n)}')
print(f'Dobro: R$ {moeda.dobro(n)}')
print(f'Aumento de 10%: R$ {moeda.aumento(n, 10)}')
print(f'Redução de 13%: R$ {moeda.reduz(n, 13)}')