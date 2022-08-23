num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
       'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while True:
       if n >= 0 and n <= 20:
              print(f'Você digitou o número {num[n]}')
              break
       else:
              print('Número inválido. Tente novamente. ', end='')
              n = int(input('Digite um número entre 0 e 20: '))