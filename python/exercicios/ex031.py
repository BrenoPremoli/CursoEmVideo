d = float(input('Digite a distância da viagem: '))
if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45
print('Preço da viagem: R$ {:.2f}'.format(preco))
print()
# ----------------------------------------------------------------
d = float(input('Digite a distância da viagem: '))
preco = d * 0.5 if d <= 200 else d * 0.45
print('Preço da viagem: R$ {:.2f}'.format(preco))