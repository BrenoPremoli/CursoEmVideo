n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('O primeiro valor ({}) é maior o segundo valor ({})'.format(n1, n2))
elif n1 < n2:
    print('O primeiro valor ({}) é menor o segundo valor ({})'.format(n1, n2))
else:
    print('O primeiro valor ({}) é igual ao segundo valor ({})'.format(n1, n2))