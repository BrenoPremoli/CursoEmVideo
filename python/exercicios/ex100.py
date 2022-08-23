from random import randint
def sorteia():
    lista = []
    for i in range(5):
        lista.append(randint(1, 10))
    print(f'Números sorteados: {lista}')
    somaPar(lista)
def somaPar(list):
    soma = 0
    for i in range(5):
        if list[i] % 2 == 0:
            soma += list[i]
    print(f'Soma dos valores pares de {list}: {soma}')
sorteia()