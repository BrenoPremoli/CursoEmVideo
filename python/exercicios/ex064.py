numero = soma = cont = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        soma += numero
        cont += 1
print('Soma dos {} números: {}'.format(cont, soma))
# =================================================================
soma = cont = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('Soma dos {} números: {}'.format(cont, soma))