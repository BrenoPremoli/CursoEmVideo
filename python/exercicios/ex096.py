def terreno(larg, compr):
    print(f'A área de de um terreno {larg:.1f}x{compr:.1f} é de {larg*compr:.1f}m²')


largura = float(input('Digite a largura (m): '))
comprimento = float(input('Digite o comprimento (m): '))
terreno(largura, comprimento)