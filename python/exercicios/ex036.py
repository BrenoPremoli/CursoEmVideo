casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite em quantos anos será pago o empréstimo: '))
prestacao = casa / (anos * 12)
minimo = salario * (30 / 100)
print('A prestação a ser paga por {} anos tem o valor de R$ {:.2f}'.format(anos, prestacao))
if prestacao > minimo:
    print('\nEmpréstimo reprovado.')
else:
    print('\nEmpréstimo aprovado.')

