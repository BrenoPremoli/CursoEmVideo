lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batatas Fritas')
for i in lanche:
    print(f'Irei comer {i} ')
print()
for i in range(0, len(lanche)):
    print(f'Irei comer {lanche[i]} na posição {i} ')
print()
for pos, i in enumerate(lanche):
    print(f'Irei comer {i} na posição {pos} ')
print()
print(sorted(lanche))  # Ordem alfabética
print()
# =============================================================
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))  # Quantidade de número na tupla
print(c.count(2))  # Contar elementos
print(c.index(8))  # Posição dos elementos
print()
# ================================================================
pessoa = ('Breno', 18, 'M', 59.60)
del(pessoa) # Apagar tupla
print(pessoa)