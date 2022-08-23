a = 3
b = 5
print('Os valores são: \33[1;35;40m{}\33[m e \33[1;31;40m{}\33[m'.format(a, b))
print()
nome = 'Breno'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\33[4;32m',nome,'\33[m'))
print()
nome = 'Breno'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[1;30;107m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
print()
print('\033[31mOlá mundo!')
print()
print('\033[7;33;44mOlá mundo!\033[m')
print()
print('\033[1;31;43mOlá mundo!')