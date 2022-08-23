v = float(input('Digite a velocidade em que o veículo está (em Km/h): '))
if v > 80:
    m = v - 80
    multa = m * 7
    print('\033[1;31mVocê ultrapassou o limite de velocidade em {:.1f} Km, sua multa é de: R$ {:.2f}'.format(m,multa))
else:
    print('\033[33mCarro na velocidade permitida.')