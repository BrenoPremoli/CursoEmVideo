import random
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('Ordem de apresentação:')
print(lista)
# ------------------------------------------------------------
print()
from random import shuffle
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('Ordem de apresentação:')
print(lista)