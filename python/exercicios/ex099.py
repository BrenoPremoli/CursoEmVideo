def maior(*num):
    maior = 0
    print(f'{num} - Foram analisados {len(num)} valores.')
    for i in range(len(num)):
        if i == 0:
            maior = num[i]
        if maior < num[i]:
            maior = num[i]
    print(f'Maior valor informado: {maior}\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


