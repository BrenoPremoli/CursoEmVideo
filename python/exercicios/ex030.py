n = int(input('\033[35mDigite um número: '))
if n % 2 == 0:
    print('{}{}{} é PAR'.format('\033[34m',n,'\033[m'))
else:
    print('{}{}{} é ÍMPAR'.format('\033[34m',n,'\033[m'))