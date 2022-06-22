def notas(*num, show=True):
    """
    NOTAS E SITUAÇÕES - ALUNOS
    num - notas dos alunos
    show - mostra a situação dos alunos
    return - dicionário com os dados da turma
    """
    nun = {}
    soma = 0
    nun['total'] = len(num)
    nun['maior'] = max(num)
    nun['menor'] = min(num)
    nun['media'] = sum(num) / len(num)
    if show:
        if nun['media'] > 7:
            nun['situacao'] = 'BOA'
        elif nun['media'] >= 5:
            nun['situacao'] = 'RAZOÁVEL'
        else:
            nun['situacao'] = 'RUIM'
    return nun



avalia = notas(9, 10, 5.5, 2.5, 8.5, show=True)
print(avalia)
help(notas)