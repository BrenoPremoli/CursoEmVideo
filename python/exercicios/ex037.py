n = int(input('Digite um número inteiro: '))
b = int(input('Qual será a base de conversão? Escolha: \n1-Binário \n2-Octal \n3-Hexadecimal \nDigite: '))
print('Opção escolhida: {}'.format(b))
if b == 1:
    print('{} em binário é: {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('{} em octal é: {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} em hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('Número inválido.')
