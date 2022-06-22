conta = str(input('Digite a expressão: '))
pilha = []
for simbolo in conta:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.\n')
# ========================================
conta = (str(input('Digite a expressão: ')))
contpa = 0
contpf = 0
if '(' in conta:
    contpa = conta.count('(')
if ')' in conta:
    contpf = conta.count(')')
if contpa == contpf:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')