t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
contador = 10
while contador > 0:
    while contador > 0:
        print(t, end=' -> ')
        t += r
        cont += 1
        contador -= 1
    print('PAUSA')
    contador = int(input('Quantos termos deseja mostrar a mais? '))
print('Total de termos mostrados: {}'.format(cont))