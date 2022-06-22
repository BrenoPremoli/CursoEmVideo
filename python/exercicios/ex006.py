n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('Número: {} \nDobro: {} \nTriplo: {} \nRaíz Quadrada: {:.2f}'.format(n, dobro, triplo, raiz))
#-------------------------------------------------------------------------------------------------
print('Número: {} \nDobro: {} \nTriplo: {} \nRaíz Quadrada: {:.2f}'.format(n, (n*2), (n*3), pow(n, (1/2))))