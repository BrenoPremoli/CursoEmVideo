def voto(v):
    from datetime import datetime
    idade = datetime.now().year - v
    if idade >= 18:
        return f'{idade} anos: VOTO OBRIGATÓRIO '
    elif idade < 18 and idade >= 16:
        return f'{idade} anos: VOTO OPCIONAL '
    else:
        return f'{idade} anos: NÃO VOTA'


ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))