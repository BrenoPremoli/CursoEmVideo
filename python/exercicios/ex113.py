def leiaInt(x):
    while True:
        try:
            valor1 = int(input(x))
        except (ValueError, TypeError):
            print('\033[0;31mERRO - Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nERRO - O usuário não informou o número!\033[m')
            return 0
        else:
            return valor1


def leiaFloat(y):
    while True:
        try:
            valor2 = float(input(y))
        except (ValueError, TypeError):
            print('\033[0;31mERRO - Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nERRO - O usuário não informou o número!\033[m')
            return 0
        else:
            return valor2


n = leiaInt('Digite um Inteiro: ')
m = leiaFloat('Digite um Real: ')
print(f'Valor inteiro: {n}')
print(f'Valor real: {m}')