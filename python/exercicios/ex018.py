import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))
# ----------------------------------------------------------
from math import radians, sin, cos, tan
import math
ang = float(input('Digite um ângulo: '))
print('Seno: {:.2f}'.format(sin(radians(ang))))
print('Cosseno: {:.2f}'.format(cos(radians(ang))))
print('Tangente: {:.2f}'.format(tan(radians(ang))))

