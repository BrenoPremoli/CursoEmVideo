salario = float(input('Digite o salário: R$ '))
if salario <= 1250.00:
    n_salario = salario + (salario * 15 / 100)
else:
    n_salario = salario + (salario * 10 / 100)
print('Novo salário: {:.2f}'.format(n_salario))