from random import randint
from time import sleep
lista = []
jogo = []
fim = 1
n = int(input('Digite quantos jogos vai querer sortear: '))
while fim <= n:
    cont = 0
    while True:
        x = randint(1, 60)
        if x not in lista:
            lista.append(x)
            cont += 1
        if cont >= 6:
            break
    fim += 1
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
for i in range(len(jogo)):
    print(f'Jogo {i+1}: {jogo[i]}')
    sleep(1)

