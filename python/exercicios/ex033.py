
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro  número: '))
maior = 0
menor = 0
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
print()
# ---------------------------------------------------------------------------
cores = {'limpa':'\033[0;0;0m',
        'red':'\033[1;31;40m',
        'green':'\033[1;32;40m'}
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro  número: '))
maior = n1
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior: {}{}{}'.format(cores['green'], maior, cores['limpa']))
print('Menor: {}{}{}'.format(cores['red'], menor, cores['limpa']))
