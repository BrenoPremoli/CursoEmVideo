soma_idade = 0
idade_homem = 0
cont_mulher = 0
homem = ''
for i in range(1,5):
    print('{}ª Pessoa'.format(i))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    soma_idade += idade
    sexo = str(input('Digite o sexo M/F: '))
    if i == 1 and (sexo == 'm' or sexo == 'M'):
        homem = nome
        idade_homem = idade
    if (sexo == 'm' or sexo == 'M') and idade > idade_homem:
        homem = nome
        idade_homem = idade
    if (sexo == 'f' or sexo == 'F') and idade < 20:
        cont_mulher += 1
media = soma_idade / 4
print('Média de idade do grupo: {:.1f} anos.'.format(media))
print('Nome do homem mais velho: {} que possui {} anos.'.format(homem, idade_homem))
print('Total de mulheres com menos de 20 anos: {} mulheres.'.format(cont_mulher))