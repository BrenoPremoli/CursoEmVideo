try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b
except (ValueError, TypeError):
    print('ERRO - Houve um problema com os tipos de dados inseridos.')
except ZeroDivisionError:
    print('ERRO - Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('\nERRO - O usuário não informou dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print('Deu certo :) \nResultado:', c)
finally:
    print('Obrigado!')