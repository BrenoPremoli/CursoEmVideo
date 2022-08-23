def leiaDinheiro(preco):
    ok = False
    while not ok:
        entrada = str(input(preco)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" não é válido.\033[m')
        else:
            ok = True
            return float(entrada)
def leiaInt(preco):
    valor = 0
    while True:
        n = str(input(preco))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print('\033[0;31mERRO. Tente Novamente.\033[m')