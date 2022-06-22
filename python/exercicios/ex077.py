palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
           'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
           'PROGRAMADOR', 'FUTURO')
for i in range(len(palavra)):
    print(f'\nNa palavra {palavra[i]} tem as vogais: ', end='')
    for j in palavra[i]:
        if j.lower() in 'aeiou':
            print(j.lower(), end=' ')
