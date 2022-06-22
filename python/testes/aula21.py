def contar(i, f, g):
    """
    Documentação da função
          docstring
    """
    cont = i
    while cont <= f:
        print(f'{cont} ', end='')
        cont += g


help(contar)


# ======================================================
def somar(i=0, f=0, g=0):  # PARÂMETRO OPCIONAL
    s = i + f + g
    print(s)


somar(1, 2)
somar(f=3, g=2)


# ========================================================
def funcao(x):
    global n1  # padroniza o uso da variável na função e fora dela
    n1 = 4
    print(f'\nn1 dentro vale {n1}')

n1 = 2
funcao(n1)
print(f'n1 fora vale {n1}')


# ==========================================================
def somar(i=0, f=0, g=0):  # RETURN
    s = i + f + g
    return s


soma = somar(3, 2, 5)
print(f'\n{soma}')


# ============================================================
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('\nDigite um número: '))
print(fatorial(n))