def soma(a, b):
    print(f'{a} + {b} = {a+b}')


soma(4, 5)
soma(8, 9)
soma(2, 1)
print()
# =================================================================
def contado(*num):
    for valor in num:
        print(valor, end=' ')
    print('FIM!\n')


contado(2, 1, 7)
# =================================================================
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(8, 0)
contador(4, 4, 7, 6, 2)
print()
# ===================================================================
def dobra(lista):
    cont = 0
    while cont < len(lista):
        lista[cont] *= 2
        cont += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
