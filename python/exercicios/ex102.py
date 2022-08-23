def fatorial(num):
    """
    Calcula o fatorial de número.
    num: o número a ser calculado.
    show: mostrar ou não a conta.
    return: o valor do fatorial de número n.
    """
    f = 1
    cont = 1
    for c in range(num, 0, -1):
        f *= c
        if num > 1:
            print(f'{num} x ', end='')
            num -= cont
        else:
            print(f'1 = {f}')
fatorial(5)
# =================================================
def fatorial(num, show=False):
    """
    Calcula o fatorial de número.
    num: o número a ser calculado.
    show: mostrar ou não a conta.
    return: o valor do fatorial de número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
print(fatorial(5, show=False))
help(fatorial)