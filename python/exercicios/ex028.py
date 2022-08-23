from random import randint
from time import sleep
print('=' * 55)
print('\033[34mVou pensar em um número entre 0 e 5. Tente advinhar!\033[m')
print('=' * 55)
x = randint(0,5)
n = int(input('Escolha um número de 0 a 5: '))
print('\033[35mProcessando...\033[m')
sleep(1)
if x == n:
    print('\033[33mParabéns você acertou! Eu escolhi o número {}.\033[m'.format(x))
else:
    print('\033[31mVocê errou, eu escolhi o número {}.\033[m'.format(x))