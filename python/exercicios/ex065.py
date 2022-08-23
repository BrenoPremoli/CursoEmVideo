cont = soma = 0
opcao = 'S'
n = int(input('Digite um número: '))
maior = menor = n
while opcao == 'S':
    soma += n
    cont += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if opcao == 'S':
        n = int(input('Digite um número: '))
media = soma / cont
print('Números digitados: {} \nMédia: {:.2f} \nMaior valor: {} \nMenor valor: {}'.format(cont, media, maior, menor))
# =======================================================================================================================
cont = soma = maior = menor = 0
opcao = 'S'
while opcao == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Números digitados: {} \nMédia: {:.2f} \nMaior valor: {} \nMenor valor: {}'.format(cont, media, maior, menor))
