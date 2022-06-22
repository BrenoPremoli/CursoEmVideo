n = int(input('Digite o número de termos: '))
x1 = 0
x2 = 1
print('{} -> {}'.format(x1, x2), end=' -> ')
while n >= 3:
    x3 = x1 + x2
    print(x3, end=' -> ')
    x1 = x2
    x2 = x3
    n -= 1
print('Fim')
# ===========================================================
n = 0
m = 1
contador = int(input('Quantos termos deseja mostrar? '))
print(n, end=' -> ')
while contador >= 2:
    x = m + n
    print(x, end=' -> ')
    m = n
    n = x
    contador -= 1
print('Fim')