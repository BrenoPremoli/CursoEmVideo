preco = float(input('Digite o valor a ser pago: R$ '))
escolha = int(input('Escolha o método de pagamento: \n1- À vista dinheiro/cheque \n2- À vista no cartão \n3- Até 2x no cartão \n4- 3x ou mais no cartão \nEscolha a opção: '))
if escolha == 1:
    preco_novo = preco - (preco * (10 /100))
    print('Total a ser pago: R$ {:.2f}'.format(preco_novo))
elif escolha == 2:
    preco_novo = preco - (preco * (5 /100))
    print('Total a ser pago: R$ {:.2f}'.format(preco_novo))
elif escolha == 3:
    parcelas = preco / 2
    print('A compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcelas))
    print('Total a ser pago: R$ {:.2f}'.format(preco))
elif escolha == 4:
    juros = int(input('Digite o número de parcelas (3 ou mais): '))
    preco_novo = preco + (preco * (20 /100))
    parcelas = preco_novo / juros
    print('A compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(juros, parcelas))
    print('Total a ser pago: R$ {:.2f}'.format(preco_novo))
else:
    print('Opção inválida. Tente novamente.')