salario = float(input('Digite seu salário: R$ '))
aumento = salario + (salario * (15 / 100))
print('O novo salário será de: R$ {:.2f}'.format(aumento))