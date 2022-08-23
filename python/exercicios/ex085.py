all = []
par = []
impar = []
for i in range(7):
    all.append(int(input(f'Digite o {i+1}º valor: ')))
    if all[i-i] % 2 == 0:
        par.append(all[:])
    else:
        impar.append(all[:])
    all.clear()
par.sort()
impar.sort()
print(f'Valores pares: {par}')
print(f'Valores ímpares: {impar}\n')
# ====================================
num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Valores pares: {num[0]}')
print(f'Valores ímpares: {num[1]}\n')