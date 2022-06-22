s = 0
cont = 0
for i in range(1, 501):  # for i in range(1, 501, 2)
    if i % 2 != 0:
        if i % 3 == 0:
            s += i
            cont += 1
print('Valore encontrados: {} \nSoma dos valores: {}'.format(cont, s))