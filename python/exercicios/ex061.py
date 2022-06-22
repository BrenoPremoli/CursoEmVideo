t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
while cont < 10:
    print(t, end=' -> ')
    t += r
    cont += 1
print('Acabou')