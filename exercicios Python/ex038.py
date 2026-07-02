n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite  o segundo núemro:'))
if n1 > n2:
    print('O número PRMEIRO {} é o maior'.format(n1))
elif n1 < n2:
    print('O PRIMEIRO número {} é o menor'.format(n1))

if n2 > n1:
    print('O SEGUNDO número {} é o maior '.format(n2))
elif n2 < n1:
    print('O SEGUNDO número é o menor '.format(n2))
else:
    print('Os números são IGUAIS!')