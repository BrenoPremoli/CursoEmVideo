n = int(input('Informe um número: '))
tot_fat = 1
print('{}! = '.format(n), end='')
while n > 1:
    print('{} X '.format(n), end='')
    tot_fat = tot_fat * n
    n = n - 1
print('1 = ', end='')
print(tot_fat)
# ===========================================
n = int(input('Informe um número: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))