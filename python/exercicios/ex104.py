def leiaInt(x):
    valor = 0
    while True:
        n = str(input(x))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print('\033[0;31mERRO. Tente Novamente.\033[m')
n = leiaInt('Digite um número: ')
print(f'Número digitado: {n}')