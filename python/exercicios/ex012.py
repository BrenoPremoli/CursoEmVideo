preco = float(input('Digite o preço do produto: R$ '))
desconto = preco - (preco * (5 / 100))
print('O novo preço do produto será: R$ {:.2f}'.format(desconto)) 