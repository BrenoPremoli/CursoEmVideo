import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('Raíz quadrada: {}'.format(raiz))
print('Raíz quadrada arredondada para cima: {}'.format(math.ceil(raiz)))
print('Raíz quadrada arredondada para baixo: {}'.format(math.floor(raiz)))
print('Raíz quadrada de duas casas: {:.2f}'.format(raiz))
#----------------------------------------------------------------------------------
print()
from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('Raíz quadrada: {}'.format(raiz))
print('Raíz quadrada arredondada para cima: {}'.format(ceil(raiz)))
print('Raíz quadrada arredondada para baixo: {}'.format(floor(raiz)))
#-----------------------------------------------------------------------------------
print()
import random
num = random.random()
n = random.randint(1, 20)
print('Número aleatório: {}'.format(num))
print('Número aleatório: {}'.format(n))
#-----------------------------------------------------------------------------------
print()
import emoji
print(emoji.emojize("Olá, Mundo :earth_americas:!", use_aliases=True))
