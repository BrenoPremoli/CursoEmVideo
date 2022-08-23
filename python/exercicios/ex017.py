import math
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('Comprimento da hipotenusa: {:.2f}'.format(hipotenusa))
# -----------------------------------------------------------------------
print()
from math import hypot
opost = float(input('Digite o comprimento do cateto oposto: '))
adjacent = float(input('Digite o comprimento do cateto adjacente: '))
print('Comprimento da hipotenusa: {:.2f}'.format(hypot(opost, adjacent)))
# -----------------------------------------------------------------------
print()
opo = float(input('Digite o comprimento do cateto oposto: '))
adjace = float(input('Digite o comprimento do cateto adjacente: '))
hipote = ((opo ** 2) + (adjace ** 2)) ** (1/2)
print('Comprimento da hipotenusa: {:.2f}'.format(hipote))