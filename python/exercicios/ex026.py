frase = input('Digite uma frase: ').strip().lower()
print('Quantidade de vezes que aparece a letra "A": {}'.format(frase.count('a')))
print('Posição em que a letra "A" aparece pela primeira vez: {}'.format(frase.find('a')+1))
print('Posição em que a letra "A" aparece pela última vez: {}'.format(frase.rfind('a')+1))


