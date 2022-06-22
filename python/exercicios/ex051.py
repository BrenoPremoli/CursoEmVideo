t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (10 - 1) * r
for i in range(t, decimo + r, r):
    print(i, end=' -> ')
print('Acabou')