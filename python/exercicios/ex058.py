from random import randint
print('\033[34mVou pensar em um número entre 0 e 10. Tente advinhar!\033[m')
cont = 1
x = randint(0, 10)
n = int(input('Escolha um número de 0 a 10: '))
while x != n:
    if n < x:
        n = int(input('Mais... Tente de novo: '))
        cont += 1
    elif n > x:
        n = int(input('Menos... Tente de novo: '))
        cont += 1
print('Acertou tentando {} vezes. Parabéns!'.format(cont))
# ====================================================================================
print('\033[34mVou pensar em um número entre 0 e 10. Tente advinhar!\033[m')
x = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    n = int(input('Escolha um número de 0 a 10: '))
    palpites += 1
    if n == x:
        acertou = True
    else:
        if n < x:
            n = int(input('Mais... Tente de novo: '))
        elif n > x:
            n = int(input('Menos... Tente de novo: '))
print('Acertou tentando {} vezes. Parabéns!'.format(cont))

