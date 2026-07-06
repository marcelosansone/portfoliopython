n = int(input('Digite um número inteiro: '))
c = n
f = 1
print('Calculando fatorial de {}! = '.format(c), end="")
while c > 0:
    print('{}'.format(c), end=" ")
    print(' x ' if c > 1 else ' = ', end=" ")
    f *= c
    c -= 1
print('{}'.format(f), end=" ")
