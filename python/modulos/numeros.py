import uteismod

num = int(input('Digite um valor: '))
fat = uteismod.fatorial(num)
print(f'Fatorial de {num}: {fat}')
print(f'Dobro de {num}: {uteismod.dobro(num)}')
print(f'Triplo de {num}: {uteismod.triplo(num)}')
# ================================================
from uteispack import numeros

num = int(input('\nDigite um valor: '))
fat = numeros.fatorial(num)
print(f'Fatorial de {num}: {fat}')
print(f'Dobro de {num}: {numeros.dobro(num)}')
print(f'Triplo de {num}: {numeros.triplo(num)}')