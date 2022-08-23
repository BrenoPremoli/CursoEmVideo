from utilidadesCeV import moeda
n = float(input('Digite o preço R$ '))
print(f'Medade de {moeda.moeda(n)}: {moeda.moeda(moeda.metade(n))}')
print(f'Dobro de {moeda.moeda(n)}: {moeda.moeda(moeda.dobro(n))}')
print(f'Aumento de 10% de {moeda.moeda(n)}: {moeda.moeda(moeda.aumento(n, 10))}')