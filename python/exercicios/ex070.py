total = quantidade = barato = cont = 0
produto = ' '
while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        quantidade += 1
    if cont == 1:
        barato = preco
        produto = nome_produto
    else:
        if barato > preco:
            barato = preco
            produto = nome_produto
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'Total gasto na compra: R$ {total:.2f}')
print(f'Quantidade de produtos custam mais de R$1000: {quantidade}')
print(f'Nome do produto mais barato: {produto} por R$ {barato:.2f}')
# ===========================================================================
total = quantidade = barato = cont = 0
produto = ' '
while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        quantidade += 1
    if cont == 1 or preco < barato:
        barato = preco
        produto = nome_produto
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'Total gasto na compra: R$ {total:.2f}')
print(f'Quantidade de produtos custam mais de R$1000: {quantidade}')
print(f'Nome do produto mais barato: {produto} por R$ {barato:.2f}')