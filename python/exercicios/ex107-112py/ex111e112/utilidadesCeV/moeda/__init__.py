def metade(preco = 0, show=True):
    preco /= 2
    if show == True:
        return moeda(preco)
    else:
        return preco


def dobro(preco = 0, show=True):
    preco *= 2
    if show == True:
        return moeda(preco)
    else:
        return preco


def aumento(preco = 0, taxa = 0, show=True):
    preco = preco + (preco * (taxa / 100))
    if show == True:
        return moeda(preco)
    else:
        return preco


def reduz(preco = 0, taxa = 0, show=True):
    preco = preco - (preco * (taxa / 100))
    if show == True:
        return moeda(preco)
    else:
        return preco


def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa1=10, taxa2=5):
    print(f'Preço: {moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{taxa1}% de aumento: \t{aumento(preco, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{reduz(preco, taxa2, True)}')

