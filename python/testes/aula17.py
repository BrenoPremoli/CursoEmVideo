num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Not find')
num.remove(2)
print(num)
print(f'Há {len(num)} elementos nesta lista.\n')
# ==============================================
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for i, j in enumerate(valores):
    print(f'Posição {i} tinha o valor {j}.')
print()
# ================================================
a = [2, 3, 4, 7]
b = a[:]
c = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')