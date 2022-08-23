import random
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = random.choice(lista)
print('O aluno sorteado foi: {}'.format(sorteado))
# ------------------------------------------------------------
print()
from random import choice
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = choice(lista)
print('O aluno sorteado foi: {}'.format(sorteado))